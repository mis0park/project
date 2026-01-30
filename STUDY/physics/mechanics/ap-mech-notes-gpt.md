
# UNIT 1 
> **Philosophy:** Unit 1 is conceptually light. Memorize the formulas, internalize the phrases, and move on. Most AP mistakes here are *signs, graphs, or language*, not math.

---

### Core Definitions
| Term             | Definition                                    |
|------------------|-----------------------------------------------|
| **Displacement** | change in position (vector)                   |
| **Velocity**     | rate of change of position                    |  
|                  | $\triangleright \ \boxed{v = \dfrac{dx}{dt}}$ |
| **Acceleration** | rate of change of velocity                    |
|                  | $\triangleright \ \boxed{a = \dfrac{dv}{dt}}$ |

> *Velocity is the slope of the position–time graph; acceleration is the slope of the velocity–time graph.*

---

### Constant-Acceleration Formula Sheet (1D)

- These apply **only when acceleration is constant**.
  - $\; v = v_0 + at$
  - $\; x = x_0 + v_0 t + \frac{1}{2} a t^2$
  - $\; v^2 = v_0^2 + 2a(x - x_0)$
  - $\; x - x_0 = \frac{1}{2} (v + v_0)t$

---

### Graph Relationships

- $x$-$t$ graph
  - slope → $v$
  - concavity → sign of $a$

- $v$–$t$ graph  
  - slope → $a$
  - area → $\Delta x$ (distance traveled)

- $a$–$t$ graph  
  - area → $\Delta v$ 

Key phrase:
> *Slope gives the rate of change; area gives the accumulated change.*

---

### Motion Diagrams (equal time intervals)

```text
Speeding up:
•  •   •     •        •
Constant speed:
•   •   •   •   •
Slowing down:
•        •     •   •  •
```

Interpretation rules:
- Increasing spacing → speed increasing
- Constant spacing → constant velocity
- Decreasing spacing → speed decreasing
- Acceleration points toward the **change** in velocity

---

### Projectile Motion (no air resistance)

Horizontal:
$$
a_x = 0,\quad v_x = v_{0x},\quad x = x_0 + v_{0x}t
$$

Vertical:
$$
a_y = -g,\quad v_y = v_{0y} - gt
$$
$$
y = y_0 + v_{0y}t - \tfrac12 gt^2
$$

Key phrases:
- *Horizontal and vertical motions are ***independent***.*
- ***Time is shared*** *between $x$ and $y$.*

---

### Relative Motion (vectors)

$$
\vec{v}_{A/G} = \vec{v}_{A/B} + \vec{v}_{B/G}
$$

Used for:
- boat + current
- plane + wind
- walking inside a moving vehicle

---

### Unit 1 Common Traps (AP loves these)

- Distance vs displacement
- Negative velocity ≠ slowing down
- Forgetting to define axes
- Using kinematic equations when $a$ is not constant
- Mixing slope and area on graphs

---

## UNIT 2 — DYNAMICS (Newton’s Laws, Forces, Diagrams)

> Every problem reduces to:
> **FBD → $\sum F = ma$ → solve components**

---

## Newton’s Laws

### Newton’s First Law
> The net force on a system is the vector sum of all forces exerted on the system.

$\; \boxed{\sum{\vec{F}_i}= 0 \implies \vec{a} = 0}$

**Translational Equilibrium**: configuration of forces such that the net force exerted on a system is zero

$\; \sum \vec{F} = 0 \implies v = \textup{constant}$

- If forces are balanced in some dimensions and not balanced in others, velocity will remain constant only in the dimension that force is balanced and change in the direction of the unbalanced force. 

**Inertial reference frame**: observer would verify Newton's First Law () 

---

### Newton’s Second Law
$$
\sum \vec{F} = m\vec{a}
$$

Component form:
$$
\sum F_x = ma_x,\qquad \sum F_y = ma_y
$$

Key phrase:
> *Acceleration is caused by the net force, not by individual forces.*

---

### Newton’s Third Law
$$
\vec{F}_{A\text{ on }B} = -\vec{F}_{B\text{ on }A}
$$

Rules:
- Forces act on **different objects**
- Action–reaction pairs never cancel on one FBD

---

## Free-Body Diagrams (FBDs)

### Absolute rules
- Draw **only forces acting on the object**
- Do **not** draw forces the object exerts
- Do **not** draw $ma$ as a force
- Choose axes *before* writing equations

---

### Common Forces (know direction + equation)

**Gravity**
$$
\vec{F}_g = m\vec{g}
$$

**Normal force**
- Perpendicular to surface
- Adjusts itself; not always $mg$

**Tension**
- Along rope/string
- Same magnitude in ideal rope

**Friction**
$$
f_k = \mu_k N
$$
$$
f_s \le \mu_s N
$$

Rule:
> Static friction matches the needed force **up to** its maximum.

**Spring force**
$$
\vec{F}_s = -k\Delta \vec{x}
$$

---

## System vs Object Choice (huge AP skill)

