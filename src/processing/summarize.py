from __future__ import annotations

import json
import re
from typing import Any


SUMMARIZE_JSON_PATTERN = r"BEGIN_STRUCTURED_JSON\s*(\{.*?\})\s*END_STRUCTURED_JSON"


def build_summarize_prompt(document_text: str) -> str:
    return (
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
        '- claims: [{"claim": "...", "alignment": "..."}]\n'
        '- concepts: [{"term": "...", "definition": "...", "mainstream_status": "..."}]\n'
        "- relationships: [ ... ]\n\n"
        "DOCUMENT:\n"
        + document_text
    )


def parse_summarize_response(full_output: str) -> tuple[str, dict | None]:
    """Returns (markdown_content, structured_data or None)."""
    match = re.search(SUMMARIZE_JSON_PATTERN, full_output, re.DOTALL)
    structured_data = None
    markdown_content = full_output
    if match:
        json_str = match.group(1)
        structured_data = json.loads(json_str)
        markdown_content = re.sub(SUMMARIZE_JSON_PATTERN, "", full_output, flags=re.DOTALL)
    return markdown_content.strip(), structured_data


def build_query_messages(memory_objects: list[dict[str, Any]], user_query: str) -> list[dict[str, str]]:
    """Build chat messages for query mode: system + user with memory and query."""
    memory_text = json.dumps(memory_objects, indent=2)
    return [
        {
            "role": "system",
            "content": "Use only the provided structured memory. Do not hallucinate. If information is absent, state that explicitly.",
        },
        {
            "role": "user",
            "content": (
                "Structured research memory:\n\n"
                + memory_text
                + "\n\nUser query:\n"
                + user_query
                + "\n\nAnswer precisely."
            ),
        },
    ]
