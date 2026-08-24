from __future__ import annotations

import json
import re

RECONSTRUCT_JSON_PATTERN = r"BEGIN_STRUCTURED_JSON\s*(\{.*?\})\s*END_STRUCTURED_JSON"


def build_reconstruct_prompt(document_text: str) -> str:
    return f"""
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


def parse_reconstruct_response(full_output: str) -> tuple[str, dict | None]:
    """Returns (markdown_content, structured_data or None)."""
    match = re.search(RECONSTRUCT_JSON_PATTERN, full_output, re.DOTALL)
    structured_data = None
    markdown_content = full_output
    if match:
        structured_data = json.loads(match.group(1))
        markdown_content = re.sub(RECONSTRUCT_JSON_PATTERN, "", full_output, flags=re.DOTALL)
    return markdown_content.strip(), structured_data
