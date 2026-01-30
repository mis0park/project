
# UNIT 1 Kinematics

- TOPIC 1.1 Scalars and Vectors  
- TOPIC 1.2 Displacement, Velocity, and Acceleration 
- TOPIC 1.3 Representing Motion  
- TOPIC 1.4 Reference Frames and Relative Motion  
- TOPIC 1.5 Motion in Two or Three Dimensions  

## TOPIC 1.1 Scalars and Vectors  

> LEARNING OBJECTIVE 1.1.A 
> - Describe a scalar or vector quantity using magnitude and direction, as appropriate. 

### EK 1.1.A.1 Scalar vs. Vector Definition
- **Scalars** are quantities described by *magnitude* only;
- **vectors** are quantities described by both *magnitude and direction*. 

### EK 1.1.A.2 Visual Models of Vectors
Vectors can be visually modeled as arrows with appropriate direction and lengths proportional to their magnitude. 

### EK 1.1.A.3 Examples of Scalar vs. Vector Quantities
**Distance and speed** are examples of scalar quantities, while **position, displacement, velocity, and acceleration** are examples of vector quantities. 

### EK 1.1.A.4 Vector Notation:
Vectors can be expressed in **unit vector notation** or as a **magnitude and a direction**. 
- i) Unit vector notation can be used to represent vectors as the sum of their constituent components in the $x-, y-,$ and $z$-directions, denoted by **$\hat{i}, \hat{j},$** **and** **$\hat{k},$** respectively. \
*Relevant equation:*
$$
\vec{r} = (A\hat{i}+B\hat{j}+C\hat{k})
$$
- ii) The **position vector** of a point is given by $\vec{r}$, and the **unit vector** in the direction of the position vector is 
- iii) A **resultant vector** is the vector sum of the addend vectors’ components. \
*Relevant equations:* 
$$
\vec{C} = \vec{A}+\vec{B} \\
\vec{C}=(A_x+B_x)\hat{i}+(A_y+B_y)\hat{j}
$$

### EK 1.1.A.5 
In a given one-dimensional coordinate system, *opposite* **directions** are denoted by *opposite* **signs**. 

## TOPIC 1.2 Displacement, Velocity, and Acceleration 

> LEARNING OBJECTIVE 1.2.A 
> - Describe a change in an object’s position. 

### EK 1.2.A.1 
When using the object model, the size, shape, and internal configuration are ignored. The object may be treated as a single point with extensive properties such as mass and charge. 

### EK 1.2.A.2 
Displacement is the change in an object’s position. \
*Relevant equation:*
$$
\Delta x=x-x_0
$$

> LEARNING OBJECTIVE 1.2.B 
> - Describe the average velocity and acceleration of an object. 

### EK 1.2.B.1 
Averages of velocity and acceleration are calculated considering the initial and final states of an object over an interval of time. 

### EK 1.2.B.2 
Average velocity is the displacement of an object divided by the interval of time in which that displacement occurs.
$$
\vec{v}_{\text{avg}}=\frac{\Delta \vec{x}}{\Delta t}
$$
### EK 1.2.B.3 
Average acceleration is the change in velocity divided by the interval of time in which that change in velocity occurs.
$$
\vec{a}_{\text{avg}}=\frac{\Delta \vec{v}}{\Delta t}
$$

### EK 1.2.B.4 
An object is accelerating if either the magnitude and/or direction of the object’s velocity are changing.  

### EK 1.2.B.5 
Calculating average velocity or average acceleration over a very small time interval yields a value that is very close to the instantaneous velocity or instantaneous acceleration. 

> LEARNING OBJECTIVE 1.2.C 
> - Describe the instantaneous position, velocity, and acceleration of an object as a function of time. 

### EK 1.2.C.1 
As the time interval used to calculate the average value of a quantity approaches zero, the average value of that quantity approaches the value of the quantity at that instant, called the instantaneous value. 
- i) Instantaneous velocity is the rate of change of the object’s position, which is equal to the derivative of position with respect to time. \
*Relevant equations:*
$$
\vec{v}=\frac{d\vec{r}}{dt}
v_x=\frac{dx}{dt}
$$ 
- ii) Instantaneous acceleration is the rate of change of the object’s velocity, which is equal to the derivative of velocity with respect to time. \
*Relevant equations:*
$$
\vec{a}=\frac{d\vec{v}}{dt}
a_x=\frac{dv_x}{dt}
$$
### EK 1.2.C.2 
Time-dependent functions and instantaneous values of position, velocity, and acceleration can be determined using differentiation and integration. 

## TOPIC 1.3 Representing Motion  

> LEARNING OBJECTIVE 1.3.A 
> - Describe the position, velocity, and acceleration of an object using representations of that object’s motion. 

### EK 1.3.A.1 
Motion can be represented by motion diagrams, figures, graphs, equations, and narrative descriptions. 

### EK 1.3.A.2 
For constant acceleration, three kinematic equations can be used to describe instantaneous linear motion in one dimension: 
$$
v_x=v_{0x}+a_x t
x=x_0+v_{0x}t+\frac{1}{2}a_x t^2
v_x^2=v_{0x}^2+2a_x(x-x_0)
$$\
*Note: The equations above are written to indicate motion in the x-direction, but these equations can be used in any single dimension as appropriate.*

### EK 1.3.A.3 
Near the surface of Earth, the vertical acceleration caused by the force of gravity is downward, constant, and has a measured value approximately equal to
$$
a_g=g\approx 10~\text{m/s}^2
.$$
### EK 1.3.A.4 
Graphs of position, velocity, and acceleration as functions of time can be used to find the relationships between those quantities. 
- i) An object’s instantaneous velocity is the rate of change of the object’s position, which is equal to the slope of a line tangent to a point on a graph of the object’s position as a function of time. \
*Relevant equation:*
$$
v_x=\frac{dx}{dt}
$$
- ii) An object’s instantaneous acceleration is the rate of change of the object’s velocity, which is equal to the slope of a line tangent to a point on a graph of the object’s velocity as a function of time. \
*Relevant equation:*
$$
a_x=\frac{dv_x}{dt}
$$
- iii) The displacement of an object during a time interval is equal to the area under the curve of a graph of the object’s velocity as a function of time (i.e., the area bounded by the function and the horizontal axis for the appropriate interval). \
*Relevant equation:*
$$
\Delta x=\int_{t_1}^{t_2} v_x(t)\,dt
$$
- iv) The change in velocity of an object during a time interval is equal to the area under the curve of a graph of the acceleration of the object as a function of time. \
*Relevant equation:*
$$
\Delta v_x=\int_{t_1}^{t_2} a_x(t)\,dt
$$

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics and AP Physics C: Electricity and Magnetism expects that for all situations in which a numerical quantity is required for $g$, the value $g\approx 10\text{m/s}^2$ will be used. However, students will not be penalized for correctly using the more precise commonly accepted values of $g=9.81\text{m/s}^2$ or $g=9.8\text{m/s}^2$. 

## TOPIC 1.4 Reference Frames and Relative Motion  

> LEARNING OBJECTIVE 1.4.A 
> - Describe the reference frame of a given observer. 

### EK 1.4.A.1 
The choice of reference frame will determine the direction and magnitude of quantities measured by an observer in that reference frame. 

> LEARNING OBJECTIVE 1.4.B 
> - Describe the motion of objects as measured by observers in different inertial reference frames. 

### EK 1.4.B.1 
Measurements from a given reference frame may be converted to measurements from another reference frame. 

### EK 1.4.B.2 
The observed velocity of an object results from the combination of the object’s velocity and the velocity of the observer’s reference frame. 
- i) Combining the motion of an object and the motion of an observer in a given reference frame involves the addition or subtraction of vectors. 
- ii) The acceleration of any object is the same as measured from all inertial reference frames. 

> BOUNDARY STATEMENT 
> - Unless otherwise stated, the frame of reference of any problem may be assumed to be inertial. 

## TOPIC 1.5 Motion in Two or Three Dimensions  

> LEARNING OBJECTIVE 1.5.A 
> - Describe the motion of an object moving in two or three dimensions. 

### EK 1.5.A.1 
Motion in two or three dimensions can be analyzed using one-dimensional kinematic relationships if the motion is separated into components. 

### EK 1.5.A.2 
Velocity and acceleration may be different in each dimension and may be nonuniform. 

### EK 1.5.A.3 
Motion in one dimension may be changed without causing a change in a perpendicular dimension. 

### EK 1.5.A.4 
Projectile motion is a special case of twodimensional motion that has zero acceleration in one dimension and constant, nonzero acceleration in the second dimension. 

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics only expects students to quantitatively analyze the motion of an object in two dimensions. AP Physics C: Electricity and Magnetism expects students to also qualitatively describe the motion of a particle in three dimensions. 

