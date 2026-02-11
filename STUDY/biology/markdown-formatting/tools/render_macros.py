#!/usr/bin/env python3
"""
Macro → Styled Markdown renderer for VS Code preview/export.

You write macros in your master notes, like:
  \vocab{term}
  \proc{process name}
  \eq{p^2 + 2pq + q^2 = 1}
  \ex{example sentence}
  \warn{watch out}
  \ced{7.10.C.2}
  \os{18.2}
  \osref{18.2}{Figure 18.14}
  \defn{term}{definition}

And this script generates a *.rendered.md where those become HTML elements with classes
that your CSS can style.

Supported 1-arg macros:
  \vocab{...}  -> <span class="vocab">...</span>
  \proc{...}   -> <span class="proc">...</span>
  \ex{...}     -> <span class="ex">...</span>
  \warn{...}   -> <span class="warn">...</span>
  \ced{...}    -> <span class="ced">...</span>
  \os{...}     -> <span class="os">OpenStax ...</span> (auto-prefix if you wrote just "18.2")
  \src{...}    -> <span class="src">...</span>
  \q{...}      -> <span class="q">...</span>
  \eq{...}     -> <span class="eq">$...$</span> (auto-wrap in $ $ unless already wrapped)

Supported 2-arg macros:
  \defn{term}{definition}     -> <div class="defn-block">...</div>
  \tag{kind}{text}            -> <span class="tag kind">text</span>
  \osref{18.2}{Figure 18.14}  -> OpenStax ref chip
  \figref{18.2}{18.14}        -> OpenStax ref chip ("Figure 18.14" auto)

Block environments:
  \begin{notes} ... \end{notes}     -> <div class="notes"> ... </div>
  \begin{osblock} ... \end{osblock} -> <div class="osblock"> ... </div>

Nested braces inside arguments are supported.
"""

from __future__ import annotations
import argparse
from pathlib import Path
import re
from typing import Optional, Tuple

# ---------- helpers: balanced-brace parsing ----------

def find_balanced_braces(text: str, start_idx: int) -> Optional[Tuple[str, int]]:
    """Given index pointing at '{', return (content, end_idx_after_closing_brace). Supports nesting."""
    if start_idx >= len(text) or text[start_idx] != "{":
        return None
    depth = 1
    i = start_idx + 1
    buf = []
    while i < len(text):
        ch = text[i]
        if ch == "{":
            depth += 1
            buf.append(ch)
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return ("".join(buf), i + 1)
            buf.append(ch)
        else:
            buf.append(ch)
        i += 1
    return None

def skip_ws(s: str, i: int) -> int:
    while i < len(s) and s[i] in (" ", "\t"):
        i += 1
    return i

# ---------- macro sets ----------

ONE_ARG = {"vocab", "proc", "ex", "warn", "ced", "os", "src", "q", "eq"}
TWO_ARG = {"defn", "tag", "osref", "figref"}

ENV_MAP = {
    "notes": ("<div class=\"notes\">", "</div>"),
    "osblock": ("<div class=\"osblock\">", "</div>"),
}

def needs_dollar_wrap(eq_content: str) -> bool:
    """Wrap in $...$ unless it already looks like math."""
    c = eq_content.strip()
    if not c:
        return False
    if c.startswith("$") and c.endswith("$"):
        return False
    if c.startswith("\\(") and c.endswith("\\)"):
        return False
    if c.startswith("\\[") and c.endswith("\\]"):
        return False
    return True

def render_one_arg(name: str, content: str) -> str:
    content = content.strip()

    if name == "eq":
        if needs_dollar_wrap(content):
            content = f"${content}$"
        return f'<span class="eq">{content}</span>'

    if name == "os":
        # normalize: \os{18.2} -> "OpenStax 18.2"
        label = content
        if re.match(r"^\d+(\.\d+)*$", content):
            label = f"OpenStax {content}"
        return f'<span class="os">{label}</span>'

    return f'<span class="{name}">{content}</span>'

