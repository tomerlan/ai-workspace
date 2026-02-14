import os
import sys
import json
import re
import glob
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
from datetime import datetime

# =====================================================
# CONFIG
# =====================================================

MODEL_NAME = "gpt-4o-mini"
PROMPT_VERSION = "v4_strict_consensus_detailed"

# =====================================================
# LOAD API KEY
# =====================================================

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment.")

client = OpenAI(api_key=api_key)

# =====================================================
# ARGUMENT PARSING
# =====================================================

if len(sys.argv) < 2:
    raise ValueError(
        "Usage:\n"
        "  python3 summarize.py <file_path> [start_page] [end_page]\n"
        "  python3 summarize.py query \"your question\""
    )

mode = "extract"

if sys.argv[1] == "query":
    mode = "query"
    if len(sys.argv) < 3:
        raise ValueError("Provide a query string.")
    user_query = sys.argv[2]
else:
    file_path = sys.argv[1]
    start_page = None
    end_page = None

    if len(sys.argv) == 4:
        start_page = int(sys.argv[2])
        end_page = int(sys.argv[3])
    elif len(sys.argv) not in [2, 4]:
        raise ValueError("Provide either no page range or both start and end page.")

# =====================================================
# QUERY MODE
# =====================================================

if mode == "query":

    json_files = (
        glob.glob("outputs/json/books/*.json") +
        glob.glob("outputs/json/papers/*.json")
    )

    if not json_files:
        raise ValueError("No structured JSON files found.")

    combined_memory = []
    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            combined_memory.append(json.load(f))

    memory_text = json.dumps(combined_memory, indent=2)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "Use only the provided structured memory. Do not hallucinate. If information is absent, state that explicitly."
            },
            {
                "role": "user",
                "content": (
                    "Structured research memory:\n\n"
                    + memory_text +
                    "\n\nUser query:\n"
                    + user_query +
                    "\n\nAnswer precisely."
                )
            }
        ],
        temperature=0.2,
    )

    print("\n--- QUERY RESULT ---\n")
    print(response.choices[0].message.content)
    sys.exit(0)

# =====================================================
# EXTRACTION MODE
# =====================================================

def extract_text(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    elif file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""
        total_pages = len(reader.pages)

        if start_page and end_page:
            if start_page < 1 or end_page > total_pages:
                raise ValueError(f"Page range must be between 1 and {total_pages}")
            for i in range(start_page - 1, end_page):
                text += reader.pages[i].extract_text() or ""
        else:
            for page in reader.pages:
                text += page.extract_text() or ""

        return text

    else:
        raise ValueError("Unsupported file type. Use .txt or .pdf")

document_text = extract_text(file_path)

if not document_text.strip():
    raise ValueError("No text extracted from file.")

# =====================================================
# STRICT CONSENSUS PROMPT
# =====================================================

prompt = (
    "Produce a detailed research extraction.\n\n"
    "STRICT CONSENSUS STANDARD:\n"
    "- 'Supported' ONLY if textbook-level, widely accepted mainstream science.\n"
    "- If based on niche frameworks, minority models, or speculative biophysical interpretations → NOT Supported.\n"
    "- If uncertain → do NOT label Supported.\n\n"
    "Output format:\n\n"
    "# Title\n"
    "- ...\n\n"
    "# One-sentence thesis\n"
    "- ...\n\n"
    "# Claims\n"
    "For each significant claim:\n"
    "- Claim:\n"
    "- Alignment: Supported / Partially supported / Contested / Speculative / Contradicted\n\n"
    "# Concepts\n"
    "For each specialized term:\n"
    "- Term:\n"
    "- Definition: (2–4 clear technical sentences)\n"
    "- Mainstream status: Established / Emerging / Contested / Fringe\n\n"
    "# Relationships\n"
    "- A -> B\n"
    "- X correlates with Y\n\n"
    "After the Markdown note, output structured JSON between:\n"
    "BEGIN_STRUCTURED_JSON\n"
    "{ ... }\n"
    "END_STRUCTURED_JSON\n\n"
    "JSON must contain:\n"
    "- claims: [{\"claim\": \"...\", \"alignment\": \"...\"}]\n"
    "- concepts: [{\"term\": \"...\", \"definition\": \"...\", \"mainstream_status\": \"...\"}]\n"
    "- relationships: [ ... ]\n\n"
    "DOCUMENT:\n"
    + document_text
)

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,
)

full_output = response.choices[0].message.content

print("\n--- RAW OUTPUT ---\n")
print(full_output)

# =====================================================
# EXTRACT JSON BLOCK
# =====================================================

json_pattern = r"BEGIN_STRUCTURED_JSON\s*(\{.*?\})\s*END_STRUCTURED_JSON"
match = re.search(json_pattern, full_output, re.DOTALL)

structured_data = None
markdown_content = full_output

if match:
    json_str = match.group(1)
    structured_data = json.loads(json_str)
    markdown_content = re.sub(json_pattern, "", full_output, flags=re.DOTALL)
else:
    print("Warning: No structured JSON block found.")

# =====================================================
# OUTPUT WRITING
# =====================================================

input_path = Path(file_path)
base_name = input_path.stem

if start_page and end_page:
    base_name = f"{base_name}_p{start_page}-{end_page}"

if "data/books" in file_path:
    output_dir = Path("outputs/books")
    json_dir = Path("outputs/json/books")
elif "data/papers" in file_path:
    output_dir = Path("outputs/papers")
    json_dir = Path("outputs/json/papers")
else:
    output_dir = Path("outputs")
    json_dir = Path("outputs/json")

output_dir.mkdir(parents=True, exist_ok=True)
json_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / f"{base_name}.md"
json_file = json_dir / f"{base_name}.json"

timestamp = datetime.utcnow().isoformat()
pages_value = f"{start_page}-{end_page}" if start_page and end_page else "full"

metadata = (
    "---\n"
    f"source_file: \"{file_path}\"\n"
    f"pages: \"{pages_value}\"\n"
    f"model: \"{MODEL_NAME}\"\n"
    f"prompt_version: \"{PROMPT_VERSION}\"\n"
    f"generated_at_utc: \"{timestamp}\"\n"
    "chunk_type: \"manual_page_range\"\n"
    "---\n\n"
)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(metadata + markdown_content)

print(f"\nSaved markdown to {output_file}")

if structured_data:
    structured_data.update({
        "source_file": file_path,
        "pages": pages_value,
        "model": MODEL_NAME,
        "prompt_version": PROMPT_VERSION,
        "generated_at_utc": timestamp
    })

    with open(json_file, "w", encoding="utf-8") as jf:
        json.dump(structured_data, jf, indent=2)

    print(f"Saved structured JSON to {json_file}")
else:
    print("No structured JSON saved.")