# UNIT 2 Force and Translational Dynamics

- 2.1 Systems and Center of Mass
- 2.2 Force and Free-Body Diagrams
- 2.3 Newton's Third Law
- 2.4 Newton's First Law
- 2.5 Newton's Second Law
- 2.6 Gravitational Force
- 2.7 Kinetic and Static Friction
- 2.8 Spring Forces
- 2.9 Resistive Forces
- 2.10 Circular Motion

## TOPIC 2.1 Systems and Center of Mass  

> LEARNING OBJECTIVE 2.1.A 
> - Describe the properties and interactions of a system. 

### EK 2.1.A.1 
System properties are determined by the interactions between objects within the system. 

### EK 2.1.A.2 
If the properties or interactions of the constituent objects within a system are not important in modeling the behavior of the macroscopic system, the system can itself be treated as a single object. 

### EK 2.1.A.3 
Systems may allow interactions between constituent parts of the system and the environment, which may result in the transfer of energy or mass. 

### EK 2.1.A.4 
Individual objects within a chosen system may behave differently from each other as well as from the system as a whole. 

### EK 2.1.A.5 
The internal structure of a system affects the analysis of that system. 

### EK 2.1.A.6 
As variables external to a system are changed, the system’s substructure may change.  

> LEARNING OBJECTIVE 2.1.B 
> - Describe the location of a system’s center of mass with respect to the system’s constituent parts. 

### EK 2.1.B.1
For objects or systems with symmetrical mass distributions, the center of mass is located on lines of symmetry. 

### EK 2.1.B.2 
The location of a system’s center of mass along a given axis can be calculated using the equation
$$
x_{\text{cm}}=\frac{\sum_i m_i x_i}{\sum_i m_i}
$$
### EK 2.1.B.3 
For a nonuniform solid that can be considered as a collection of differential masses, dm, the solid’s center of mass can be calculated using the equation
$$
\vec{r}_{\text{cm}}=\frac{\int \vec{r}\,dm}{\int dm}
$$
- i) The linear mass density of a rod or other linear rigid body is the derivative of the rod’s mass with respect to the position of the differential mass element on the rigid body. \
*Relevant equation:*
$$
\lambda=\frac{d\,m(\ell)}{d\ell}
$$
- ii) If a function of mass density is given for a solid, the total mass can be determined by integrating the mass density over the length (one dimension), area (two dimensions), or volume (three dimensions) of the solid. For example: 
$$
M_{\text{total}}=\int \rho(\vec{r})\,dV
$$

### EK 2.1.B.4 
A system can be modeled as a singular object that is located at the system’s center of mass. 

## TOPIC 2.2 Forces and Free-Body Diagrams  

> LEARNING OBJECTIVE 2.2.A 
> - Describe a force as an interaction between two objects or systems 

### EK 2.2.A.1 
Forces are vector quantities that describe the interactions between objects or systems. 
- i) A force exerted on an object or system is always due to the interaction of that object or system with another object or system. 
- ii) An object or system cannot exert a net force on itself. 

### EK 2.2.A.2 
Contact forces describe the interaction of an object or system touching another object or system and are macroscopic effects of interatomic electric forces. 

> LEARNING OBJECTIVE 2.2.B 
> - Describe the forces exerted on an object or system using a free-body diagram. 

### EK 2.2.B.1 
Free-body diagrams are useful tools for visualizing forces being exerted on a single object or system and for determining the equations that represent a physical situation. 

### EK 2.2.B.2 
The free-body diagram of an object or system shows each of the forces exerted on the object or system by the environment. 

### EK 2.2.B.3 
Forces exerted on an object or system are represented as vectors originating from the representation of the center of mass, such as a dot. A system is treated as though all of its mass is located at the center of mass.  

### EK 2.2.B.4 
A coordinate system with one axis parallel to the direction of acceleration of the object or system simplifies the translation from freebody diagram to algebraic representation. For example, in a free-body diagram of an object on an inclined plane, it is useful to set one axis parallel to the surface of the incline. 

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics and AP Physics C: Electricity and Magnetism only expect students to depict the forces exerted on objects, not the force components on free-body diagrams. On the AP Physics exams, individual forces represented on a free-body diagram must be drawn as individual straight arrows, originating on the dot and pointing in the direction of the force. Individual forces that are in the same direction must be drawn side by side, not overlapping. 

## TOPIC 2.3 Newton’s Third Law  

> LEARNING OBJECTIVE 2.3.A 
> - Describe the interaction of two objects or systems using Newton’s third law and a representation of paired forces exerted on each object or system. 

### EK 2.3.A.1 
Newton’s third law describes the interaction of two objects or systems in terms of the paired forces that each exerts on the other. 
$$
\vec{F}_{\text{A on B}} = -\vec{F}_{\text{B on A}}
$$
### EK 2.3.A.2 
Interactions between objects within a system (internal forces) do not influence the motion of a system’s center of mass. 

### EK 2.3.A.3 
Tension is the macroscopic net result of forces that infinitesimal segments of a string, cable, chain, or similar system exert on each other in response to an external force. 
- i) An ideal string has negligible mass and does not stretch when under tension. 
- ii) The tension in an ideal string is the same at all points within the string. 
- iii) In a string with nonnegligible mass, tension may not be the same at all points within the string. 
- iv) An ideal pulley is a pulley that has negligible mass and rotates about an axle through its center of mass with negligible friction. 

## TOPIC 2.4 Newton’s First Law  

> LEARNING OBJECTIVE 2.4.A 
> - Describe the conditions under which a system’s velocity remains constant. 

### EK 2.4.A.1 
The net force on a system is the vector sum of all forces exerted on the system. 

### EK 2.4.A.2 
Translational equilibrium is the configuration of forces such that the net force exerted on a system is zero. \
*Derived equation:* 
$$
\sum{\vec{F}_i}=0
$$

### EK 2.4.A.3 
Newton’s first law states that if the net force exerted on a system is zero, the velocity of that system will remain constant. 

### EK 2.4.A.4 
Forces may be balanced in one dimension but unbalanced in another. The system’s velocity will change only in the direction of the unbalanced force. 

### EK 2.4.A.5 
An inertial reference frame is one from which an observer would verify Newton’s first law of motion. 

## TOPIC 2.5 Newton’s Second Law  

> LEARNING OBJECTIVE 2.5.A 
> - Describe the conditions under which a system’s velocity changes. 

### EK 2.5.A.1 
Unbalanced forces are a configuration of forces such that the net force exerted on a system is not equal to zero. 

### EK 2.5.A.2 
Newton’s second law of motion states that the acceleration of a system’s center of mass has a magnitude proportional to the magnitude of the net force exerted on the system and is in the same direction as that net force. \
*Relevant equation:*
$$
\vec{a}_{\text{sys}}=\frac{\sum \vec{F}_{\text{net}}}{m_{\text{sys}}}=\frac{\vec{F}_{\text{net}}}{m_{\text{sys}}}
$$ 

### EK 2.5.A.3 
The velocity of a system’s center of mass will only change if a nonzero net external force is exerted on that system. 

## TOPIC 2.6 Gravitational Force  

> LEARNING OBJECTIVE 2.6.A 
> - Describe the gravitational interaction between two objects or systems with mass. 

### EK 2.6.A.1 
Newton’s law of universal gravitation describes the gravitational force between two objects or systems as directly proportional to each of their masses and inversely proportional to the square of the distance between the systems’ centers of mass. \
*Relevant equation:*
$$
\vec{F}_g=G\frac{m_1 m_2}{r^2}
$$
- i) The gravitational force is attractive. 
- ii) The gravitational force is always exerted along the line connecting the center of mass of the two interacting systems. 
- iii) The gravitational force on a system can be considered to be exerted on the system’s center of mass. 

### EK 2.6.A.2 
A field models the effects of a noncontact force exerted on an object at various positions in space.  
- i) The magnitude of the gravitational field created by a system of mass M at a point in space is equal to the ratio of the gravitational force exerted by the system on a test object of mass m to the mass of the test object. \
*Derived equation:* 
$$
|\vec{g}|=\frac{|\vec{F}_g|}{m}=G\frac{M}{r^2}
$$
- ii) If the gravitational force is the only force exerted on an object, the observed acceleration of the object (in $\text{m/s}^2$) is numerically equal to the magnitude of the gravitational field strength (in $\text{N/kg}$) at that location. 

### EK 2.6.A.3 
The gravitational force exerted by an astronomical body on a relatively small nearby object is called weight. \
*Derived equation:* 
$$
\text{Weight}=F_g=mg
$$

