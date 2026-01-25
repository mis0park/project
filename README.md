<!-- SNIPPETS:START -->

## Expressions

| Prefix | Expands to | What it is |
|--------|-------------|-----------|
| `ff`  | `\frac{${1}}{${2}}` | Fraction |
| `ffd` | `\dfrac{${1}}{${2}}` | Display fraction |
| `ffc` | `\cfrac{${1}}{${2}}` | Continued fraction |
| `sum` | `\sum_{${1:i}=1}^{${2:n}}` | Summation |
| `int` | `\int_{${1:a}}^{${2:b}} ${3:f(x)}\,dx` | Integral |
| `dv`  | `\\dv{${1:f}}{${2:x}}` | Total derivative (physics pkg) |
| `dv2` | `\\dv[2]{${1:f}}{${2:x}}` | 2nd total derivative |
| `pdv` | `\\pdv{${1:f}}{${2:x}}` | Partial derivative (physics pkg) |

## Environments

| Prefix | Expands to | What it is |
|------|-----------|-----------|
| `eq` | `\begin{equation*}\n ${1}\n\end{equation*}` | equation* (unnumbered) |
| `eqn` | `\begin{equation}\n ${1}\n\end{equation}` | equation (numbered) |
| `al` | `\begin{align*}\n ${1}\n\end{align*}` | align* (unnumbered) |
| `aln` | `\begin{align}\n ${1}\n\end{align}` | align (numbered) |
| `ald` | `\begin{aligned}\n ${1}\n\end{aligned}` | aligned (use inside equation/equation*) |
| `pf` | `\begin{proof}\n ${1}\n\end{proof}` | Proof environment |
| `thm` | `\begin{theorem}\n ${1}\n\end{theorem}` | Theorem environment |

## Formatting

| Prefix | Expands to | What it is |
|------|-----------|-----------|
| `qty` | `\\qty(${1})` | Auto-sized delimiters (physics pkg) |

## Vectors

| Prefix | Expands to | What it is |
|------|-----------|-----------|
| `vb` | `\\vb{${1:v}}` | Bold vector (physics pkg) |
| `dot` | `${1:\\vb{A}}\\cdot ${2:\\vb{B}}` | Dot product |
| `cross` | `${1:\\vb{A}}\\times ${2:\\vb{B}}` | Cross product |

## Units

| Prefix | Expands to | What it is |
|------|-----------|-----------|
| `si` | `\\SI{${1:9.8}}{${2:m/s^2}}` | SI value + unit (siunitx) |

## Symbols

| Prefix | Expands to | What it is |
|------|-----------|-----------|
| `sy` | `\\sym{${1:I}}` | Linked base symbol (requires \sym macro) |
| `ss` | `\\symsub{${1:I}}{${2:avg}}` | Linked subscripted symbol |
| `symrow` | `${1:Name} & \\hypertarget{sym:${2:I}}{$$${2:I}$$} & ${3:Meaning/definition} & \\si{${4:}} & ${5:Common subscripts: avg, rms, 0, eq} \\` | Adds an anchor so \sym{I} links to it |

## Diagrams

| Prefix | Expands to | What it is |
|------|-----------|-----------|
| `tz` | `\begin{tikzpicture}[>=Latex]\n ${1}\n\end{tikzpicture}` | tikzpicture env |
| `ctz` | `\begin{circuitikz}\n ${1}\n\end{circuitikz}` | circuitikz env |
| `fbd` | `\begin{tikzpicture}[>=Latex]\n \\draw[thick] (-1,0) -- (3,0);\n \\draw[thick] (0,0) rectangle (2,1);\n \\draw[->] (1,1) -- (1,2) node[above] {$N$};\n \\draw[->] (1,0) -- (1,-1) node[below] {$mg$};\n \\draw[->] (2,0.5) -- (3,0.5) node[right] {$F$};\n\end{tikzpicture}` | Quick FBD skeleton |

<!-- SNIPPETS:END -->