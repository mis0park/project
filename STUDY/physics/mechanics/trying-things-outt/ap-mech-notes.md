
# UNIT 1 - KINEMATICS (10–15% MC Weighting)



- 1.1 Scalars and Vectors
- 1.2 Displacement, Velocity, and Acceleration
- 1.3 Representing Motion
- 1.4 Reference Frames and Relative Motion
- 1.5 Motion in Two or Three Dimensions
---

## 1.1 Scalars and Vectors
> 1.1.A: Describe a scalar or vector quantity using magnitude and direction,as appropriate. 

### EK 1.1.A.1 Scalar vs. Vector
- **Scalars**: describes magnitude only (time, mass, temperature, energy,...)
- **Vectors**: describes magnitude and **direction** (displacement, velocity, acceleration,...)

### EK 1.1.B Vector Notation & Calculation
- Vectors can be represented using **components** along perpendicular axes.
- Vector addition and subtraction can be performed using component methods.
- **$\vec{A}$** is a vector; **$|\vec{A}|$** is its magnitude.

**2D vector:**
$$
\vec{A} = A_x \hat{i} + A_y \hat{j}
$$
**Magnitude:**
$$
A = \sqrt{A_x^2 + A_y^2}
$$
**Angle with x-axis:**
$$
\tan\theta = \frac{A_y}{A_x}
$$

### Vector addition (component method)
$$
\vec{R} = \vec{A} + \vec{B}
$$
$$
R_x = A_x + B_x \; ,\quad R_y = A_y + B_y
$$

<!----- TikZ: head-to-tail addition of two vectors, show resultant ----->

### Units + dimensional sanity checks
- Always carry units through algebra.
- If you add terms, they must have the same units.

---

# 1.2 Displacement, Velocity, and Acceleration :contentReference[oaicite:5]{index=5}

### Definitions (calc-first, since it’s Physics C)
\[
\Delta x = x_f - x_i
\]
\[
v_{\text{avg}} = \frac{\Delta x}{\Delta t}
\quad,\quad
v(t) = \frac{dx}{dt}
\]
\[
a_{\text{avg}} = \frac{\Delta v}{\Delta t}
\quad,\quad
a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}
\]

### Sign conventions (1D)
- Choose + direction once, then stick to it.
- “Slowing down” ≠ “negative acceleration” (depends on sign of \(v\)). :contentReference[oaicite:6]{index=6}

### Quick interpretation rules
- \(v\) has the sign of the slope of \(x(t)\).
- \(a\) has the sign of the slope of \(v(t)\).

<!----- TikZ: x(t) curve with tangent slope labeled v ----->  
<!----- TikZ: v(t) line with slope labeled a ----->

### Mini example (OpenStax-style)
Given \(x(t)=4t^2-3t+1\):
\[
v(t)=\frac{dx}{dt}=8t-3,\quad a(t)=\frac{dv}{dt}=8
\]
Interpretation: constant positive \(a\) → parabola for \(x(t)\).

---

# 1.3 Representing Motion :contentReference[oaicite:7]{index=7}

> You must be able to translate between: motion map ↔ verbal description ↔ graphs ↔ equations. :contentReference[oaicite:8]{index=8}

### 1D motion maps (dot diagrams)
- Equal spacing → constant velocity
- Increasing spacing → speeding up
- Decreasing spacing → slowing down

<!----- TikZ: motion map constant v (equal dot spacing) ----->  
<!----- TikZ: motion map speeding up (increasing spacing) ----->  
<!----- TikZ: motion map slowing down (decreasing spacing) ----->

### Graph connections (this is exam glue)
1. **Slope rules**
   \[
   \text{slope of }x(t) = v(t)
   \quad,\quad
   \text{slope of }v(t) = a(t)
   \]
2. **Area rules**
   \[
   \Delta x = \int v(t)\,dt
   \quad,\quad
   \Delta v = \int a(t)\,dt
   \]

<!----- TikZ: v(t) vs t with shaded area = displacement ----->  
<!----- TikZ: a(t) vs t with shaded area = change in velocity ----->