> LEARNING OBJECTIVE 2.6.B
> - Describe situations in which the gravitational force can be considered constant. 

### EK 2.6.B.1 
If the gravitational force between two systems’ centers of mass has a negligible change as the relative position of the two systems changes, the gravitational force can be considered constant at all points between the initial and final positions of the systems. 

### EK 2.6.B.2 
Near the surface of Earth, the strength of the gravitational field is
$$
g\approx 10\text{ N/kg}
$$ 

> LEARNING OBJECTIVE 2.6.C
> - Describe the conditions under which the magnitude of a system’s apparent weight is different from the magnitude of the gravitational force exerted on that system. 

### EK 2.6.C.1 
The magnitude of the apparent weight of a system is the magnitude of the normal force exerted on the system. 

### EK 2.6.C.2 
If the system is accelerating, the apparent weight of the system is not equal to the magnitude of the gravitational force exerted on the system. 

### EK 2.6.C.3 
A system appears weightless when there are no forces exerted on the system or when the force of gravity is the only force exerted on the system. 

### EK 2.6.C.4 
The equivalence principle states that an observer in a noninertial reference frame is unable to distinguish between an object’s apparent weight and the gravitational force exerted on the object by a gravitational field. 

> LEARNING OBJECTIVE 2.6.D 
> - Describe inertial and gravitational mass. 

### EK 2.6.D.1 
Objects have inertial mass, or inertia, a property that determines how much an object’s motion resists changes when interacting with another object. 

### EK 2.6.D.2 
Gravitational mass is related to the force of attraction between two systems with mass. 

### EK 2.6.D.3 
Inertial mass and gravitational mass have been experimentally verified to be equivalent.  

> LEARNING OBJECTIVE 2.6.E 
> - Describe the gravitational force exerted on an object by a uniform spherical distribution of mass. 

### EK 2.6.E.1 
The net gravitational force exerted on an object by a uniform spherical distribution of mass is the sum of the individual forces from small differential masses that comprise the distribution. 

### EK 2.6.E.2 
Newton’s shell theorem describes the net gravitational force exerted on an object by a uniform spherical shell of mass. 
- i) The net gravitational force exerted on an object inside a thin spherical shell is zero. 
- ii) The net gravitational force exerted on an object outside a thin spherical shell can be determined by treating the shell as a single massive object located at the center of the shell. 
- iii) An object inside a sphere of uniform density experiences a net gravitational force from only a partial mass of the sphere. 
- iv) The partial mass of a sphere that contributes to the net gravitational force exerted on an object within that sphere is the portion of the sphere’s mass located a distance less than or equal to the object’s distance from the center of the sphere and can be calculated using the density of the sphere. \
*Derived equation:* 
$$
m_{\text{partial}}=\frac{4}{3}\pi \rho\,r_{\text{partial}}^3
$$
### EK 2.6.E.3 
The gravitational force exerted on an object within a uniform sphere can be shown to be proportional to the object’s distance from the sphere’s center. \
*Derived equation:* 
$$
\vec{F}_{g,\text{partial}}=-k\,\vec{r}_{\text{partial}}
$$

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics does not expect students to mathematically prove or derive Newton’s shell theorem. 

## TOPIC 2.7 Kinetic and Static Friction  

> LEARNING OBJECTIVE 2.7.A 
> - Describe kinetic friction between two surfaces. 

### EK 2.7.A.1 
Kinetic friction occurs when two surfaces in contact move relative to each other. 
- i) The kinetic friction force is exerted in a direction opposite the motion of each surface relative to the other surface. 
- ii) The force of friction between two surfaces does not depend on the size of the surface area of contact. 

### EK 2.7.A.2 
The magnitude of the kinetic friction force exerted on an object is the product of the normal force the surface exerts on the object and the coefficient of kinetic friction. \
*Relevant equation:*
$$
\vec{F}_{f,k}=\mu_k \vec{F}_N
$$
- i) The coefficient of kinetic friction depends on the material properties of the surfaces that are in contact. 
- ii) Normal force is the perpendicular component of the force exerted on an object by the surface with which it is in contact; it is directed away from the surface. 

> LEARNING OBJECTIVE 2.7.B 
> - Describe static friction between two surfaces. 

### EK 2.7.B.1 
Static friction may occur between the contacting surfaces of two objects that are not moving relative to each other. 

### EK 2.7.B.2 
Static friction adopts the value and direction required to prevent an object from slipping or sliding on a surface. \
*Relevant equation:*
$$
F_{f,s}\le \mu_s F_N
$$
- i) Slipping and sliding refer to situations in which two surfaces are moving relative to each other. 
- ii) There exists a maximum value for which static friction will prevent an object from slipping on a given surface. \
*Derived equation:* 
$$
F_{f,s,\max}=\mu_s F_N
$$
### EK 2.7.B.3 
The coefficient of static friction is typically greater than the coefficient of kinetic friction for a given pair of surfaces. 

## TOPIC 2.8 Spring Forces  

> LEARNING OBJECTIVE 2.8.A 
> - Describe the force exerted on an object by an ideal spring. 

### EK 2.8.A.1 
An ideal spring has negligible mass and exerts a force that is proportional to the change in its length as measured from its relaxed length. A nonideal spring either has nonnegligible mass or exerts a force that is not proportional to the change in its length as measured from its relaxed length. 

### EK 2.8.A.2 
The magnitude of the force exerted by an ideal spring on an object is given by Hooke’s law:
$$
\vec{F}_s=-k\,\Delta \vec{x}
$$
### EK 2.8.A.3 
The force exerted on an object by a spring is always directed toward the equilibrium position of the object–spring system. 

> LEARNING OBJECTIVE 2.8.B 
> - Describe the equivalent spring constant of a combination of springs exerting forces on an object. 

### EK 2.8.B.1 
A collection of springs that exert forces on an object may behave as though they were a single spring with an equivalent spring constant keq. 
- i) The inverse of the equivalent spring constant of a set of springs in series is equal to the sum of the inverses of the individual spring constants. \
*Derived equation:* 
$$
\frac{1}{k_{\text{eq,series}}}=\sum_i \frac{1}{k_i}=\frac{1}{k_1}+\frac{1}{k_2}+\cdots
$$
- ii) The equivalent spring constant of a set of springs arranged in series is smaller than the smallest constituent spring constant. 
- iii) The equivalent spring constant of a set of springs arranged in parallel is the sum of the individual spring constants. \
*Derived equation:* 
$$
k_{\text{eq,parallel}}=\sum_i k_i=k_1+k_2+\cdots
$$

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics only expects students to find the effective spring constant of systems of springs that are arranged either in series or in parallel and does not expect students to find the effective spring constant of a system in which springs are arranged in both series and parallel. 

## TOPIC 2.9 Resistive Forces  

> LEARNING OBJECTIVE 2.9.A 
> - Describe the motion of an object subject to a resistive force. 

### EK 2.9.A.1 
A resistive force is defined as a velocitydependent force in the opposite direction of an object’s velocity, for example:
$$
\vec{F}_r=-k\vec{v}
$$

### EK 2.9.A.2 
Applying Newton’s second law to an object upon which a resistive force is exerted results in a differential equation for velocity. 
- i) Using the method of separation of variables, the velocity can be determined by integrating over the proper limits of integration. 
- ii) The acceleration or position of a moving object that is subject to a velocity-dependent force may be determined using initial conditions of the object and methods of calculus, once a function for velocity is determined. 
- iii) The position, velocity, and acceleration as functions of time of an object under the influence of a resistive force of the form $\vec{F}_r=-k\vec{v}$ are exponential and have asymptotes that are determined by the initial conditions of the object and the forces exerted on the object. 

### EK 2.9.A.3 
Terminal velocity is defined as the maximum speed achieved by an object moving under the influence of a constant force and a resistive force that are exerted on the object in opposite directions. The terminal condition is reached when the net force exerted on the object is zero. 

## TOPIC 2.10 Circular Motion

> LEARNING OBJECTIVE 2.10.A 
> - Describe the motion of an object traveling in a circular path. 

### EK 2.10.A.1 
Centripetal acceleration is the component of an object’s acceleration directed toward the center of the object’s circular path. 
- i) The magnitude of centripetal acceleration for an object moving in a circular path is the ratio of the object’s tangential speed squared to the radius of the circular path. \
*Relevant equation:*
$$
a_c=\frac{v^2}{r}
$$
- ii) Centripetal acceleration is directed toward the center of an object’s circular path. 