- Choose **system** when you want acceleration
- Choose **individual object** when you want internal forces (tension, contact)

Internal forces cancel in system equations.

---

## Inclines (always decompose $mg$)

$$
mg_\parallel = mg\sin\theta
$$
$$
mg_\perp = mg\cos\theta
$$

Normal force (no vertical acceleration):
$$
N = mg\cos\theta
$$

---

## Apparent Weight (elevators)

$$
\sum F = N - mg = ma
$$

Interpretation:
- Accelerating up → $N > mg$
- Accelerating down → $N < mg$
- Free fall → $N = 0$

---

## Circular Motion (not a new force!)

Centripetal acceleration:
$$
a_c = \frac{v^2}{r}
$$

Radial Newton’s Second Law:
$$
\sum F_{\text{radial}} = m\frac{v^2}{r}
$$

Key phrase:
> *Centripetal force is the net inward force.*

---

## Vertical Circles (classic AP problem)

Top of loop (minimum speed, $N=0$):
$$
mg = m\frac{v^2}{r}
$$
$$
v_{\min} = \sqrt{gr}
$$

---

## Drag and Terminal Speed

Linear drag model:
$$
\vec{F}_r = -k\vec{v}
$$

Terminal speed:
$$
mg = kv_t \Rightarrow v_t = \frac{mg}{k}
$$

---

## 3.1 Translational Kinetic Energy

### What kinetic energy *means*

Kinetic energy measures how much **motion** an object has (not how fast it is changing).
It depends only on ***mass*** and ***speed***, not direction.

$$
\boxed{K = \frac{1}{2}mv^2}
$$

Key properties:
- Scalar quantity
- Always nonnegative
- Depends on the **reference frame**

> If two observers measure different speeds, they measure different kinetic energies.

### Why the $v^2$ matters
Relationship between speed & KE
- doubling speed → **four times** the kinetic energy.  
    ⇒ This is why stopping distance grows so fast with speed.

---

## 3.2 Work

### Key Ideas

<*> Work is **the amount of energy transfer (into or out of a system) by a force exerted (on that system) over a distance**.

Only the component of force **parallel** to motion transfers energy(does work).
- Interpretation:
  - Parallel force → positive work
  - Opposite force → negative work
  - Perpendicular force → zero work

⚠ Normal force and centripetal force often do **zero work**, but can **change direction**.

### Properties of Work (⌗ 3.2.A.2) 
- Work is a scalar property
- units are $\text{N・m} = \textup{J (Joules)} = \text{kg・m}^2\text{/s}^2$

### Conservative vs. Nonconservative Force (⌗ 3.2.A.1)

Work done by a **conservative force** on a system:
- path-independent; only depends on the initial/final configuration of the system.
- if the system returns to original configuration
    - $\Delta \textup{PE} = W_{\textup{total}} = 0$
- potential energies can be associated

Work done by a **nonconservative force** on a system:
- path-dependent
- x associate with potential energies
  - ex) friction, air resistance
  - (⌗ 3.2.A.4.iii) The energy dissipated by friction is typically equated to the force of friction times the length of the path over which the force is exerted.
    $$\Delta E_{\text{mech}}=F_f d\cos\theta$$


|      | conservative              | nonconservative                 |
|------|---------------------------|---------------------------------|
|path  | independent               | dependent                       |
| PE?  | associated                | not associated                  |
| ex)  | gravitational, magnetic, spring, electric force | friction, air resistance |

### Calculating Work (⌗ 3.2.A.3)

The work done on an object by a **variable** force:
$$\boxed{W=\int_{a}^{b}\vec{F}(r)\cdot d\vec{r}}$$
-> Integral is taken over the path from point $a$ to point $b$. 

If a component of force parallel to displacement is **constant**:
$$\boxed{W=F_{\parallel}d=Fd\cos\theta}$$
-> parallel $\implies \cos{\theta} = 1$

Even if force is **perpendicular** to the direction of the displacement of the system's center of mass, it **can change the direction** of the system's motion **without changing the kinetic energy**. 

(⌗ 3.2.A.5)
Work is equal to the area under the curve of a graph of $F_{\parallel}$ as a function of displacement. 

<+> Calculating Dot Product:
  $$
  \vec{A}\cdot\vec{B}=AB\cos\theta
  $$

---

### Work–Energy Theorem (⌗ 3.2.A.4)

<*> The **work-energy theorem** states that the change in an object's kinetic energy is equal to the sum of work(net work) being done by all forces exterted on the object. 
$$
\Delta K=\sum_i W_i=\sum_i F_{\parallel,i}\,d_i
$$
-> $F_{\parallel,i}$ = component of the external force parallel to the displacement
-> $d_i$ = displacement of the point of application of the force

> Force cause acceleration. 
- > Acceleration changes velocity.
- > Change in velocity changes KE. 

> When a net force acts through a displacement, it does work. 
- > This work changes the object's KE. 

> Forces change kinetic energy by doing work.

