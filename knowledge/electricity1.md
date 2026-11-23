# Introduction to Electricity and Basic Circuit Design

## Introduction

Electricity can seem complicated because we cannot directly see electrons moving inside a wire. A useful way to understand circuits is to start at the atomic level and then gradually move toward practical circuits.

The basic idea is:

**Electric charge moves → current flows → electrical components control that current → useful work happens.**

For example, a battery can provide the energy that causes charge to move through a circuit. A lightbulb converts some of that electrical energy into light and heat.

---

# Part 1 — Pushing Electrons

## Atomic Level Science

Everything around us is made of atoms.

An atom contains:

* **Protons** — positively charged
* **Neutrons** — electrically neutral
* **Electrons** — negatively charged

In many metals, some electrons can move through the material relatively easily. These are commonly called **conduction electrons**.

When there is no applied electric field, their motion is mostly random.

When a voltage is applied across a conductor, an electric field is established. The electric field exerts a force on charged particles, causing the electrons to develop a small average drift.

That organized movement of electric charge is **electric current**.

### Example

Imagine a copper wire connected to a battery.

The battery establishes an electric field through the circuit. The electrons in the copper respond to this field and acquire a net drift.

The electrons do not need to travel from the battery all the way to the lightbulb before the bulb responds. The electric field is established through the circuit, causing charges throughout the conductor to respond.

---

## A History of Electrical Discoveries

Our understanding of electricity developed over a long period.

Scientists gradually discovered that electricity and magnetism were related and developed mathematical laws describing electrical phenomena.

Important discoveries included:

* Understanding electric charge
* Understanding electric current
* Understanding voltage
* Discovering relationships between electricity and magnetism
* Developing practical batteries, generators, motors, and electrical circuits

Modern electronics are built on this accumulated knowledge.

---

## Why Do Lightbulbs Glow?

A lightbulb converts electrical energy into other forms of energy.

When current flows through a suitable light-producing element, electrical energy is converted into light and heat.

Modern LEDs work differently from traditional incandescent bulbs. An LED produces light using semiconductor materials rather than heating a wire until it glows.

### Example

A battery connected to an LED forms a circuit:

**Battery → wire → LED → wire → battery**

When the circuit is properly connected and the LED receives suitable current, it produces light.

---

# Part 2 — Go With the Flow

## Water Analogies

Water is often used as an analogy for electricity because it can make basic circuit ideas easier to visualize.

A rough comparison is:

| Water system        | Electrical system |
| ------------------- | ----------------- |
| Water flow          | Electric current  |
| Pressure difference | Voltage           |
| Narrow pipe         | Resistance        |
| Pump                | Energy source     |

The analogy is useful, but electricity is **not literally water flowing through wires**. It is only a way to build intuition.

---

## Ohm's Law

Ohm's Law describes the relationship between voltage, current, and resistance.

$$
V = I \times R
$$

Where:

* **V** = voltage, measured in volts (V)
* **I** = current, measured in amperes (A)
* **R** = resistance, measured in ohms (Ω)

The equation can also be rearranged:

$$
I = \frac{V}{R}
$$

$$
R = \frac{V}{I}
$$

### Example

Suppose a 12 V source is connected to a 4 Ω resistor.

$$
I = \frac{V}{R}
$$

$$
I = \frac{12}{4}
$$

$$
I = 3\,A
$$

So the current is 3 amperes, assuming the resistor behaves according to Ohm's law under those conditions.

---

## Electrical Power

Electrical power describes how quickly electrical energy is transferred or converted.

Power is measured in **watts (W)**.

The basic power equation is:

$$
P = V \times I
$$

Where:

* **P** = power in watts (W)
* **V** = voltage in volts (V)
* **I** = current in amperes (A)

Using Ohm's Law, power can also be calculated using resistance:

$$
P = I^2 \times R
$$

or:

$$
P = \frac{V^2}{R}
$$

### Example

A device operates at 12 V and draws 2 A.

$$
P = V \times I
$$

$$
P = 12 \times 2
$$

$$
P = 24\,W
$$

The device is using or transferring electrical power at a rate of **24 watts**.

### Important idea

Energy and power are related, but they are not the same thing.

* **Energy** tells us how much electrical work is transferred.
* **Power** tells us how quickly that energy is transferred.

For example, a 100 W device transfers energy faster than a 10 W device.

---

## Real-World Measurements

Electrical quantities can be measured using instruments.

A **voltmeter** measures voltage.

An **ammeter** measures current.

A **multimeter** can commonly measure several electrical quantities, such as voltage, resistance, and current, depending on the model and its settings.

Power can be calculated when voltage and current are known.

Measurements are important because real circuits may behave differently from ideal calculations.

---

## Theory Into Practice

Circuit theory gives us a way to predict what should happen before building a circuit.

For example, if we know:

* Supply voltage = 9 V
* Resistance = 1 kΩ

Then:

$$
I = \frac{V}{R}
$$

$$
I = \frac{9}{1000}
$$