def render_two_arg(name: str, a: str, b: str) -> str:
    a = a.strip()
    b = b.strip()

    if name == "defn":
        # definition block: term highlighted + "= definition"
        return (
            '<div class="defn-block">'
            f'<span class="vocab">{a}</span>'
            f'<span class="defn-eq"> = </span>'
            f'<span class="defn-text">{b}</span>'
            '</div>'
        )

    if name == "tag":
        # tag{kind}{text} -> <span class="tag kind">text</span>
        kind = re.sub(r"[^A-Za-z0-9_-]+", "", a) or "tag"
        return f'<span class="tag {kind}">{b}</span>'

    if name == "osref":
        # osref{18.2}{Figure 18.14} -> chips: OpenStax 18.2 + Figure 18.14
        sec = a
        if re.match(r"^\d+(\.\d+)*$", sec):
            sec = f"OpenStax {sec}"
        return (
            '<span class="osref">'
            f'<span class="os">{sec}</span>'
            f'<span class="osref-sep"> · </span>'
            f'<span class="osref-item">{b}</span>'
            '</span>'
        )

    if name == "figref":
        # figref{18.2}{18.14} -> "OpenStax 18.2 · Figure 18.14"
        sec = a
        fig = b
        if re.match(r"^\d+(\.\d+)*$", sec):
            sec = f"OpenStax {sec}"
        if re.match(r"^\d+(\.\d+)*$", fig):
            fig = f"Figure {fig}"
        return (
            '<span class="osref">'
            f'<span class="os">{sec}</span>'
            f'<span class="osref-sep"> · </span>'
            f'<span class="osref-item">{fig}</span>'
            '</span>'
        )

    # fallback: leave untouched if something unexpected happens
    return f'\\{name}{{{a}}}{{{b}}}'

def render(md: str) -> str:
    out = []
    i = 0
    while i < len(md):
        # environments
        if md.startswith("\\begin{", i):
            b = find_balanced_braces(md, i + len("\\begin"))
            if b:
                env_name, end_i = b
                env_name = env_name.strip()
                if env_name in ENV_MAP:
                    out.append(ENV_MAP[env_name][0])
                    i = end_i
                    continue

        if md.startswith("\\end{", i):
            b = find_balanced_braces(md, i + len("\\end"))
            if b:
                env_name, end_i = b
                env_name = env_name.strip()
                if env_name in ENV_MAP:
                    out.append(ENV_MAP[env_name][1])
                    i = end_i
                    continue

        # macros
        if md[i] == "\\":
            m = re.match(r"\\([A-Za-z]+)", md[i:])
            if m:
                name = m.group(1)
                j = i + 1 + len(name)
                j = skip_ws(md, j)

                # 2-arg macros
                if name in TWO_ARG and j < len(md) and md[j] == "{":
                    arg1 = find_balanced_braces(md, j)
                    if arg1:
                        a1, k = arg1
                        k = skip_ws(md, k)
                        if k < len(md) and md[k] == "{":
                            arg2 = find_balanced_braces(md, k)
                            if arg2:
                                a2, end_i = arg2
                                out.append(render_two_arg(name, a1, a2))
                                i = end_i
                                continue

                # 1-arg macros
                if name in ONE_ARG and j < len(md) and md[j] == "{":
                    arg = find_balanced_braces(md, j)
                    if arg:
                        content, end_i = arg
                        out.append(render_one_arg(name, content))
                        i = end_i
                        continue

        out.append(md[i])
        i += 1

    return "".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Path to source .md file (macro version)")
    ap.add_argument("-o", "--output", help="Output path (.rendered.md). Default: <input>.rendered.md")
    args = ap.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        raise SystemExit(f"Input file not found: {in_path}")

    out_path = Path(args.output) if args.output else in_path.with_suffix(".rendered.md")

    src = in_path.read_text(encoding="utf-8")
    rendered = render(src)

    banner = (
        "<!-- AUTO-GENERATED FILE. DO NOT EDIT DIRECTLY.\n"
        f"     Source: {in_path.name}\n"
        "     Generated by tools/render_macros.py -->\n\n"
    )
    out_path.write_text(banner + rendered, encoding="utf-8")
    print(f"Wrote: {out_path}")

if __name__ == "__main__":
    main()