### EK 2.10.A.2 
Centripetal acceleration can result from a single force, more than one force, or components of forces that are exerted on an object in circular motion. 
- i) At the top of a vertical, circular loop, an object requires a minimum speed to maintain circular motion. At this point, and with this minimum velocity, the gravitational force is the only force that causes the centripetal acceleration. \
*Derived equation:* 
$$
v=\sqrt{gr}
$$
- ii) Components of the static friction force and the normal force can contribute to the net force producing centripetal acceleration of an object traveling in a circle on a banked surface. 
- iii) A component of tension contributes to the net force producing centripetal acceleration experienced by a conical pendulum. 

### EK 2.10.A.3 
Tangential acceleration is the rate at which an object’s speed changes and is directed tangent to the object’s circular path. 

### EK 2.10.A.4 
The net acceleration of an object moving in a circle is the vector sum of the centripetal acceleration and tangential acceleration. 

### EK 2.10.A.5 
The revolution of an object traveling in a circular path at a constant speed (uniform circular motion) can be described using period and frequency. 
- i) The time to complete one full circular path, one full rotation, or a full cycle of oscillatory motion is defined as period, $\text{T}$. 
- ii) The rate at which an object is completing revolutions is defined as frequency, $\textit{f}$. \
*Relevant equation:*
$$
T=\frac{1}{f}
$$
- iii) For an object traveling at a constant speed in a circular path, the period is given by the derived equation
$$
T=\frac{2\pi r}{v}
.$$
> LEARNING OBJECTIVE 2.10.B 
> - Describe circular orbits using Kepler’s third law. 

### EK 2.10.B.1 
For a satellite in circular orbit around a central body, the satellite’s centripetal acceleration is caused only by gravitational attraction. The period and radius of the circular orbit are related to the mass of the central body. \
*Derived equation:* 
$$
T^2=\frac{4\pi^2}{GM}R^3
$$

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics does not expect students to know Kepler’s first or second laws of planetary motion. 

# UNIT 3 Work, Energy, and Power

- 3.1 Translational Kinetic Energy
- 3.2 Work
- 3.3 Potential Energy
- 3.4 Conservation of Energy
- 3.5 Power

## TOPIC 3.1 Translational Kinetic Energy  

> LEARNING OBJECTIVE 3.1.A 
> - Describe the translational kinetic energy of an object in terms of the object’s mass and velocity. 

### EK 3.1.A.1 
An object’s translational kinetic energy is given by the equation
$$K=\frac{1}{2}mv^2$$

### EK 3.1.A.2 
Translational kinetic energy is a scalar quantity. 

### EK 3.1.A.3 
Different observers may measure different values of the translational kinetic energy of an object, depending on the observer’s frame of reference. 

## TOPIC 3.2 Work 

> LEARNING OBJECTIVE 3.2.A 
> - Describe the work done on an object or system by a given force or collection of forces. 

### EK 3.2.A.1 
Work is the amount of energy transferred into or out of a system by a force exerted on that system over a distance. 
- i) The work done by a conservative force exerted on a system is path-independent and only depends on the initial and final configurations of that system. 
- ii) The work done by a conservative force on a system—or the change in the potential energy of the system—will be zero if the system returns to its initial configuration. 
- iii) Potential energies are associated only with conservative forces. 
- iv) The work done by a nonconservative force is path-dependent. 
- v) The most common nonconservative forces are friction and air resistance. 

### EK 3.2.A.2 
Work is a scalar quantity that may be positive, negative, or zero. 

### EK 3.2.A.3 
The work done on an object by a variable force is calculated using $W=\int_{a}^{b}\vec{F}(r)\cdot d\vec{r}$, where the integral is taken over the path from point a to point b. 
- i) The dot product between two vectors, $\vec{A}$ and $\vec{B}$, results in a scalar quantity of magnitude
$$
\vec{A}\cdot\vec{B}=AB\cos\theta
.$$ 
- ii) Only the component of the force exerted on a system that is parallel to the displacement of the point of application of the force will change the system’s total energy. 
- iii) If the component of the force exerted on a system that is parallel to the displacement is constant, the work done on the system by the force is given by the derived equation
$$
W=F_{\parallel}d=Fd\cos\theta
.$$
- iv) The component of the force exerted on a system perpendicular to the direction of the displacement of the system’s center of mass can change the direction of the system’s motion without changing the system’s kinetic energy. 

### EK 3.2.A.4 
The work–energy theorem states that the change in an object’s kinetic energy is equal to the sum of the work (net work) being done by all forces exerted on the object. \
*Relevant equation:*
$$
\Delta K=\sum_i W_i=\sum_i F_{\parallel,i}\,d_i
$$
- i) An external force may change the configuration of a system. The component of the external force parallel to the displacement times the displacement of the point of application of the force gives the change in kinetic energy of the system.  
- ii) If the system’s center of mass and the point of application of the force move the same distance when a force is exerted on a system, then the system may be modeled as an object, and only the system’s kinetic energy can change. 
- iii) The energy dissipated by friction is typically equated to the force of friction times the length of the path over which the force is exerted.
$$
\Delta E_{\text{mech}}=F_f d\cos\theta
$$

### EK 3.2.A.5 
Work is equal to the area under the curve of a graph of $F_{\parallel}$ as a function of displacement. Describe the work done on an object or system by a given force or collection of forces. 

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics only expects students to analyze the transfer of mechanical energy, although students should be aware that mechanical energy may be dissipated in the form of thermal energy or sound. 

## TOPIC 3.3 Potential Energy  

> LEARNING OBJECTIVE 3.3.A 
> - Describe the potential energy of a system. 

### EK 3.3.A.1 
A system composed of two or more objects has potential energy if the objects within that system only interact with each other through conservative forces. 

### EK 3.3.A.2 
Potential energy is a scalar quantity associated with the position of objects within a system. 

### EK 3.3.A.3 
The definition of zero potential energy for a given system is a decision made by the observer considering the situation to simplify or otherwise assist in analysis. 

### EK 3.3.A.4 
The relationship between conservative forces exerted on a system and the system’s potential energy is
$$
\Delta U=-\int_{a}^{b}\vec{F}_{cf}(r)\cdot d\vec{r}.
$$

### EK 3.3.A.5 
The conservative forces exerted on a system in a single dimension can be determined using the slope of the system’s potential energy with respect to position in that dimension; these forces point in the direction of decreasing potential energy. \
*Relevant equation:* 
$$
F_x=-\frac{dU(x)}{dx}
.$$

### EK 3.3.A.6 
Graphs of a system’s potential energy as a function of its position can be useful in determining physical properties of that system.
- i) Stable equilibrium is a location at which a small displacement in an object’s position results in a force exerted on the object opposite to the direction of the small displacement, accelerating the object back toward the equilibrium position. 
- ii) Unstable equilibrium is a location at which a small displacement in an object’s position results in a force exerted on the object in the same direction as the small displacement, accelerating the object away from the equilibrium position. 
- iii) In a given dimension, stable equilibrium positions exist at locations where the potential energy as a function of position in that dimension has a local minimum. 
- iv) In a given dimension, unstable equilibrium positions occur at locations where the potential energy as a function of position in that dimension has a local maximum. 

### EK 3.3.A.7 
The potential energy of common physical systems can be described using the physical properties of that system. 
- i) The elastic potential energy of an ideal spring is given by the following equation, where Δx is the distance the spring has been stretched or compressed from its equilibrium length. \
*Relevant equation:*
$$
U_s=\frac{1}{2}k(\Delta x)^2
$$
- ii) The general form for the gravitational potential energy of a system consisting of two approximately spherical distributions of mass (e.g., moons, planets, or stars) is given by the equation
$$
U_g=-G\frac{m_1m_2}{r}
.$$
- iii) Because the gravitational field near the surface of a planet is nearly constant, the change in gravitational potential energy in a system consisting of an object with mass m and a planet with gravitational field of magnitude $g$ when the object is near the surface of the planet may be approximated by the equation
$$
\Delta U_g=mg\,\Delta y
.$$

### EK 3.3.A.8 
The total potential energy of a system containing more than two objects is the sum of the potential energy of each pair of objects within the system. 

## TOPIC 3.4 Conservation of Energy 

> LEARNING OBJECTIVE 3.4.A 
> - Describe the energies present in a system. 

### EK 3.4.A.1 
A system composed of only a single object can only have kinetic energy. 

### EK 3.4.A.2 
A system that contains objects that interact via conservative forces or that can change its shape reversibly may have both kinetic and potential energies. 

> LEARNING OBJECTIVE 3.4.B 
> - Describe the behavior of a system using conservation of mechanical energy principles.  

### EK 3.4.B.1 
Mechanical energy is the sum of a system’s kinetic and potential energies. 