$$
I = 0.009\,A
$$

$$
I = 9\,mA
$$

The resistor's power can also be calculated:

$$
P = V \times I
$$

$$
P = 9 \times 0.009
$$

$$
P = 0.081\,W
$$

So the resistor is dissipating approximately **0.081 W**, or **81 mW**, under these ideal conditions.

This lets us estimate circuit behavior before connecting the components.

---

# Series Circuits

In a series circuit, components are connected along a single path for current.

### Voltage

The total voltage is the sum of the voltage across each component:

$$
V_{\text{total}} = V_1 + V_2 + V_3 + \cdots
$$

### Resistance

The total resistance is the sum of the individual resistances:

$$
R_{\text{total}} = R_1 + R_2 + R_3 + \cdots
$$

### Current

The same current flows through every component:

$$
I_{\text{total}} = I_1 = I_2 = I_3 = \cdots
$$

### Example

Suppose three resistors are connected in series:

* R₁ = 2 Ω
* R₂ = 3 Ω
* R₃ = 5 Ω

The total resistance is:

$$
R_{\text{total}} = 2 + 3 + 5
$$

$$
R_{\text{total}} = 10\,\Omega
$$

If the circuit has a 20 V supply:

$$
I = \frac{V}{R}
$$

$$
I = \frac{20}{10}
$$

$$
I = 2\,A
$$

Because this is a series circuit, the current through every resistor is **2 A**.

The individual voltage drops add up to the total supply voltage:

$$
V_1 + V_2 + V_3 = 20\,V
$$

### Simple rule

**Series → same current, voltage adds, resistance adds.**

---

# Resistors

A resistor is a component designed to provide electrical resistance.

Resistance limits current and causes electrical energy to be dissipated, usually as heat.

The power dissipated by a resistor can be calculated using:

$$
P = V \times I
$$

$$
P = I^2 \times R
$$

$$
P = \frac{V^2}{R}
$$

### Example

A resistor has:

* Resistance = 100 Ω
* Current = 0.1 A

Its power is:

$$
P = I^2 \times R
$$

$$
P = 0.1^2 \times 100
$$

$$
P = 1\,W
$$

Therefore, the resistor is dissipating **1 watt**.

A resistor must be selected with a suitable power rating for the circuit.

### Example

A resistor can be placed in series with an LED to limit the current and help prevent excessive current from damaging the LED.

---

# Parallel Circuits

In a parallel circuit, components are connected across the same two electrical nodes.

### Voltage

The voltage across every parallel branch is the same:

$$
V_{\text{total}} = V_1 = V_2 = V_3 = \cdots
$$

### Current

The total current is the sum of the current through each branch:

$$
I_{\text{total}} = I_1 + I_2 + I_3 + \cdots
$$

### Resistance

The reciprocal of the total resistance is the sum of the reciprocals of the individual resistances:

$$
\frac{1}{R_{\text{total}}}
=
\frac{1}{R_1}
+
\frac{1}{R_2}
+
\frac{1}{R_3}
+
\cdots
$$

Therefore:

$$
R_{\text{total}}
=
\frac{1}{
\frac{1}{R_1}
+
\frac{1}{R_2}
+
\frac{1}{R_3}
+
\cdots
}
$$

For two resistors, another useful formula is:

$$
R_{\text{total}}
=
\frac{R_1 \times R_2}{R_1 + R_2}
$$

### Example

Two 10 Ω resistors are connected in parallel.

$$
R_{\text{total}}
=
\frac{10 \times 10}{10 + 10}
$$

$$
R_{\text{total}}
=
\frac{100}{20}
$$

$$
R_{\text{total}}
=
5\,\Omega
$$

Notice that the total resistance is lower than either individual resistor.

If the parallel circuit is connected to a 10 V source:

$$
V_1 = V_2 = 10\,V
$$

Using Ohm's Law:

$$
I_1 = \frac{10}{10}
$$

$$
I_1 = 1\,A
$$

$$
I_2 = \frac{10}{10}
$$

$$
I_2 = 1\,A
$$

Therefore:

$$
I_{\text{total}} = I_1 + I_2
$$

$$
I_{\text{total}} = 1 + 1
$$

$$
I_{\text{total}} = 2\,A
$$

The total power supplied to the parallel circuit is:

$$
P = V \times I
$$

$$
P = 10 \times 2
$$

$$
P = 20\,W
$$

### Simple rule

**Parallel → same voltage, current adds, reciprocal resistance.**

---

# Complex Circuits

Real circuits can contain combinations of series and parallel connections.

A useful method is to simplify the circuit one section at a time.

For example:

1. Identify resistors in series.
2. Calculate their equivalent resistance.
3. Identify parallel sections.
4. Calculate their equivalent resistance.
5. Continue until the entire circuit has been reduced to one equivalent resistance.
6. Use Ohm's Law to calculate the total current.
7. Use voltage and current to calculate power when needed.

This makes complicated circuits easier to analyze.

---

# Part 3 — Controlling Nature

