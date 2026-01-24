#!/usr/bin/env python3
"""
Generate README snippet tables from VS Code snippets in latex.json.

- Reads:  latex.json (VS Code snippet format)
- Writes: README.md
- Replaces only the block between:
    <!-- SNIPPETS:START -->
    <!-- SNIPPETS:END -->

Preserves:
- CATEGORY_ORDER for category sections
- Original latex.json order *within each category*

Fixes Windows regex replacement issues with LaTeX backslashes by using a
FUNCTION replacement for re.sub.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

SNIPPETS_PATH = Path("latex.json")
README_PATH = Path("README.md")

START = "<!-- SNIPPETS:START -->"
END = "<!-- SNIPPETS:END -->"

CATEGORY_ORDER = [
    "Expressions",
    "Environments",
    "Formatting",
    "Vectors",
    "Units",
    "Symbols",
    "Diagrams",
]


def body_to_str(body: Any) -> str:
    """VS Code snippet body can be a string or list of strings."""
    if isinstance(body, list):
        return "\n".join(str(x) for x in body)
    return str(body)


def compact_for_table(s: str) -> str:
    """Make snippet bodies table-friendly (single line) while keeping \\n visible."""
    s = s.strip()
    s = s.replace("\n", r"\n")
    s = re.sub(r"\s+", " ", s)
    return s


def esc_cell(s: str) -> str:
    """Escape characters that break Markdown tables."""
    return s.replace("|", r"\|").strip()


def load_snippets() -> tuple[dict[str, list[dict[str, str]]], list[str]]:
    """
    Returns:
      - groups: category -> list of snippets (in the same order as latex.json)
      - category_seen_order: categories in the order they first appear in latex.json
    """
    if not SNIPPETS_PATH.exists():
        raise SystemExit(f"Missing snippets file: {SNIPPETS_PATH.resolve()}")

    data = json.loads(SNIPPETS_PATH.read_text(encoding="utf-8"))

    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    category_seen_order: list[str] = []
    seen = set()

    # IMPORTANT: dict iteration preserves JSON order (Python 3.7+)
    for name, snip in data.items():
        prefix = str(snip.get("prefix", "")).strip()
        desc = (snip.get("description") or str(name)).strip()
        cat = str(snip.get("category", "Uncategorized")).strip()
        body = body_to_str(snip.get("body", ""))

        if not prefix:
            continue

        if cat not in seen:
            seen.add(cat)
            category_seen_order.append(cat)

        groups[cat].append({"prefix": prefix, "desc": desc, "body": body})

    # NO SORTING — preserves latex.json order within each category
    return groups, category_seen_order


def make_md(groups: dict[str, list[dict[str, str]]], category_seen_order: list[str]) -> str:
    out: list[str] = []
    used: set[str] = set()

    def emit_category(cat: str, items: list[dict[str, str]]) -> None:
        out.append(f"## {cat}\n")
        out.append("| Prefix | Expands to | What it is |")
        out.append("|------|-----------|-----------|")
        for s in items:
            exp = compact_for_table(s["body"])
            out.append(f"| `{esc_cell(s['prefix'])}` | `{esc_cell(exp)}` | {esc_cell(s['desc'])} |")
        out.append("")

    # 1) Emit categories in your preferred order first
    for cat in CATEGORY_ORDER:
        if cat in groups and groups[cat]:
            emit_category(cat, groups[cat])
            used.add(cat)

    # 2) Emit any remaining categories (typos/new categories) in the order they appear in latex.json
    leftovers = [c for c in category_seen_order if c not in used]
    if leftovers:
        emit_category("Uncategorized", [s for c in leftovers for s in groups[c]])

    return "\n".join(out).strip() + "\n"


def replace_block(readme_text: str, new_block: str) -> str:
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), flags=re.S)
    if not pattern.search(readme_text):
        raise SystemExit(
            f"README missing markers:\n{START}\n{END}\n\n"
            "Add them where you want the generated tables to appear."
        )

    # Use a function replacement so LaTeX backslashes are inserted literally.
    return pattern.sub(lambda _m: f"{START}\n\n{new_block}\n{END}", readme_text, count=1)


def main() -> None:
    if not README_PATH.exists():
        raise SystemExit(f"Missing README file: {README_PATH.resolve()}")

    groups, category_seen_order = load_snippets()
    md = make_md(groups, category_seen_order)

    readme = README_PATH.read_text(encoding="utf-8")
    updated = replace_block(readme, md)
    README_PATH.write_text(updated, encoding="utf-8")

    print(f"✅ README updated from {SNIPPETS_PATH.name}")


if __name__ == "__main__":
    main()