### EK 3.4.B.2 
Any change to a type of energy within a system must be balanced by an equivalent change of other types of energies within the system or by a transfer of energy between the system and its surroundings. 

### EK 3.4.B.3 
A system may be selected so that the total energy of that system is constant. 

### EK 3.4.B.4 
If the total energy of a system changes, that change will be equivalent to the energy transferred into or out of the system.  

> LEARNING OBJECTIVE 3.4.C 
> - Describe how the selection of a system determines whether the energy of that system changes. 

### EK 3.4.C.1 
Energy is conserved in all interactions. 

### EK 3.4.C.2 
If the work done on a selected system is zero and there are no nonconservative interactions within the system, the total mechanical energy of the system is constant. 

### EK 3.4.C.3 
If the work done on a selected system is nonzero, energy is transferred between the system and the environment. 

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics expects students to know that mechanical energy can be dissipated as thermal energy or sound by nonconservative forces. 

## TOPIC 3.5 Power 

> LEARNING OBJECTIVE 3.5.A 
> - Describe the transfer of energy into, out of, or within a system in terms of power.

### EK 3.5.A.1 
Power is the rate at which energy changes with respect to time, either by transfer into or out of a system or by conversion from one type to another within a system. 

### EK 3.5.A.2 
Average power is the amount of energy being transferred or converted, divided by the time it took for that transfer or conversion to occur. \
*Relevant equation:*
$$
P_{\text{avg}}=\frac{\Delta E}{\Delta t}
.$$
### EK 3.5.A.3 
Because work is the change in energy of an object or system due to a force, average power is the total work done, divided by the time during which that work was done. \
*Relevant equation:*
$$
P_{\text{avg}}=\frac{W}{\Delta t}
.$$
### EK 3.5.A.4 
The instantaneous power delivered to an object by a force is given by the equation
$$P_{\text{inst}}=\frac{dW}{dt}
.$$
### EK 3.5.A.5 
The instantaneous power delivered to an object by the component of a constant force parallel to the object’s velocity can be described with the derived equation
$$
P_{\text{inst}}=F_{\parallel}v=Fv\cos\theta
.$$

# UNIT 4 Linear Momentum

- 4.1 Linear Momentum
- 4.2 Change in Momentum and Impulse
- 4.3 Conservation of Linear Momentum
- 4.4 Elastic and Inelastic Collisions

## TOPIC 4.1 Linear Momentum 

> LEARNING OBJECTIVE 4.1.A 
> - Describe the linear momentum of an object or system. 

### EK 4.1.A.1 
Linear momentum is defined by the equation$\vec{p}=m\vec{v}$. 

### EK 4.1.A.2 
Momentum is a vector quantity and has the same direction as the velocity. 

### EK 4.1.A.3 
Momentum can be used to analyze collisions and explosions. 
- i) A collision is a model for an interaction where the forces exerted between the involved objects in the system are much larger than the net external force exerted on those objects during the interaction. 
- ii) As only the initial and final states of a collision are analyzed, the object model may be used to analyze collisions. 
- iii) An explosion is a model for an interaction in which forces internal to the system move objects within that system apart.  


## TOPIC 4.2 Change in Momentum and Impulse  

> LEARNING OBJECTIVE 4.2.A 
> - Describe the impulse delivered to an object or system. 

### EK 4.2.A.1 
The rate of change of a system’s momentum is equal to the net external force exerted on that system. \
*Relevant equation:*

### EK 4.2.A.2 
Impulse is defined as the integral of a force exerted on an object or system over a time interval. \
*Relevant equation:*
$$
\vec{J}=\int_{t_1}^{t_2} \vec{F}_{net}(t)\,dt
$$
### EK 4.2.A.3 
Impulse is a vector quantity and has the same direction as the net force exerted on the system. 

### EK 4.2.A.4 
The impulse delivered to a system by a net external force is equal to the area under the curve of a graph of the net external force exerted on the system as a function of time. 

### EK 4.2.A.5 
The net external force exerted on a system is equal to the slope of a graph of the momentum of the system as a function of time.  

> LEARNING OBJECTIVE 4.2.B 
> - Describe the relationship between the impulse exerted on an object or system and the change in momentum of the object or system. 

### EK 4.2.B.1 
Change in momentum is the difference between a system’s final momentum and its initial momentum. \
*Relevant equation:*
$$
\Delta\vec{p}=\vec{p}-\vec{p_0}
$$
### EK 4.2.B.2 
The impulse–momentum theorem relates the impulse delivered to an object and the object’s change in momentum. 
- i) The impulse exerted on an object is equal to the object’s change in momentum. \
*Relevant equation:*
$$
\vec{J}=\int_{t_1}^{t_2} \vec{F}_{net}(t)\,dt=\Delta\vec{p}
$$
- ii) Newton’s second law of motion is a direct result of the impulse–momentum theorem applied to systems with constant mass.
$$
\vec{F}_{net}=\cfrac{d\vec{p}}{dt}=m\cfrac{d\vec{v}}{dt}=m\vec{a}
$$
- iii) The impulse–momentum theorem also describes the behavior of a system in which the velocity is constant but the mass changes with respect to time.
$$
\vec{F}_{net}=\cfrac{d\vec{p}}{dt}=\cfrac{dm}{dt}\vec{v}
$$

## TOPIC 4.3 Conservation of Linear Momentum  

> LEARNING OBJECTIVE 4.3.A 
> - Describe the behavior of a system using conservation of linear momentum. 

### EK 4.3.A.1 
A collection of objects with individual momenta can be described as one system with one center-of-mass velocity. 
- i) For a collection of objects, the velocity of a system’s center of mass can be calculated using the equation
$$
\vec{v}_{\textup{cm}}=\dfrac{\sum\vec{p}_{i}}{\sum{m_i}}=\dfrac{\sum{(m_i\vec{v}_{i})}}{m_i}
.$$
- ii) The velocity of a system’s center of mass is constant in the absence of a net external force. 

### EK 4.3.A.2 
The total momentum of a system is the sum of the momenta of the system’s constituent parts. 

### EK 4.3.A.3 
In the absence of net external forces, any change to the momentum of an object within a system must be balanced by an equivalent and opposite change of momentum elsewhere within the system. Any change to the momentum of a system is due to a transfer of momentum between the system and its surroundings. 
- i) The impulse exerted by one object on a second object is equal and opposite to the impulse exerted by the second object on the first. This is a direct result of Newton’s third law.

> LEARNING OBJECTIVE 4.3.A 
> - Describe the behavior of a system using conservation of linear momentum. 
- ii) A system may be selected so that the total momentum of that system is constant. 
- iii) If the total momentum of a system changes, that change will be equivalent to the impulse exerted on the system. \
*Relevant equation:*
$$
\vec{J}=\Delta\vec{p}
$$
### EK 4.3.A.4 
Correct application of conservation of momentum can be used to determine the velocity of a system immediately before and immediately after collisions or explosions. 

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics only expects students to quantitatively analyze collisions and interactions in one or two dimensions. Three-dimensional collisions may be analyzed qualitatively. 

> LEARNING OBJECTIVE 4.3.B 
> - Describe how the selection of a system determines whether the momentum of that system changes. 

### EK 4.3.B.1 
Momentum is **conserved** in all interactions. 

### EK 4.3.B.2 
If the net external force on the selected system is **zero**, the total momentum of the system is ***constant***. 

### EK 4.3.B.3 
If the net external force on the selected system is **nonzero**, ***momentum is transferred*** between the system and the environment. 

## TOPIC 4.4 Elastic and Inelastic Collisions  

> LEARNING OBJECTIVE 4.4.A 
> - Describe whether an interaction between objects is elastic or inelastic. 

### EK 4.4.A.1 
An elastic collision between objects is one in which the initial kinetic energy of the system is equal to the final kinetic energy of the system. 

### EK 4.4.A.2 
In an elastic collision, the final kinetic energies of each of the objects within the system may be different from their initial kinetic energies. 

### EK 4.4.A.3 
An inelastic collision between objects is one in which the total kinetic energy of the system decreases. 

### EK 4.4.A.4 
In an inelastic collision, some of the initial kinetic energy is not restored to kinetic energy but is transformed by nonconservative forces into other forms of energy. 

### EK 4.4.A.5 
In a perfectly inelastic collision, the objects stick together and move with the same velocity after the collision. AP PHYSICS C: MECHANICS UNIT 5 Torque and Rotational Dynamics 10–15% AP EXAM WEIGHTING ~14/~20 CLASS PERIODS 

# UNIT 5 Torque and Rotational Dynamics

- 5.1 Rotational Kinematics
- 5.2 Connecting Linear and Rotational Motion
- 5.3 Torque
- 5.4 Rotational Inertia
- 5.5 Rotational Equilibrium and Newton's First Law in Rotational Form
- 5.6 Newton's Second Law in Rotational Form

