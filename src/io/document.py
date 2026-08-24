from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


def extract_document_text(
    path: str | Path,
    start_page: int | None = None,
    end_page: int | None = None,
) -> str:
    """
    Extract text from a PDF or plain text file.
    For PDFs, start_page/end_page are 1-based inclusive; if both None, all pages.
    """
    path = Path(path)
    path_str = str(path)

    if path_str.lower().endswith(".pdf"):
        reader = PdfReader(path_str)
        total_pages = len(reader.pages)
        if start_page is not None and end_page is not None:
            if start_page < 1 or end_page > total_pages:
                raise ValueError(
                    f"Page range must be between 1 and {total_pages}"
                )
            pages = range(start_page - 1, end_page)
        else:
            pages = range(total_pages)
        text = ""
        for i in pages:
            text += reader.pages[i].extract_text() or ""
        return text

    if path_str.lower().endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    raise ValueError("Unsupported file type. Use .pdf or .txt.")
