## Core Math / LaTeX Snippets

| Prefix | Expands to | What it is | Notes |
|------|-----------|-----------|------|
| ff | `\frac{a}{b}` | Fraction | inline |
| ffd | `\dfrac{a}{b}` | Display fraction | larger |
| ffc | `\cfrac{a}{b}` | Continued fraction | nested |
| sum | `\sum_{i=1}^{n}` | Summation | |
| int | `\int_a^b f(x)\,dx` | Integral | includes spacing |

## Display Math Environments

| Prefix | Expands to | Environment | Notes |
|------|-----------|------------|------|
| eq | `equation*` | Unnumbered equation | default |
| eqn | `equation` | Numbered equation | |
| al | `align*` | Unnumbered aligned block | |
| aln | `align` | Numbered align | |
| ald | `aligned` | Embedded alignment | use inside equation |

## Physics / Vector Calculus

| Prefix | Expands to | Command | Notes |
|------|-----------|--------|------|
| dv | `\dv{f}{x}` | Total derivative | physics pkg |
| dv2 | `\dv[2]{f}{x}` | Second derivative | |
| pdv | `\pdv{f}{x}` | Partial derivative | |
| vb | `\vb{v}` | Bold vector | preferred |
| dot | `\vb{A}\cdot\vb{B}` | Dot product | |
| cross | `\vb{A}\times\vb{B}` | Cross product | |

## Units

| Prefix | Expands to | Command | Notes |
|------|-----------|--------|------|
| si | `\SI{9.8}{m/s^2}` | SI quantity | siunitx |

## Diagrams

| Prefix | Expands to | Environment | Notes |
|------|-----------|------------|------|
| tz | `tikzpicture` | TikZ diagram | generic |
| ctz | `circuitikz` | Circuit diagram | E&M |
| fbd | TikZ block | Free-body diagram | mechanics |

## Symbol System

| Prefix | Expands to | Meaning | Notes |
|------|-----------|--------|------|
| sy | `\sym{I}` | Base symbol | links to table |
| ss | `\symsub{I}{avg}` | Subscripted symbol | avg, eq, rms |
| symrow | table row | Anchored symbol row | symbol map |