## TOPIC 5.1 Rotational Kinematics  

> LEARNING OBJECTIVE 5.1.A 
> - Describe the rotation of a system with respect to time using angular displacement, angular velocity, and angular acceleration. 

### EK 5.1.A.1 
Angular displacement is the measurement of the angle, in radians, through which a point on a rigid system rotates about a specified axis. \
*Relevant equation:*
$$
\Delta\theta=\theta-\theta_0
$$ 
- i) A rigid system is one that holds its shape but in which different points on the system move in different directions during rotation. A rigid system cannot be modeled as an object. 
- ii) One direction of angular displacement about an axis of rotation—clockwise or counterclockwise—is typically indicated as mathematically positive, with the other direction becoming mathematically negative. 
- iii) If the rotation of a system about an axis may be well described using the motion of the system’s center of mass, the system may be treated as a single object. For example, the rotation of Earth about its axis may be considered negligible when considering the revolution of Earth about the center of mass of the Earth–Sun system.  

### EK 5.1.A.2 
Angular velocity is the rate at which angular position changes with respect to time. \
*Relevant equation:*
$$
\omega=\dfrac{d\theta}{dt} 
$$
### EK 5.1.A.3 
Angular acceleration is the rate at which angular velocity changes with respect to time. \
*Relevant equation:* 
$$
\alpha=\dfrac{d\omega}{dt}
$$
### EK 5.1.A.4 
Angular displacement, angular velocity, and angular acceleration around one axis are analogous to linear displacement, velocity, and acceleration in one dimension and demonstrate the same mathematical relationships. 
- i) For constant angular acceleration, the mathematical relationships between angular displacement, angular velocity, and angular acceleration can be described with the following equations:
$$
\omega=\omega_0 + \alpha t
$$
$$
\theta=\theta_0 + \omega_0t + \dfrac{1}{2}\alpha t^2
$$
$$
\omega^2={\omega_0}^2+2\alpha(\theta-\theta_0)
$$
- ii) Graphs of angular displacement, angular velocity, and angular acceleration as functions of time can be used to find the relationships between those quantities. 

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics expects students to be able to mathematically manipulate the magnitudes of angular displacement, angular velocity, and angular acceleration using vector conventions. However, the directions of said vectors will not be assessed on the exam. 
> - Descriptions of the directions of rotational kinematics quantities for a point or rigid body are limited to clockwise and counterclockwise with respect to a given axis of rotation. 

## TOPIC 5.2 Connecting Linear and Rotational Motion  

> LEARNING OBJECTIVE 5.2.A 
> - Describe the linear motion of a point on a rotating rigid system that corresponds to the rotational motion of that point, and vice versa. 

### EK 5.2.A.1 
For a point at a distance r from a fixed axis of rotation, the linear distance s traveled by the point as the system rotates through an angle $\Delta\theta$ is given by the equation $\Delta s=r\Delta\theta$. 

### EK 5.2.A.2 
Derived relationships of linear velocity and of the tangential component of acceleration to their respective angular quantities are given by the following equations:
$$
s=r\theta
$$
$$
v=r\omega
$$
$$
a_{T}=r\alpha
$$
### EK 5.2.A.3 
For a rigid system, all points within that system have the same angular velocity and angular acceleration. 

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics expects students to be able to mathematically manipulate the magnitudes of angular displacement, angular velocity, and angular acceleration using vector conventions. However, the directions of the vectors will not be assessed on the exam. 
>- Descriptions of the directions of rotational kinematics quantities for a point or rigid body are limited to clockwise and counterclockwise with respect to a given axis of rotation. 

## TOPIC 5.3 Torque 

> LEARNING OBJECTIVE 5.3.A 
> - Identify the torques exerted on a rigid system.

### EK 5.3.A.1 
Torque results only from the force component perpendicular to the position vector from the axis of rotation to the point of application of the force. 

### EK 5.3.A.2 
The lever arm is the perpendicular distance from the axis of rotation to the line of action of the exerted force. 

> LEARNING OBJECTIVE 5.3.B 
> - Describe the torques exerted on a rigid system. 

### EK 5.3.B.1 
Torques can be described using force diagrams. 
- i) Force diagrams are similar to free-body diagrams and are used to analyze the torques exerted on a rigid system. 
- ii) Similar to free-body diagrams, force diagrams represent the relative magnitude and direction of the forces exerted on a rigid system. Force diagrams also depict the location at which those forces are exerted relative to the axis of rotation. 

### EK 5.3.B.2 
The torque exerted on a rigid system about a chosen pivot point by a given force is described by
$$
\vec{\tau}=\vec{r}\times\vec{F}
.$$
- i) The cross-product between two vectors, $\vec{A}$ and $\vec{B}$, results in a vector quantity of magnitude
$$
\vec{A}\times\vec{B}=AB\sin{\theta}
.$$
- ii) The direction of the vector resulting from the cross-product of vectors $\vec{A}$ and $\vec{B}$ is perpendicular to both vectors $\vec{A}$ and $\vec{B}$ and therefore is normal to the plane defined by vectors $\vec{A}$ and $\vec{B}$. 
- iii) The direction of the vector resulting from the cross-product of vectors $\vec{A}$ and $\vec{B}$ can be qualitatively determined by applying the appropriate right-hand rule. 

## TOPIC 5.4 Rotational Inertia  

> LEARNING OBJECTIVE 5.4.A 
> - Describe the rotational inertia of a rigid system relative to a given axis of rotation. 

### EK 5.4.A.1 
Rotational inertia measures a rigid system’s resistance to changes in rotation and is related to the mass of the system and the distribution of that mass relative to the axis of rotation. 

### EK 5.4.A.2 
The rotational inertia of an object rotating a perpendicular distance $r$ from an axis is described by the equation 
$$
I=mr^2
.$$ 

### EK 5.4.A.3 
The total rotational inertia of a collection of objects about an axis is the sum of the rotational inertias of each object about that axis.
$$
I_{tot}=\sum_{I_{i}}=\sum_{m_i{r_i}^2}
$$

### EK 5.4.A.4 
For a solid that can be considered as a collection of differential masses, dm, the solid’s rotational inertia can be calculated using the equation
$$
I = \int{r^2}\,dm
,$$
where $r$ is the perpendicular distance from $dm$ to the axis of rotation. 

> LEARNING OBJECTIVE 5.4.B 
> - Describe the rotational inertia of a rigid system rotating about an axis that does not pass through the system’s center of mass. 

### EK 5.4.B.1 
A rigid system’s rotational inertia in a given plane is at a minimum when the rotational axis passes through the system’s center of mass.

### EK 5.4.B.2 
The parallel axis theorem uses the following equation to relate the rotational inertia of a rigid system about any axis that is parallel to an axis through its center of mass:
$$
I'=I_{\textup{cm}} + Md^2
$$ 

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics only expects students to use calculus in the derivations of the rotational inertia of thin rods of uniform or nonuniform density about an arbitrary axis perpendicular to the rod, as well as derivations of the rotational inertia of a thin cylindrical shell, disk, or rigid bodies that can be considered to be made up of coaxial rings or shells about an axis that passes through their centers (e.g., annular rings). Students should have a qualitative understanding of the factors that affect rotational inertia; for example, how rotational inertia is greater when mass is farther from the axis of rotation, which is why a hoop has more rotational inertia than a solid puck of the same mass and radius. 

## TOPIC 5.5 Rotational Equilibrium and Newton’s First Law in Rotational Form  

> LEARNING OBJECTIVE 5.5.A 
> - Describe the conditions under which a system’s angular velocity remains constant. 

### EK 5.5.A.1 
A system may exhibit rotational equilibrium (constant angular velocity) without being in translational equilibrium, and vice versa. 
- i) Free-body and force diagrams describe the nature of the forces and torques exerted on an object or rigid system. 
- ii) Rotational equilibrium is a configuration of torques such that the net torque exerted on the system is zero. \
*Relevant equation:*
$$
\sum{\tau_i}=0
$$
- iii) The rotational analog of Newton’s first law is that a system will have a constant angular velocity only if the net torque exerted on the system is zero. 

### EK 5.5.A.2 
A rotational corollary to Newton’s second law states that if the torques exerted on a rigid system are not balanced, the system’s angular velocity must be changing. 

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics does not expect students to simultaneously analyze rotation in multiple planes. 

## TOPIC 5.6 Newton’s Second Law in Rotational Form  

> LEARNING OBJECTIVE 5.6.A 
> - Describe the conditions under which a system’s angular velocity changes. 

