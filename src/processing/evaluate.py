from __future__ import annotations

import json
import re
from typing import Any

EVALUATE_JSON_PATTERN = r"BEGIN_EVALUATION_JSON\s*(\{.*?\})\s*END_EVALUATION_JSON"


def build_evaluate_prompt(claims: list[Any]) -> str:
    claims_text = json.dumps(claims, indent=2)
    return f"""
You are performing a strict external scientific evaluation.

Input:
A list of author claims extracted from a text.

Your task:
For EACH claim:
- Evaluate alignment with mainstream scientific consensus.
- Use only:
    Supported
    Partially supported
    Contested
    Speculative
    Contradicted
- If classification is Contradicted, explain precisely what established framework it conflicts with.
- Do not generalize.
- Do not restate the claim.
- Be technically specific.
- No vague statements.

Return structured JSON between:

BEGIN_EVALUATION_JSON
{{ 
  "evaluations": [
    {{
      "claim": "...",
      "alignment": "...",
      "explanation": "..."
    }}
  ]
}}
END_EVALUATION_JSON

Claims:
{claims_text}
"""


def parse_evaluate_response(full_output: str) -> dict[str, Any]:
    match = re.search(EVALUATE_JSON_PATTERN, full_output, re.DOTALL)
    if not match:
        raise ValueError("No evaluation JSON block found in model output.")
    return json.loads(match.group(1))