This is Newton’s Second Law rewritten in energy language.
---

(⌗ 3.2.A.4.ii) \ 
[systems center of mass] & [point of application of F] move the same distance \
-> system may be modeled as an object \
-> only the system's KE can change

---

## 3.3 Potential Energy

### Conservative vs nonconservative forces

**Conservative forces**
- Path-independent work
- Can define a potential energy
- Examples: gravity, spring force

**Nonconservative forces**
- Path-dependent work
- Convert mechanical energy to thermal/internal energy
- Example: friction

---

### Potential Energy 

(⌗ 3.3.A.1-2) \
A system composed of 2 or more objects has potential energy **if** the objects within that system **only interact with each other through conservative forces**. 
- scalar quantity \
- associated with the position of the object **within the system**.

(⌗ 3.3.A.3) \
The definition of **zero potential energy** for a given system is **a decision made by the observer** considering the situation to simplify or otherwise assist in analysis. 

### Conservative Forces & Potential Energy

(⌗ 3.3.A.4) \
$$
\Delta U=-\int_{a}^{b}\vec{F}_{cf}(r)\cdot d\vec{r}.
$$
-> ΔU = change in PE($U$) \
-> ΔU => opposite sign, same magnitude compared to work(W). 

(⌗ 3.3.A.5)
The coservative forces exerted on a system in a single dimension = $-\{U(x)\}'$
$$
F_x=-\frac{dU(x)}{dx}
$$
-> $F_{\textup{cf}}$ point in the direction of **decreasing** PE(ΔU).

---

### Stable/Unstable Equilibrium & Potential Energy (⌗ 3.3.A.6)

Graphs of $U(x)$ (a system's PE as a function of its position) can be useful in determining physical properties of that system. 

<*> stable equilibrium = a location at which a **small displacement** in an object’s position results in a force exerted on the object _opposite to the direction of the small displacement_, **accelerating the object back toward the equilibrium position**.
- in a given dimension, stable equilibrium exists at locations where the $U(x)$ has a local minimum. (x = position in that dimension)

<*> unstable equilibrium =  a location at which a **small displacement** in an object’s position results in a force exerted on the object _in the same direction as the small displacement_, **accelerating the object away from the equilibrium position**.
- In a given dimension, unstable equilibrium positions occur at locations where the $U(x)$ has a local maximum. (x = position in that dimension)

| | stable equilibrium | unstable equilibrium |
|----|-----|------|
| direction of F compared to displacement | opposite | same |
| accelerating the object [  ] equilibrium position | back towards | away from |
| occur when $U(x)$ has a local | minimum | maximum |

---

### Potential Energy of Common Physical Systems (⌗ 3.3.A.7)

The PE of common physical systems can be described using the physical properties of that system. 

#### Elastic Potential Energy

$$
U_s=\frac{1}{2}k(\Delta x)^2
$$
-> $U_s$ = elastic PE of an ideal spring
-> $\Delta x$ = distance the spring has been stretched/compressed from its equilibrium length

#### Gravitational Potential Energy

The general form for the gravitational PE of a system consisting of 2 approximately spherical distributions of mass (e.g., moons, planets, stars) = 
$$
U_g=-G\frac{m_1m_2}{r}
$$

The gravitational field near the surface of a planet is nearly constant;
$\Delta U_g$ of a system consisting of an object with mass $m$ and gravitational field $g$ when the object is near the surface =  
$$
\Delta U_g=mg\,\Delta y
$$

---

## 3.4 Conservation of Energy

### Mechanical energy

$$
E = K + U
$$

A system may have:
- Only $K$ (single object)
- $K + U$ (interacting objects)

---

### When energy is conserved

If:
- Only conservative forces act
- No external work

Then:

$$
E_i = E_f
$$

Expanded:

$$
K_i + U_i = K_f + U_f
$$

This is the **fastest tool** for many problems.

---

### Including nonconservative work

When friction or external forces act:

$$
E_i + W_{nc} = E_f
$$

For kinetic friction:

$$
W_f = -f_k d = -\mu_k N d
$$

Mechanical energy decreases, but **total energy is still conserved**.

---

### Energy bar charts (conceptual mastery)

Energy bar charts help visualize:
- where energy starts
- where it ends
- how it transfers

AP often tests reasoning *before* equations.

---

## 3.5 Power

### What power measures

Power is the **rate of energy transfer**.

Average power:

$$
P_{\text{avg}} = \frac{\Delta E}{\Delta t} = \frac{W}{\Delta t}
$$

Instantaneous power:

$$
P = \vec{F} \cdot \vec{v}
$$

Key idea:
> Large force does not guarantee large power — speed matters.

---

## Strategy: Energy vs Newton’s Laws

Use **energy** when:
- You want speed at a position
- Forces are complicated but conservative
- Time is irrelevant

Use **Newton’s laws** when:
- You need acceleration or time
- Forces change direction
- Constraints matter

Best students choose the **simpler representation**, not the “stronger” one.

---