### EK 5.6.A.1 
Angular velocity changes when the net torque exerted on the object or system is not equal to zero. 

### EK 5.6.A.2 
The rate at which the angular velocity of a rigid system changes is directly proportional to the net torque exerted on the rigid system and is in the same direction. The angular acceleration of the rigid system is inversely proportional to the rotational inertia of the rigid system. \
*Relevant equation:*
$$
\alpha_{\textup{sys}}=\dfrac{\sum{\tau}}{I_{\textup{sys}}}=\dfrac{\tau_{\textup{net}}}{I_{\textup{sys}}}
$$
### EK 5.6.A.3 
To fully describe a rotating rigid system, linear and rotational analyses may need to be performed independently.

# UNIT 6 Energy and Momentum of Rotating Systems

- 6.1 Rotational Kinetic Energy
- 6.2 Torque and Work
- 6.3 Angular Momentum and Angular Impulse
- 6.4 Conservation of Angular Momentum
- 6.5 Rolling
- 6.6 Motion of Orbiting Satellites

## TOPIC 6.1 Rotational Kinetic Energy  

> LEARNING OBJECTIVE 6.1.A 
> - Describe the rotational kinetic energy of a rigid system in terms of the rotational inertia and angular velocity of that rigid system. 

### EK 6.1.A.1 
The rotational kinetic energy of an object or rigid system is related to the rotational inertia and angular velocity of the rigid system and is given by the equation
$$
K_{\textup{rot}}=\dfrac{1}{2}I\omega^2
.$$
- i) The rotational inertia of an object about a fixed axis can be used to show that the rotational kinetic energy of that object is equivalent to its translational kinetic energy, which is its total kinetic energy. 
- ii) The total kinetic energy of a rigid system is the sum of its rotational kinetic energy due to its rotation about its center of mass and the translational kinetic energy due to the linear motion of its center of mass. 

### EK 6.1.A.2 
A rigid system can have rotational kinetic energy while its center of mass is at rest due to the individual points within the rigid system having linear speed and, therefore, kinetic energy. 

### EK 6.1.A.3 
Rotational kinetic energy is a scalar quantity. 

## TOPIC 6.2 Torque and Work  

> LEARNING OBJECTIVE 6.2.A 
> - Describe the work done on a rigid system by a given torque or collection of torques. 

### EK 6.2.A.1 
A torque can transfer energy into or out of an object or rigid system if the torque is exerted over an angular displacement. 

### EK 6.2.A.2 
The amount of work done on a rigid system by a torque is related to the magnitude of that torque and the angular displacement through which the rigid system rotates during the interval in which that torque is exerted. \
*Relevant equation:*
$$
W=\int_{\theta_1}^{\theta_2} \tau\,d\theta
$$
### EK 6.2.A.3 
Work done on a rigid system by a given torque can be found from the area under the curve of a graph of the torque as a function of angular position. 

## TOPIC 6.3 Angular Momentum and Angular Impulse  

> LEARNING OBJECTIVE 6.3.A 
> - Describe the angular momentum of an object or rigid system. 

### EK 6.3.A.1 
The magnitude of the angular momentum of a rigid system about a specific axis can be described with the equation
$$
L = I\omega
.$$
### EK 6.3.A.2 
The angular momentum of an object about a given point is
$$
\vec{L}=\vec{r}\times\vec{p}
.$$ 
- i) The selection of the axis about which an object is considered to rotate influences the determination of the angular momentum of that object. 
- ii) The measured angular momentum of an object traveling in a straight line depends on the distance between the reference point and the object, the mass of the object, the speed of the object, and the angle between the radial distance and the velocity of the object. 

> LEARNING OBJECTIVE 6.3.B 
> - Describe the angular impulse delivered to an object or rigid system by a torque. 

### EK 6.3.B.1 
Angular impulse is defined as the product of the torque exerted on an object or rigid system and the time interval during which the torque is exerted. \
*Relevant equation:*
$$
\text{amgular impulse}=\int\tau\,dt
$$
### EK 6.3.B.2 
Angular impulse has the same direction as the torque imparting it. 

### EK 6.3.B.3 
The angular impulse delivered to an object or rigid system by a torque can be found from the area under the curve of a graph of the torque as a function of time. 

> LEARNING OBJECTIVE 6.3.C 
> - Relate the change in angular momentum of an object or rigid system to the angular impulse given to that object or rigid system. 

### EK 6.3.C.1 
The magnitude of the change in angular momentum can be described by comparing the magnitudes of the final and initial momenta of the object or rigid system.
$$
\Delta L=L-L_{0}
$$
### EK 6.3.C.2 
A rotational form of the impulse–momentum theorem relates the angular impulse delivered to an object or rigid system and the change in angular momentum of that object or rigid system. 
- i) The angular impulse exerted on an object or rigid system is equal to the change in angular momentum of that object or rigid system. \
*Relevant equation:*
$$
\Delta L = \int_{t_1}^{t_2} \tau\,dt
$$
- ii) The rotational form of the impulse– momentum theorem is a direct result of Newton’s second law of motion for cases in which rotational inertia is constant.
$$
\tau_{\textup{net}}=\dfrac{dL}{dt}=I\dfrac{d\omega}{dt}=I\alpha
$$
### EK 6.3.C.3 
The net torque exerted on an object or rigid system is equal to the slope of the graph of the angular momentum of an object as a function of time. 

### EK 6.3.C.4 
The angular impulse delivered to an object or rigid system is equal to the area under the curve of a graph of the net external torque exerted on an object as a function of time. 

## TOPIC 6.4 Conservation of Angular Momentum  

> LEARNING OBJECTIVE 6.4.A 
> - Describe the behavior of a system using conservation of angular momentum. 

### EK 6.4.A.1 
The total angular momentum of a system about a rotational axis is the sum of the angular momenta of the system’s constituent parts about that rotational axis. 

### EK 6.4.A.2 
Any change to a system’s angular momentum must be due to an interaction between the system and its surroundings. 
- i) The angular impulse exerted by one object or system on a second object or system is equal and opposite to the angular impulse exerted by the second object or system on the first. This is a direct result of Newton’s third law. 
- ii) A system may be selected so that the total angular momentum of that system is constant. 
- iii) The angular speed of a nonrigid system may change without the angular momentum of the system changing if the system changes shape by moving mass closer to or farther from the rotational axis. 
- iv) If the total angular momentum of a system changes, that change will be equivalent to the angular impulse exerted on the system.  

> LEARNING OBJECTIVE 6.4.B 
> - Describe how the selection of a system determines whether the angular momentum of that system changes. 

### EK 6.4.B.1 
Angular momentum is conserved in all interactions. 

### EK 6.4.B.2 
If the net external torque exerted on a selected object or rigid system is zero, the total angular momentum of that system is constant. 

### EK 6.4.B.3 
If the net external torque exerted on a selected object or rigid system is nonzero, angular momentum is transferred between the system and the environment. 

## TOPIC 6.5 Rolling  

> LEARNING OBJECTIVE 6.5.A 
> - Describe the kinetic energy of a system that has translational and rotational motion. 

### EK 6.5.A.1 
The total kinetic energy of a system is the sum of the system’s translational and rotational kinetic energies. \
*Relevant equation:* 
$$
K_{\textup{tot}}=K_{\textup{trans}}+K_{\textup{rot}}
$$

> LEARNING OBJECTIVE 6.5.B 
> - Describe the motion of a system that is rolling without slipping. 

### EK 6.5.B.1 
While rolling without slipping, the translational motion of a system’s center of mass is related to the rotational motion of the system itself with the following equations:
$$
\Delta x_{\textup{cm}}=r\Delta\theta
$$
$$
v_{\textup{cm}}=r\omega
$$
$$
a_{\textup{cm}}=r\alpha
$$
### EK 6.5.B.2 
For ideal cases, rolling without slipping implies that the frictional force does not dissipate any energy from the rolling system. 

> LEARNING OBJECTIVE 6.5.C 
> - Describe the motion of a system that is rolling while slipping. 

### EK 6.5.C.1 
When slipping, the motion of a system’s center of mass and the system’s rotational motion cannot be directly related. 

### EK 6.5.C.2 
When a rotating system is slipping relative to another surface, the point of application of the force of kinetic friction exerted on the system moves with respect to the surface, so the force of kinetic friction will dissipate energy from the system. 

> BOUNDARY STATEMENT 
> - Rolling friction is beyond the scope of AP Physics C: Mechanics. 

## TOPIC 6.6 Motion of Orbiting Satellites  

> LEARNING OBJECTIVE 6.6.A 
> - Describe the motions of a system consisting of two objects or systems interacting only via gravitational forces. 

