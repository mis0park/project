#!/usr/bin/env python3
"""
Generate README snippet tables from VS Code snippets in latex.json.

- Reads:  latex.json (VS Code snippet format)
- Writes: README.md
- Replaces only the block between:
    <!-- SNIPPETS:START -->
    <!-- SNIPPETS:END -->

Fixes the common Windows regex issue where LaTeX backslashes (e.g. \cfrac)
break re.sub replacement strings by using a FUNCTION replacement.
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


def load_snippets() -> dict[str, list[dict[str, str]]]:
    if not SNIPPETS_PATH.exists():
        raise SystemExit(f"Missing snippets file: {SNIPPETS_PATH.resolve()}")

    data = json.loads(SNIPPETS_PATH.read_text(encoding="utf-8"))
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)

    for name, snip in data.items():
        prefix = str(snip.get("prefix", "")).strip()
        desc = (snip.get("description") or str(name)).strip()
        cat = str(snip.get("category", "Uncategorized")).strip()
        body = body_to_str(snip.get("body", ""))

        if not prefix:
            # skip malformed snippets with no prefix
            continue

        groups[cat].append(
            {"prefix": prefix, "desc": desc, "body": body}
        )

    # sort within each category by prefix length then alphabetically
    for cat in list(groups.keys()):
        groups[cat].sort(key=lambda x: (len(x["prefix"]), x["prefix"]))

    return groups


def make_md(groups: dict[str, list[dict[str, str]]]) -> str:
    out: list[str] = []
    used: set[str] = set()

    def emit_category(cat: str, items: list[dict[str, str]]) -> None:
        out.append(f"## {cat}\n")
        out.append("| Prefix | Expands to | What it is |")
        out.append("|------|-----------|-----------|")
        for s in items:
            exp = compact_for_table(s["body"])
            out.append(
                f"| `{esc_cell(s['prefix'])}` | `{esc_cell(exp)}` | {esc_cell(s['desc'])} |"
            )
        out.append("")

    # ordered categories first
    for cat in CATEGORY_ORDER:
        if cat in groups and groups[cat]:
            emit_category(cat, groups[cat])
            used.add(cat)

    # anything else (typos/new categories)
    leftovers = [c for c in groups.keys() if c not in used]
    if leftovers:
        emit_category("Uncategorized", [s for c in sorted(leftovers) for s in groups[c]])

    return "\n".join(out).strip() + "\n"


def replace_block(readme_text: str, new_block: str) -> str:
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), flags=re.S)
    if not pattern.search(readme_text):
        raise SystemExit(
            f"README missing markers:\n{START}\n{END}\n\n"
            "Add them where you want the generated tables to appear."
        )

    # CRITICAL FIX:
    # Use a function replacement so LaTeX backslashes (e.g. \cfrac, \begin) are inserted literally.
    return pattern.sub(lambda _m: f"{START}\n\n{new_block}\n{END}", readme_text, count=1)


def main() -> None:
    if not README_PATH.exists():
        raise SystemExit(f"Missing README file: {README_PATH.resolve()}")

    groups = load_snippets()
    md = make_md(groups)

    readme = README_PATH.read_text(encoding="utf-8")
    updated = replace_block(readme, md)
    README_PATH.write_text(updated, encoding="utf-8")

    print(f"✅ README updated from {SNIPPETS_PATH.name}")


if __name__ == "__main__":
    main()
