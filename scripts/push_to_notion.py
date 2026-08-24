#!/usr/bin/env python3
"""
Push markdown files to Notion as new pages under a parent page.

Setup (once):
  - .env: NOTION_SECRET=your_integration_secret (from notion.so/my-integrations)
  - In Notion: on each page you want to push to, click "..." → "Add connections" → your integration
  - No need to put any page ID in .env; pass the target page each run.

Install: pip install md2notionpage

Usage (target page = where the new sub-page will appear):
  # One file → one specific Notion page (pass page ID every time):
  python scripts/push_to_notion.py path/to/file.md NOTION_PAGE_ID

  # Same, with flag:
  python scripts/push_to_notion.py --parent-id NOTION_PAGE_ID path/to/file.md

  # Multiple files → same page:
  python scripts/push_to_notion.py --parent-id NOTION_PAGE_ID path/to/dir/
"""

import os
import re
import sys
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

try:
    from md2notionpage import md2notionpage
except ImportError:
    print("Install the Notion upload dependency: pip install md2notionpage", file=sys.stderr)
    sys.exit(1)


# Default: push from outputs/books
DEFAULT_MD_DIR = Path(__file__).resolve().parent.parent / "outputs" / "books"

# Notion page IDs are 32 hex chars, often with dashes (8-4-4-4-12)
NOTION_ID_PATTERN = __import__("re").compile(r"^[a-fA-F0-9\-]{32,36}$")


def collect_md_paths(paths):
    """Return a list of .md file Paths from given path strings (files or dirs)."""
    out = []
    for p in paths:
        path = Path(p).resolve()
        if not path.exists():
            print(f"Skip (not found): {path}", file=sys.stderr)
            continue
        if path.is_file():
            if path.suffix.lower() == ".md":
                out.append(path)
            else:
                print(f"Skip (not .md): {path}", file=sys.stderr)
        else:
            for f in sorted(path.rglob("*.md")):
                if f.is_file():
                    out.append(f)
    return out


def filename_to_title(path: Path) -> str:
    """Derive a readable Notion page title from the markdown filename."""
    name = path.stem
    # e.g. Herrera_Melanin_the_Master_Molecule_p79-123_reconstruct -> same or shortened
    if name.endswith("_reconstruct"):
        name = name[: -len("_reconstruct")]
    return name.replace("_", " ").strip() or path.name


def _normalize_md_for_notion(content: str) -> str:
    """Avoid md2notionpage bugs and preserve claim numbers in Notion."""
    # 1) Remove the *in-text citation markers* used in mainstream_melanin.md (these look terrible in Notion)
    # Examples:   (often repeated back-to-back).
    content = re.sub(r"【\d+†L\d+(?:-L\d+)?】", "", content)

    # 2) Drop md2notionpage placeholders that show up as noisy text
    # Example line:  *Figure: ...*
    content = re.sub(r"^【\d+†embed_image】.*(?:\n|$)", "", content, flags=re.MULTILINE)

    # 3) Clean up any doubled spaces left behind after stripping citation markers
    content = re.sub(r"[ \t]{2,}", " ", content)

    # 4) Numbered list "1. " "2. " -> "**1.** " so numbers show correctly (Notion often shows all as "1.")
    content = re.sub(r"^(\d+)\. ", r"**\1.** ", content, flags=re.MULTILINE)

    # 5) Avoid md2notionpage bug: nested bullets under numbered lists can crash or render weirdly.
    # IMPORTANT: only touch bullets that are nested *under numbered lists* (keep normal nested bullets intact).
    lines = content.splitlines()
    out_lines: list[str] = []
    in_numbered = False
    for ln in lines:
        if not ln.strip():
            in_numbered = False
            out_lines.append(ln)
            continue
        if re.match(r"^\*\*\d+\.\*\*\s+", ln):
            in_numbered = True
            out_lines.append(ln)
            continue
        if in_numbered and re.match(r"^\s+-\s+", ln):
            out_lines.append(re.sub(r"^(\s+)-\s+", r"\1", ln))
            continue
        out_lines.append(ln)

    return "\n".join(out_lines)


