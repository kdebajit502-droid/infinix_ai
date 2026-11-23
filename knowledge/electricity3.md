# How Computers Work: From Electricity to Microprocessors

## 1. Why Understanding Computers Matters

Computers are now part of everyday life. Phones, cars, machines, websites, industrial equipment, and many other systems depend on computers.

A computer may look complicated from the outside, but its basic operation can be understood by starting with something very simple:

**Electrical signals.**

At the lowest level, computers work with electrical states that can be represented as two conditions:

* **High / Low**
* **On / Off**
* **1 / 0**

By combining enormous numbers of these simple states, computers can perform complicated operations.

---

# 2. Starting With a Simple Circuit

Imagine a battery, a light bulb, and two switches.

### Switches in series

Suppose the switches are connected in series:

```text
Battery → Switch A → Switch B → Light → Battery
```

For current to reach the light, **both switches must be closed**.

| Switch A | Switch B | Light |
| -------- | -------- | ----- |
| OFF      | OFF      | OFF   |
| ON       | OFF      | OFF   |
| OFF      | ON       | OFF   |
| ON       | ON       | ON    |

This behavior is called **AND logic**.

The light turns on only when:

> A AND B are ON.

### Switches in parallel

Now connect the switches in parallel:

```text
             ┌── Switch A ──┐
Battery ─────┤              ├── Light
             └── Switch B ──┘
```

Now either switch can complete a path for current.

| Switch A | Switch B | Light |
| -------- | -------- | ----- |
| OFF      | OFF      | OFF   |
| ON       | OFF      | ON    |
| OFF      | ON       | ON    |
| ON       | ON       | ON    |

This is **OR logic**.

The light turns on when:

> A OR B is ON.

These tables are called **truth tables**.

A truth table describes what output a system produces for every possible combination of inputs.

---

# 3. From Manual Switches to Logic Gates

A person can physically operate a switch, but computers need a way to control switches automatically.

One early solution was the **relay**.

A relay uses an electrical signal to control another electrical circuit.

For example:

```text
Small control signal
        ↓
      Relay
        ↓
Large circuit ON/OFF
```

This allowed one electrical signal to control another circuit.

Instead of a person physically pressing a button, another electrical circuit could provide the signal.

This is an important idea behind digital electronics:

> An electrical signal can represent information.

---

# 4. What Is a Bit?

A system with two possible states can represent one **bit** of information.

For example:

```text
0 = OFF
1 = ON
```

A bit can also be represented physically by different electrical conditions.

For example:

```text
0 → low voltage
1 → high voltage
```

The exact voltages depend on the electronic technology. They are not universally 0 V and 5 V.

A single bit is very small, but many bits can be combined to represent numbers, text, instructions, images, and other information.

---

# 5. Logic Gates

A **logic gate** is a circuit that produces an output based on one or more inputs.

Common logic gates include:

* AND
* OR
* NOT
* XOR
* NAND
* NOR

### AND gate

The output is 1 only when both inputs are 1.

```text
A = 1
B = 1

Output = 1
```

### OR gate

The output is 1 when at least one input is 1.

```text
A = 1
B = 0

Output = 1
```

### NOT gate

A NOT gate reverses the input.

```text
Input  = 1
Output = 0
```

Logic gates are extremely important because they allow simple electrical states to be combined into useful operations.

---

# 6. Vacuum Tubes

Early electronic computers used **vacuum tubes** to control electrical signals.

A vacuum tube can control the flow of electrons through a vacuum.

One important process is called **thermionic emission**.

When a suitable electrode is heated, electrons can be emitted from its surface.

A positively charged electrode can attract those electrons.

This allows current to flow through the tube.

A vacuum tube can therefore be used to control electrical signals and perform switching operations.

### Controlling the electrons

A vacuum tube can also contain a control grid.

Changing the electrical condition of the grid changes how easily electrons move through the tube.

This makes the vacuum tube useful as an electronic switch or amplifier.

---

# 7. Why Vacuum Tubes Were Replaced

Vacuum tubes had an important advantage over mechanical relays:

**They had no moving mechanical parts.**

A relay physically moves a mechanical component.

That movement limits how quickly it can switch.

A vacuum tube can switch much faster.

However, vacuum tubes had serious disadvantages:

* They were large.
* They consumed significant power.
* They produced considerable heat.
* They were less convenient to maintain.
* Large computers required enormous numbers of them.

Early computers could therefore occupy entire rooms.

The basic idea worked, but engineers needed something much smaller and more efficient.

That led to the **transistor**.

---

# 8. The Transistor

The transistor was one of the most important inventions in electronics.

It allowed engineers to create electronic switches that were:

* Much smaller
* More efficient
* Very fast
* More reliable
* Easier to manufacture in large numbers

Modern processors contain enormous numbers of transistors.

A transistor can be used to control whether electrical current can flow.

This makes it possible to construct logic gates from transistors.

Logic gates can then be combined into larger circuits.

---

# 9. Silicon

A large part of modern electronics is based on **silicon**.

Silicon has four valence electrons.

In a pure silicon crystal, silicon atoms form a structured lattice in which electrons participate in bonds.

Pure silicon is a **semiconductor**, not simply a perfect insulator.

Its electrical behavior can be changed by adding small amounts of other elements. This process is called **doping**.

---

# 10. N-Type Silicon

Suppose silicon is doped with phosphorus.

Phosphorus has five valence electrons.

Four can participate in bonding with neighboring silicon atoms, leaving an additional electron that can contribute to electrical conduction.

This produces **n-type semiconductor material**.

The main charge carriers are electrons.

```text
Silicon + phosphorus
        ↓
Extra available electrons
        ↓
N-type material
```

---

# 11. P-Type Silicon

Now consider doping silicon with boron.

Boron has three valence electrons.

This creates an absence of an electron in the bonding structure.

We represent this absence as a **hole**.

A hole behaves as an effective positive charge carrier.

This produces **p-type semiconductor material**.

```text
Silicon + boron
        ↓
Electron holes
        ↓
P-type material
```

The important idea is:

> N-type material mainly uses electrons as charge carriers, while p-type material mainly uses holes as effective charge carriers.

---

# 12. The PN Junction

When p-type and n-type semiconductor materials are joined, a **PN junction** is formed.

Near the junction, electrons and holes interact and recombine.

This creates a region with very few mobile charge carriers called the **depletion region**.

The depletion region acts as a barrier to charge movement.

The behavior of this junction depends on how an external voltage is applied.

This is the basic principle behind a **diode**.

---

# 13. How a Diode Works

A diode is designed to allow current to flow much more easily in one direction than the other.

When the PN