## Manual Switches

A switch controls whether a circuit path is open or closed.

When a switch is **closed**, current can flow through the intended path.

When a switch is **open**, the path is interrupted.

### Example

A flashlight uses a switch to control whether current reaches the light source.

---

# Schematics

A schematic is a simplified drawing that represents an electrical circuit.

Instead of drawing components exactly as they physically look, standardized symbols are used.

For example, a schematic might represent:

**Battery → switch → resistor → LED → battery**

Schematics help engineers understand and design circuits without needing to draw the physical arrangement of every component.

---

# Switch Poles and Throws

Switches can be described using terms such as:

* **Pole** — the number of separate circuits a switch controls.
* **Throw** — the number of positions or paths available to the switch.

For example, an SPST switch means:

**Single Pole, Single Throw**

It is essentially a simple on/off switch for one circuit.

---

# Magnetism Basics

Electricity and magnetism are closely connected.

An electric current produces a magnetic field around a conductor.

The magnetic field becomes stronger when the current increases, although the exact behavior depends on the geometry and material.

### Example

When current flows through a straight wire, a magnetic field forms around the wire.

---

# Electromagnets

An electromagnet uses electric current to produce a magnetic field.

A coil of wire can produce a stronger magnetic field than a single straight wire.

Adding a suitable magnetic core can increase the magnetic effect.

### Example

Electromagnets are used in:

* Relays
* Electric motors
* Solenoids
* Lifting magnets

---

# Permanent Magnets

A permanent magnet produces a magnetic field without requiring continuous electrical current.

Permanent magnets are made from materials whose magnetic properties can remain after magnetization.

### Example

The magnet in a small speaker interacts with magnetic fields produced by current in a coil, allowing electrical signals to produce movement and sound.

---

# Electromechanical Switches

A relay is an example of an electromechanical switch.

A small electrical current can energize a coil, producing a magnetic field that mechanically moves contacts.

This allows one circuit to control another circuit.

### Example

A low-power control circuit can activate a relay, which then switches a separate higher-power circuit.

---

# Simple Switch Logic

Switches can also be used to create simple logical behavior.

For example:

**AND behavior:** Two switches must both be closed for the output to activate.

**OR behavior:** Either of two switches can activate the output.

These simple ideas are the foundation of more advanced digital logic.

---

# Part 4 — Basic Safety

## Why Wires Must Be Protected

Electrical current produces heating in wires.

If too much current flows through a wire, it can become dangerously hot.

Therefore, wires must be selected according to the amount of current they are expected to carry and the conditions in which they are used.

---

# The American Wire Gauge

American Wire Gauge (AWG) is a system used to specify wire sizes.

In general:

* A smaller AWG number means a thicker wire.
* A larger AWG number means a thinner wire.

The appropriate wire size depends on factors such as current, length, temperature, insulation, and installation conditions.

---

# Circuit Protection Devices

Circuit protection devices are designed to interrupt dangerous current conditions.

Common examples include:

* Fuses
* Circuit breakers

Their purpose is to help prevent excessive current from damaging wiring and equipment.

---

# Slow Trips

Some protection devices are designed to tolerate short-duration increases in current.

This can be useful for equipment that naturally draws a larger current when starting.

The exact behavior depends on the protection device and its specifications.

---

# Short Circuits and Fast Trips

A short circuit creates an unintended low-resistance path.

Because resistance is very low, a very large current can potentially flow.

This can rapidly heat wires and damage components.

Circuit protection devices can detect excessive current and disconnect the circuit.

---

# Ground in Electrical Devices

Ground can have different meanings depending on the circuit.

In many electrical systems, a protective ground provides a low-resistance path for fault current so that protection devices can operate.

In electronic circuits, "ground" is also commonly used as a reference point for circuit voltages.

These two uses should not automatically be treated as identical.

---

# Bad Connections

Poor electrical connections can cause problems such as:

* Increased resistance
* Heating
* Intermittent operation
* Voltage drops
* Arcing in some situations

A circuit may appear correct on paper but still fail because of a poor physical connection.

### Example

If a wire terminal is loose, the connection may have higher resistance than intended. Current flowing through that resistance can produce unwanted heating.

---

# Conclusion

Basic circuit design becomes easier when we understand what is happening physically.

A useful progression is:

**Atoms → electric charge → electric field → force on charge → current → resistance → circuits → components → electromagnetic effects → circuit control → safety**

Once these foundations are understood, more advanced topics become easier to study.

Circuit design is not only about memorizing formulas. The goal is to understand **why the circuit behaves the way it does** and then use mathematics and measurements to predict and verify that behavior.

---

# The Next Step

After understanding basic circuits, the next useful topics include:

* Kirchhoff's laws
* Capacitors
* Inductors
* Diodes
* Transistors
* AC circuits
* Digital logic
* Operational amplifiers
* Power supplies
* Microcontrollers

These topics build on the basic ideas of voltage, current, resistance, energy, and electromagnetic behavior.