### EK 6.6.A.1 
In a system consisting only of a massive central object and an orbiting satellite with mass that is negligible in comparison to the central object’s mass, the motion of the central object itself is negligible. 

### EK 6.6.A.2 
The motion of satellites in orbits is constrained by conservation laws. 
- i) In circular orbits, the system’s total mechanical energy, the system’s gravitational potential energy, and the satellite’s angular momentum and kinetic energy are constant. 
- ii) In elliptical orbits, the system’s total mechanical energy and the satellite’s angular momentum are constant, but the system’s gravitational potential energy and the satellite’s kinetic energy can each change. 
- iii) The gravitational potential energy of a system consisting of a satellite and a massive central object is defined to be zero when the satellite is an infinite distance from the central object. \
*Relevant equation:*
$$
U_{g}=-G\dfrac{m_1 m_2}{r}
$$

### EK 6.6.A.3 
The total energy of a system consisting of a satellite orbiting a central object in a circular path can be written in terms of the gravitational potential energy of that system or the kinetic energy of the satellite. \
*Derived equations:*
$$
K=-\dfrac{1}{2}U
$$
$$
E_{total}=\dfrac{1}{2}U=-\dfrac{GMm}{2r}
$$

### EK 6.6.A.4 
The escape velocity of a satellite is the satellite’s velocity such that the mechanical energy of the satellite–central-object system is equal to zero. 
- i) When the only force exerted on a satellite is gravity from a central object, a satellite that reaches escape velocity will move away from the central body until its speed reaches zero at an infinite distance from the central body. 
- ii) The escape velocity of a satellite from a central body of mass $M$ can be derived using conservation of energy laws. \
*Derived equation:* 
$$
v_{\textup{esc}}=\sqrt{\dfrac{2GM}{r}}
$$

# UNIT 7 Oscillations

- 7.1 Defining Simple Harmonic Motion (SHM)
- 7.2 Frequency and Period of SHM
- 7.3 Representing and Analyzing SHM
- 7.4 Energy of Simple Harmonic Oscillators
- 7.5 Simple and Physical Pendulums

## TOPIC 7.1 Defining Simple Harmonic Motion (SHM)  

> LEARNING OBJECTIVE 7.1.A 
> - Describe simple harmonic motion. 

### EK 7.1.A.1 
Simple harmonic motion is a special case of periodic motion. 

### EK 7.1.A.2 
SHM results when the magnitude of the restoring force exerted on an object is proportional to that object’s displacement from its equilibrium position. \
*Derived equation:* 
$$
ma_x=-k\Delta x
$$
- i) A restoring force is a force that is exerted in a direction opposite to the object’s displacement from an equilibrium position. 
- ii) An equilibrium position is a location at which the net force exerted on an object or system is zero. 

## TOPIC 7.2 Frequency and Period of SHM  

> LEARNING OBJECTIVE 7.2.A 
> - Describe the frequency and period of an object exhibiting SHM. 

### EK 7.2.A.1 
The period of SHM is related to the angular frequency, $\omega$, of the object’s motion by the following equation:
$$
T=\dfrac{2\pi}{\omega}=\dfrac{1}{f}
$$
- i) The period of an object–ideal-spring oscillator is given by the equation
$$
T_s=2\pi\sqrt{\dfrac{m}{k}}
.$$
- ii) The period of a simple pendulum displaced by a small angle is given by the equation
$$
T_p=2\pi\sqrt{\dfrac{l}{g}}
.$$

## TOPIC 7.3 Representing and Analyzing SHM  

> LEARNING OBJECTIVE 7.3.A 
> - Describe the displacement, velocity, and acceleration of an object exhibiting SHM. 

### EK 7.3.A.1 
For an object exhibiting SHM, the displacement of that object measured from its equilibrium position can be represented by the equations
$$
x=A\cos{2\pi ft} \text{ or } x=A\sin{2\pi ft}
.$$
- i) Minima, maxima, and zeros of displacement, velocity, and acceleration are features of harmonic motion. 
- ii) Recognizing the positions or times at which the displacement, velocity, and acceleration for SHM have extrema or zeros can help in qualitatively describing the behavior of the motion. 

### EK 7.3.A.2 
The position as a function of time for an object exhibiting SHM is a solution of the secondorder differential equation derived from the application of Newton’s second law. \
*Derived equation:* 
$$
\dfrac{d^2x}{dt^2}=-\omega^2x
$$

### EK 7.3.A.3 
Characteristics of SHM, such as velocity and acceleration, can be determined by or derived from the equation
$$
x = A\cos{\omega t + \phi}
.$$
- i) The acceleration of an object exhibiting SHM is related to the object’s angular frequency and position. \
*Derived equation:* 
$$
a=-\omega^2x
$$
- ii) It can be shown that the maximum velocity and acceleration of an object exhibiting SHM are related to the angular frequency of the object’s motion. \
*Derived equations:*
$$
v_{\textup{max}}=A\omega
$$
$$
a_{\textup{max}}=A\omega^2
$$
### EK 7.3.A.4 
In the presence of a sinusoidal external force, a system may exhibit resonance. 
- i) Resonance occurs when an external force is exerted at the natural frequency of an oscillating system. 
- ii) Resonance increases the amplitude of oscillating motion. 
- iii) The natural frequency of a system is the frequency at which the system will oscillate when it is displaced from its equilibrium position. 

### EK 7.3.A.5 
Changing the amplitude of a system exhibiting SHM will not change its period. 

### EK 7.3.A.6 
Properties of SHM can be determined and analyzed using graphical representations. 

> BOUNDARY STATEMENT 
> - AP Physics C: Mechanics only expects students to know the solution to the second-order differential equation that describes SHM, as well as be able to identify SHM. AP Physics C: Mechanics does not expect students to mathematically prove that the solution is correct. 

## TOPIC 7.4 Energy of Simple Harmonic Oscillators  

> LEARNING OBJECTIVE 7.4.A 
> - Describe the mechanical energy of a system exhibiting SHM. 

### EK 7.4.A.1 
The total energy of a system exhibiting SHM is the sum of the system’s kinetic and potential energies. \
*Relevant equation:*
$$
E_{\textup{total}}=U+K
$$
### EK 7.4.A.2 
Conservation of energy indicates that the total energy of a system exhibiting SHM is constant. 

### EK 7.4.A.3 
The kinetic energy of a system exhibiting SHM is at a maximum when the system’s potential energy is at a minimum. 

### EK 7.4.A.4 
The potential energy of a system exhibiting SHM is at a maximum when the system’s kinetic energy is at a minimum. 
- i) The minimum kinetic energy of a system exhibiting SHM is zero. 
- ii) hanging the amplitude of a system exhibiting SHM will change the maximum potential energy of the system and, therefore, the total energy of the system. \
*Relevant equation for a spring–object system:*
$$
E_{\textup{total}}=\dfrac{1}{2}kA^2
$$
## TOPIC 7.5 Simple and Physical Pendulums  

> LEARNING OBJECTIVE 7.5.A 
> - Describe the properties of a physical pendulum. 

### EK 7.5.A.1 
A physical pendulum is a rigid body that undergoes oscillation about a fixed axis. 

### EK 7.5.A.2 
For small amplitudes of motion, the period of a physical pendulum is derived from the application of Newton’s second law in rotational form. \
*Relevant equation:*
$$
T_{\textup{phys}}=2\pi\sqrt{\dfrac{I}{mgd}}
$$
- i) When displaced from equilibrium, the gravitational force exerted on a physical pendulum’s center of mass provides a restoring torque. \
*Derived equation:* 
$$
\tau=-mgd\sin{\theta}
$$
- ii) For small amplitudes of motion, the smallangle approximation can be applied to the restoring torque. \
*Derived equation:* 
$$
\sin{\theta}\approx \theta
$$
$$
\tau=-mgd\theta=I\alpha
$$
- iii) The small-angle approximation and Newton’s second law in rotational form yield a second-order differential equation that describes SHM:
$$
\dfrac{d^2\theta}{dt^2}=-\omega^2\theta
$$

### EK 7.5.A.3 
A simple pendulum is a special case of physical pendulums in which the hanging object can be modeled as a point mass at a distance, l, from the pivot point.\
*Relevant equation:*
$$
T_p=2\pi\sqrt{\dfrac{l}{g}}
$$
### EK 7.5.A.4 
A torsion pendulum is a case of SHM where the restoring torque is proportional to the angular displacement of a rotating system. For example, a horizontal disk that is suspended from a wire attached to its center of mass may undergo rotational oscillations about the wire in the horizontal plane. \
*Derived equation:* 
$$
I\alpha=-k\Delta\theta
$$