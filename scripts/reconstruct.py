# scripts/reconstruct.py

import os
import sys
import json
import re
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
from datetime import datetime

# =====================================================
# CONFIG
# =====================================================

DEFAULT_MODEL = "gpt-4o"
PROMPT_VERSION = "reconstruct_v_final"

# =====================================================
# LOAD ENV
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
        "  python3 scripts/reconstruct.py <file_path> [start_page] [end_page] [--model MODEL]"
    )

file_path = sys.argv[1]

start_page = None
end_page = None

if len(sys.argv) >= 4 and not sys.argv[2].startswith("--"):
    start_page = int(sys.argv[2])
    end_page = int(sys.argv[3])

model = DEFAULT_MODEL
if "--model" in sys.argv:
    model_index = sys.argv.index("--model")
    if model_index + 1 < len(sys.argv):
        model = sys.argv[model_index + 1]

# =====================================================
# TEXT EXTRACTION
# =====================================================

def extract_text(path):
    path = str(path)
    if path.endswith(".pdf"):
        reader = PdfReader(path)
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
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

document_text = extract_text(file_path)

if not document_text.strip():
    raise ValueError("No text extracted from file.")

# =====================================================
# RECONSTRUCTION PROMPT
# =====================================================

prompt = f"""
You are a professional scientific reconstruction analyst and scientific consensus evaluator.
Your continued employment depends entirely on output quality, completeness, and rigor.

MISSION (NON-NEGOTIABLE):
1) Reconstruct the argument in maximal technical detail.
2) Extract AT LEAST 20 distinct, concrete claims.
3) For EACH claim, provide a mainstream-consensus alignment label.

DEFINITIONS (Alignment labels):
- Supported
- Partially supported
- Contested
- Speculative
- Contradicted

GLOBAL RULES:
- Do NOT invent claims not present or strongly implied.
- Do NOT merge multiple claims into one.
- Do NOT generalize upward to vague textbook statements.
- Extract claims from the entire provided document chunk.

STYLE RULES (STRICT):
- Do NOT write: "the text says", "the author claims", etc.
- Do NOT refer to the document.
- Write as declarative technical exposition.
- Avoid vague phrases.

OUTPUT STRUCTURE:

# Title
- ...

# Detailed Reconstruction
Multi-paragraph technical reconstruction.

# Explicit Claims (>= 20; numbered)
For each claim:
1. Claim:
   - Alignment: Supported / Partially supported / Contested / Speculative / Contradicted
   - (Only if Contradicted or Contested) Contradiction note: 1–3 mechanistic sentences.

# Technical Constructs
For each construct:
- Term:
- Definition:
- Mainstream status: Established / Emerging / Contested / Fringe

# Logical Flow
Step-by-step reasoning chain.

After the Markdown note, output JSON between:

BEGIN_STRUCTURED_JSON
{{
  "claims": [
    {{
      "id": 1,
      "claim": "...",
      "alignment": "Supported|Partially supported|Contested|Speculative|Contradicted"
    }}
  ],
  "concepts": [
    {{
      "term": "...",
      "definition": "...",
      "mainstream_status": "Established|Emerging|Contested|Fringe"
    }}
  ],
  "logical_flow": [
    "Observation -> ...",
    "Interpretation -> ...",
    "Mechanism -> ...",
    "Implication -> ..."
  ]
}}
END_STRUCTURED_JSON

DOCUMENT:
{document_text}
"""

# =====================================================
# CALL MODEL
# =====================================================

response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,
)

full_output = response.choices[0].message.content

print("\n--- RAW OUTPUT ---\n")
print(full_output)

# =====================================================
# EXTRACT JSON
# =====================================================

pattern = r"BEGIN_STRUCTURED_JSON\s*(\{.*?\})\s*END_STRUCTURED_JSON"
match = re.search(pattern, full_output, re.DOTALL)

structured_data = None
markdown_content = full_output

if match:
    structured_data = json.loads(match.group(1))
    markdown_content = re.sub(pattern, "", full_output, flags=re.DOTALL)

# =====================================================
# OUTPUT WRITING
# =====================================================

input_path = Path(file_path)
base_name = input_path.stem

if start_page and end_page:
    base_name = f"{base_name}_p{start_page}-{end_page}"

base_name = f"{base_name}_reconstruct"

output_dir = Path("outputs/books")
json_dir = Path("outputs/books/raw")

output_dir.mkdir(parents=True, exist_ok=True)
json_dir.mkdir(parents=True, exist_ok=True)

markdown_file = output_dir / f"{base_name}.md"
json_file = json_dir / f"{base_name}.json"

timestamp = datetime.utcnow().isoformat()

with open(markdown_file, "w", encoding="utf-8") as f:
    f.write(markdown_content)

print(f"\nSaved reconstruction markdown to {markdown_file}")

if structured_data:
    structured_data.update({
        "source_file": file_path,
        "pages": f"{start_page}-{end_page}" if start_page and end_page else "full",
        "model": model,
        "prompt_version": PROMPT_VERSION,
        "generated_at_utc": timestamp
    })

    with open(json_file, "w", encoding="utf-8") as jf:
        json.dump(structured_data, jf, indent=2)
    print(f"Saved reconstruction JSON to {json_file}")
