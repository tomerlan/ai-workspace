from __future__ import annotations

from pathlib import Path


def _base_name_with_pages(source_path: str | Path, start_page: int | None, end_page: int | None) -> str:
    base = Path(source_path).stem
    if start_page is not None and end_page is not None:
        base = f"{base}_p{start_page}-{end_page}"
    return base


def get_reconstruct_paths(
    source_path: str | Path,
    start_page: int | None,
    end_page: int | None,
    root: str | Path = ".",
) -> tuple[Path, Path, str]:
    """
    Returns (markdown_path, json_path, base_name) for reconstruct outputs.
    Outputs go under outputs/books and outputs/json/books.
    """
    root = Path(root)
    base = _base_name_with_pages(source_path, start_page, end_page)
    base = f"{base}_reconstruct"
    md_path = root / "outputs" / "books" / f"{base}.md"
    json_path = root / "outputs" / "json" / "books" / f"{base}.json"
    return md_path, json_path, base


def get_summarize_paths(
    source_path: str,
    start_page: int | None,
    end_page: int | None,
    root: str | Path = ".",
) -> tuple[Path, Path, str]:
    """
    Returns (markdown_path, json_path, base_name) for summarize outputs.
    Subdir (books/papers) chosen by presence of "data/books" or "data/papers" in source_path.
    """
    root = Path(root)
    base = _base_name_with_pages(source_path, start_page, end_page)
    if "data/books" in source_path:
        out_sub = "books"
        json_sub = "books"
    elif "data/papers" in source_path:
        out_sub = "papers"
        json_sub = "papers"
    else:
        out_sub = ""
        json_sub = ""
    md_path = root / "outputs" / out_sub / f"{base}.md" if out_sub else root / "outputs" / f"{base}.md"
    json_path = root / "outputs" / "json" / json_sub / f"{base}.json" if json_sub else root / "outputs" / "json" / f"{base}.json"
    return md_path, json_path, base


def get_evaluate_output_path(
    json_stem: str,
    timestamp: str,
    root: str | Path = ".",
) -> Path:
    """Output path for evaluation JSON: outputs/evaluations/<stem>_evaluation_<timestamp>.json"""
    root = Path(root)
    return root / "outputs" / "evaluations" / f"{json_stem}_evaluation_{timestamp}.json"
