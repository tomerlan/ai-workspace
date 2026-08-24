from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def read_json(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str | Path, data: dict[str, Any], indent: int = 2) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)


def write_text(path: str | Path, content: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def ensure_directory(path: str | Path) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def read_jsons_from_globs(globs: list[str]) -> list[dict[str, Any]]:
    """Load and return a list of JSON objects from files matching the given glob patterns."""
    import glob as glob_module

    files = []
    for pattern in globs:
        files.extend(glob_module.glob(pattern))
    result = []
    for f in files:
        result.append(read_json(f))
    return result