### Constant acceleration set (derived from calculus)
If \(a=\text{constant}\):
\[
v = v_0 + at
\]
\[
x = x_0 + v_0 t + \frac12 at^2
\]
\[
v^2 = v_0^2 + 2a(x-x_0)
\]

### Common “representation trap”
If \(v(t)\) is negative, the object can still be **speeding up** if \(a(t)\) is also negative (magnitude of velocity increasing).

---

# 1.4 Reference Frames and Relative Motion

### Learning focus
- 1.4.A: describe a reference frame
- 1.4.B: relate measurements in different inertial frames :contentReference[oaicite:10]{index=10}

### Key essential knowledge (use these as “claims”)
- **1.4.A.1**: measured direction/magnitude depend on chosen frame. :contentReference[oaicite:11]{index=11}  
- **1.4.B.1**: you can convert measurements between frames. :contentReference[oaicite:12]{index=12}  
- **1.4.B.2**: observed velocity combines object velocity + observer’s frame velocity. :contentReference[oaicite:13]{index=13}  
  - **1.4.B.2.i**: do it via vector add/subtract. :contentReference[oaicite:14]{index=14}  
  - **1.4.B.2.ii**: acceleration is the same in all inertial frames. :contentReference[oaicite:15]{index=15}  

### Core equations (1D form)
Let frames \(S\) and \(S'\) with \(S'\) moving at constant \(u\) relative to \(S\):
\[
x = x' + ut
\]
\[
v = v' + u
\]
\[
a = a'
\]

### Diagram intuition
<!----- TikZ: two reference frames S and S' moving relative; show velocity addition arrows ----->

### Boundary statement
Unless stated otherwise, assume the reference frame is inertial. :contentReference[oaicite:16]{index=16}

---

# 1.5 Motion in Two or Three Dimensions :contentReference[oaicite:17]{index=17}

### What the CED wants you to be able to say/do
- **1.5.A.1**: break motion into perpendicular components; use 1D kinematics per axis. :contentReference[oaicite:18]{index=18}  
- **1.5.A.2**: \( \vec{v} \) and \( \vec{a} \) can differ by dimension; can be nonuniform. :contentReference[oaicite:19]{index=19}  
- **1.5.A.3**: changing motion in one dimension doesn’t force change in perpendicular dimension. :contentReference[oaicite:20]{index=20}  
- **1.5.A.4**: projectile motion = \(a_x=0\), \(a_y=-g\) (constant). :contentReference[oaicite:21]{index=21}  

### Vector forms
\[
\vec{r}(t)=x(t)\hat{i}+y(t)\hat{j}
\]
\[
\vec{v}(t)=\frac{d\vec{r}}{dt}=v_x\hat{i}+v_y\hat{j}
\]
\[
\vec{a}(t)=\frac{d\vec{v}}{dt}=a_x\hat{i}+a_y\hat{j}
\]

### Projectile motion (no air resistance)
\[
a_x=0 \Rightarrow v_x = v_{0x},\;\; x = x_0 + v_{0x}t
\]
\[
a_y=-g \Rightarrow v_y = v_{0y}-gt,\;\; y = y_0 + v_{0y}t - \frac12 gt^2
\]

Component setup:
\[
v_{0x}=v_0\cos\theta,\quad v_{0y}=v_0\sin\theta
\]

<!----- TikZ: projectile parabola; show constant vx arrow, changing vy arrow, acceleration downward ----->

### Boundary statement (important)
AP Physics C: Mechanics expects **quantitative** analysis in **two** dimensions; 3D is not required here. :contentReference[oaicite:22]{index=22}

---

## Unit 1 Summary (what you should be able to do fast) :contentReference[oaicite:23]{index=23}

- Convert between **scalars/vectors** and **components** (1.1).
- Use calculus definitions \(v=\frac{dx}{dt}\), \(a=\frac{dv}{dt}\) (1.2).
- Translate **graphs ⇄ equations ⇄ words**; use slope/area meaning (1.3).
- Do **relative velocity** cleanly with frame choice; remember \(a=a'\) for inertial frames (1.4).
- Solve 2D motion by splitting into axes; projectile motion is the flagship case (1.5).

(Next: Unit 2 — Force & Translational Dynamics)
