# scripts/evaluate.py

import sys
from pathlib import Path
from datetime import datetime

# Project root on path for src imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import EVALUATE_DEFAULT_MODEL
from src.io import get_openai_client, read_json, write_json, ensure_directory, get_evaluate_output_path
from src.io.env import get_project_root
from src.processing.evaluate import build_evaluate_prompt, parse_evaluate_response


def main() -> None:
    if len(sys.argv) < 2:
        raise ValueError(
            "Usage:\n"
            "  python3 scripts/evaluate.py <reconstruct_json_file> [--model MODEL]"
        )

    json_path = Path(sys.argv[1])
    model = EVALUATE_DEFAULT_MODEL
    if "--model" in sys.argv:
        i = sys.argv.index("--model")
        if i + 1 < len(sys.argv):
            model = sys.argv[i + 1]

    if not json_path.exists():
        raise ValueError(f"File not found: {json_path}")

    structured_data = read_json(json_path)
    claims = structured_data.get("claims", [])
    if not claims:
        raise ValueError("No claims found in JSON file.")

    root = get_project_root()
    client = get_openai_client(root)

    prompt = build_evaluate_prompt(claims)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
    )
    full_output = response.choices[0].message.content

    print("\n--- RAW EVALUATION OUTPUT ---\n")
    print(full_output)

    evaluation_data = parse_evaluate_response(full_output)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    out_path = get_evaluate_output_path(json_path.stem, timestamp, root)
    ensure_directory(out_path.parent)
    write_json(out_path, evaluation_data)
    print(f"\nSaved evaluation to {out_path}")


if __name__ == "__main__":
    main()
