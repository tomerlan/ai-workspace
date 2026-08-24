# scripts/summarize.py

import sys
from pathlib import Path
from datetime import datetime

# Project root on path for src imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import SUMMARIZE_MODEL, SUMMARIZE_PROMPT_VERSION
from src.io import (
    get_openai_client,
    extract_document_text,
    read_jsons_from_globs,
    write_text,
    write_json,
    ensure_directory,
    get_summarize_paths,
)
from src.io.env import get_project_root
from src.processing.summarize import (
    build_summarize_prompt,
    parse_summarize_response,
    build_query_messages,
)


def main() -> None:
    if len(sys.argv) < 2:
        raise ValueError(
            "Usage:\n"
            "  python3 summarize.py <file_path> [start_page] [end_page]\n"
            "  python3 summarize.py query \"your question\""
        )

    if sys.argv[1] == "query":
        _run_query()
        return

    file_path = sys.argv[1]
    start_page = None
    end_page = None
    if len(sys.argv) == 4:
        start_page = int(sys.argv[2])
        end_page = int(sys.argv[3])
    elif len(sys.argv) not in [2, 4]:
        raise ValueError("Provide either no page range or both start and end page.")

    root = get_project_root()
    client = get_openai_client(root)

    document_text = extract_document_text(file_path, start_page, end_page)
    if not document_text.strip():
        raise ValueError("No text extracted from file.")

    prompt = build_summarize_prompt(document_text)
    response = client.chat.completions.create(
        model=SUMMARIZE_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    full_output = response.choices[0].message.content

    print("\n--- RAW OUTPUT ---\n")
    print(full_output)

    markdown_content, structured_data = parse_summarize_response(full_output)

    md_path, json_path, base_name = get_summarize_paths(file_path, start_page, end_page, root)
    ensure_directory(md_path.parent)
    ensure_directory(json_path.parent)

    timestamp = datetime.utcnow().isoformat()
    pages_value = f"{start_page}-{end_page}" if (start_page and end_page) else "full"
    metadata = (
        "---\n"
        f'source_file: "{file_path}"\n'
        f'pages: "{pages_value}"\n'
        f'model: "{SUMMARIZE_MODEL}"\n'
        f'prompt_version: "{SUMMARIZE_PROMPT_VERSION}"\n'
        f'generated_at_utc: "{timestamp}"\n'
        "chunk_type: \"manual_page_range\"\n"
        "---\n\n"
    )
    write_text(md_path, metadata + markdown_content)
    print(f"\nSaved markdown to {md_path}")

    if structured_data:
        structured_data.update({
            "source_file": file_path,
            "pages": pages_value,
            "model": SUMMARIZE_MODEL,
            "prompt_version": SUMMARIZE_PROMPT_VERSION,
            "generated_at_utc": timestamp,
        })
        write_json(json_path, structured_data)
        print(f"Saved structured JSON to {json_path}")
    else:
        print("No structured JSON saved.")


def _run_query() -> None:
    if len(sys.argv) < 3:
        raise ValueError("Provide a query string.")
    user_query = sys.argv[2]

    root = get_project_root()
    memory = read_jsons_from_globs([
        str(root / "outputs" / "json" / "books" / "*.json"),
        str(root / "outputs" / "json" / "papers" / "*.json"),
    ])
    if not memory:
        raise ValueError("No structured JSON files found.")

    client = get_openai_client(root)
    messages = build_query_messages(memory, user_query)
    response = client.chat.completions.create(
        model=SUMMARIZE_MODEL,
        messages=messages,
        temperature=0.2,
    )
    print("\n--- QUERY RESULT ---\n")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
