import os
import sys
import json
import re
import glob
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

# =====================================================
# CONFIG
# =====================================================

DEFAULT_MODEL = "gpt-4o-mini"

# =====================================================
# ENV SETUP
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
        "  python3 reconstruct.py <file_path> [start_page] [end_page] [--model MODEL]\n"
        "  python3 reconstruct.py query \"your question\" [--model MODEL]"
    )

mode = "extract"
model_name = DEFAULT_MODEL

# Handle --model flag
if "--model" in sys.argv:
    idx = sys.argv.index("--model")
    try:
        model_name = sys.argv[idx + 1]
    except IndexError:
        raise ValueError("Provide model name after --model")
    del sys.argv[idx:idx+2]

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

# =====================================================
# QUERY MODE
# =====================================================

if mode == "query":

    json_files = (
        glob.glob("outputs/json/books/*.json") +
        glob.glob("outputs/json/papers/*.json")
    )

    if not json_files:
        raise ValueError("No structured JSON memory found.")

    combined_memory = []

    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            combined_memory.append(json.load(f))

    memory_text = json.dumps(combined_memory, indent=2)

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided structured memory."},
            {"role": "user", "content": memory_text + "\n\nQuery:\n" + str(user_query)}
        ],
        temperature=0.2,
    )

    print("\n--- QUERY RESULT ---\n")
    print(response.choices[0].message.content)
    sys.exit(0)

# =====================================================
# TEXT EXTRACTION
# =====================================================

def extract_text(path):
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        text = ""
        total_pages = len(reader.pages)

        if start_page and end_page:
            if start_page < 1 or end_page > total_pages:
                raise ValueError(f"Page range must be 1–{total_pages}")
            for i in range(start_page - 1, end_page):
                text += reader.pages[i].extract_text() or ""
        else:
            for page in reader.pages:
                text += page.extract_text() or ""
        return text

    elif path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    else:
        raise ValueError("Unsupported file type (.pdf or .txt only)")

document_text = extract_text(file_path)

if not document_text or not document_text.strip():
    raise ValueError("No text extracted.")

# =====================================================
# RECONSTRUCTION PROMPT
# =====================================================

prompt = f"""
Reconstruct the author's argument in high technical detail.

Constraints:
- Do NOT generalize upward.
- Avoid vague phrasing.
- Extract as many distinct concrete claims as possible.
- Every claim must correspond to something explicitly stated or strongly implied.
- No generic rationale section. Only alignment classification.


# Style constraints:
- Do NOT refer to “the author,” “the text,” or “this chapter.”
- Do NOT describe what the document does.
- State the content directly as propositions.
- Write as if presenting the claims themselves, not commenting on them.

# Title
- ...

# Core Argument Reconstruction
- Multi-paragraph detailed reconstruction in concrete mechanistic terms.

# Specific Claims (dense extraction)
For each claim:
- Claim:
- Alignment: Supported / Partially supported / Contested / Speculative / Contradicted
Alignment must be determined as follows:

Supported:
    The claim is widely accepted in standard academic treatments of the field.

Partially supported:
    The core phenomenon is accepted, but the interpretation here extends beyond consensus.

Contested:
    There is active disagreement in peer-reviewed literature.

Speculative:
    The claim proposes a mechanism or interpretation not established in mainstream research.

Contradicted:
    The claim conflicts with well-established empirical findings.

Do not default to Supported.
If uncertain, choose Partially supported or Speculative.

# Technical Concepts (explain each fully)
For each term:
- Term:
- Definition (precise, how used here)
- Mainstream status: Established / Emerging / Contested / Fringe

# Logical Chain
- Step-by-step mapping from observation to interpretation.


After the Markdown, output JSON between:

BEGIN_STRUCTURED_JSON
{{ ... }}
END_STRUCTURED_JSON

JSON must contain:
- claims: [{{claim, alignment}}]
- concepts: [{{term, definition, mainstream_status}}]
- logical_chain: [...]

DOCUMENT:
{document_text}
"""

response = client.chat.completions.create(
    model=model_name,
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,
)

full_output = response.choices[0].message.content

print("\n--- RAW OUTPUT ---\n")
print(full_output)

# =====================================================
# JSON EXTRACTION
# =====================================================

json_pattern = r"BEGIN_STRUCTURED_JSON\s*(\{.*?\})\s*END_STRUCTURED_JSON"
match = re.search(json_pattern, full_output, re.DOTALL)

structured_data = None
markdown_content = full_output

if match:
    json_str = match.group(1)
    structured_data = json.loads(json_str)
    markdown_content = re.sub(json_pattern, "", full_output, flags=re.DOTALL)

# =====================================================
# OUTPUT WRITING
# =====================================================

input_path = Path(file_path)
base_name = input_path.stem

if start_page and end_page:
    base_name = f"{base_name}_p{start_page}-{end_page}"

model_tag = model_name.replace("-", "")
base_name = f"{base_name}_reconstruct_{model_tag}"

# Directory routing
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

with open(output_file, "w", encoding="utf-8") as f:
    f.write(markdown_content)

if structured_data:
    with open(json_file, "w", encoding="utf-8") as jf:
        json.dump(structured_data, jf, indent=2)

print(f"\nSaved markdown to {output_file}")
if structured_data:
    print(f"Saved structured JSON to {json_file}")