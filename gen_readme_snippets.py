import json
import re
from pathlib import Path
from collections import defaultdict

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

def body_to_str(body):
    # VS Code snippet body can be a string or list of strings
    if isinstance(body, list):
        return "\n".join(body)
    return str(body)

def compact_for_table(s: str) -> str:
    # Make multiline bodies table-friendly
    s = s.strip()
    s = s.replace("\n", r"\n")
    s = re.sub(r"\s+", " ", s)
    return s

def esc_cell(s: str) -> str:
    return s.replace("|", r"\|").strip()

def load_snippets():
    data = json.loads(SNIPPETS_PATH.read_text(encoding="utf-8"))
    groups = defaultdict(list)

    for name, snip in data.items():
        prefix = snip.get("prefix", "")
        desc = snip.get("description", "") or str(name)
        cat = snip.get("category", "Uncategorized")
        body = body_to_str(snip.get("body", ""))

        groups[cat].append({
            "prefix": str(prefix),
            "desc": str(desc),
            "body": body
        })

    # sort within category by prefix
    for cat in groups:
        groups[cat].sort(key=lambda x: (len(x["prefix"]), x["prefix"]))

    return groups

def make_md(groups):
    out = []
    used = set()

    for cat in CATEGORY_ORDER:
        if cat not in groups:
            continue
        used.add(cat)

        out.append(f"## {cat}\n")
        out.append("| Prefix | Expands to | What it is |")
        out.append("|------|-----------|-----------|")

        for s in groups[cat]:
            exp = compact_for_table(s["body"])
            out.append(
                f"| `{esc_cell(s['prefix'])}` | `{esc_cell(exp)}` | {esc_cell(s['desc'])} |"
            )
        out.append("")

    # Anything uncategorized (or category typos)
    leftovers = [c for c in groups.keys() if c not in used]
    if leftovers:
        out.append("## Uncategorized\n")
        out.append("| Prefix | Expands to | What it is |")
        out.append("|------|-----------|-----------|")
        for cat in sorted(leftovers):
            for s in groups[cat]:
                exp = compact_for_table(s["body"])
                out.append(
                    f"| `{esc_cell(s['prefix'])}` | `{esc_cell(exp)}` | {esc_cell(s['desc'])} |"
                )
        out.append("")

    return "\n".join(out).strip() + "\n"

def replace_block(readme_text: str, new_block: str) -> str:
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), flags=re.S)
    if not pattern.search(readme_text):
        raise SystemExit(f"README missing markers:\n{START}\n{END}")
    return pattern.sub(f"{START}\n\n{new_block}\n{END}", readme_text, count=1)

def main():
    groups = load_snippets()
    md = make_md(groups)

    readme = README_PATH.read_text(encoding="utf-8")
    updated = replace_block(readme, md)
    README_PATH.write_text(updated, encoding="utf-8")
    print("✅ README updated from latex.json")

if __name__ == "__main__":
    main()