def push_one(md_path: Path, parent_page_id: str, dry_run: bool) -> Optional[str]:
    """Read markdown from md_path, push to Notion; return page URL or None."""
    content = md_path.read_text(encoding="utf-8", errors="replace")
    # If this file contains an archived legacy append block, do not push it to Notion.
    legacy_marker = "<!-- LEGACY_APPEND_START"
    if legacy_marker in content:
        content = content.split(legacy_marker, 1)[0].rstrip() + "\n"
    # Skip melanin-specific normalization for circadian docs (avoids empty-page bugs)
    if "circadian" not in md_path.name.lower():
        content = _normalize_md_for_notion(content)
    # Prefer the first H1 in the markdown as the Notion page title.
    # Fallback to a filename-derived title if no H1 exists.
    title = filename_to_title(md_path)
    for ln in content.splitlines():
        m = re.match(r"^#\s+(.+?)\s*$", ln)
        if m:
            title = m.group(1).strip()
            break
    if dry_run:
        print(f"[dry-run] Would push: {md_path} -> title={title!r}")
        return None

    # md2notionpage appends blocks one-by-one, which can time out on large pages.
    # Do the same conversion but append blocks in batches.
    from notion_client import Client
    from notion_client.client import ClientOptions
    import time

    import md2notionpage.core as mdcore

    secret = os.getenv("NOTION_SECRET", "")
    notion = Client(options=ClientOptions(auth=secret, timeout_ms=300_000))

    created_page = notion.pages.create(
        parent={"type": "page_id", "page_id": parent_page_id},
        properties={
            "title": {"title": [{"type": "text", "text": {"content": title}}]}
        },
        children=[],
    )

    blocks = mdcore.parse_md(content)

    # Notion API validates code block languages strictly.
    # Some markdown-to-notion conversions yield "text", which Notion rejects.
    for b in blocks:
        if b.get("type") == "code":
            code = b.get("code") or {}
            lang = code.get("language")
            if lang in (None, "", "text"):
                code["language"] = "plain text"
                b["code"] = code

    def _chunks(xs, n: int):
        for i in range(0, len(xs), n):
            yield xs[i : i + n]

    for chunk in _chunks(blocks, 50):
        # simple retry loop for transient Notion timeouts
        for attempt in range(5):
            try:
                notion.blocks.children.append(created_page["id"], children=chunk)
                break
            except Exception:
                if attempt == 4:
                    raise
                time.sleep(1.5 * (2**attempt))

    return created_page["url"]


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Push markdown files to Notion as new pages.",
        epilog=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=[str(DEFAULT_MD_DIR)],
        help="Markdown file(s) or dir(s); or 'file.md PAGE_ID' to push one file to that page",
    )
    parser.add_argument(
        "--parent-id",
        default=os.getenv("NOTION_PARENT_PAGE_ID"),
        help="Notion page ID (optional; or pass as second arg: file.md PAGE_ID)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only print what would be pushed, do not call Notion",
    )
    args = parser.parse_args()

    # One file + page ID: paths = [file.md, page_id]
    parent_id_override = None
    if len(args.paths) == 2 and NOTION_ID_PATTERN.match(args.paths[1].strip()):
        parent_id_override = args.paths[1].strip()
        args.paths = args.paths[:1]
    if parent_id_override is not None:
        args.parent_id = parent_id_override

    secret = os.getenv("NOTION_SECRET")
    if not secret and not args.dry_run:
        print("Set NOTION_SECRET in .env (Notion integration token).", file=sys.stderr)
        sys.exit(1)
    if not args.parent_id and not args.dry_run:
        print("Pass the Notion page ID: file.md PAGE_ID  or  --parent-id PAGE_ID", file=sys.stderr)
        sys.exit(1)

    md_paths = collect_md_paths(args.paths)
    if not md_paths:
        print("No .md files found.", file=sys.stderr)
        sys.exit(1)

    for md_path in md_paths:
        try:
            url = push_one(md_path, args.parent_id or "", args.dry_run)
            if url:
                print(f"Pushed: {md_path.name} -> {url}")
        except Exception as e:
            print(f"Error pushing {md_path}: {e}", file=sys.stderr)
            if not args.dry_run:
                raise


if __name__ == "__main__":
    main()
