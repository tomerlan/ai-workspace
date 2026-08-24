from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


def get_project_root() -> Path:
    """Project root (parent of 'scripts')."""
    return Path(__file__).resolve().parent.parent.parent


def load_env(project_root: Path | None = None) -> None:
    if project_root is None:
        project_root = get_project_root()
    load_dotenv(dotenv_path=project_root / ".env")


def get_openai_client(project_root: Path | None = None) -> OpenAI:
    if project_root is None:
        project_root = get_project_root()
    load_env(project_root)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment.")
    return OpenAI(api_key=api_key)
