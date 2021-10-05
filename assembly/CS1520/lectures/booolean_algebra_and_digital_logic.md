# Boolean functions
NOT > AND > OR precedence

F(x, y, z) = xz&#773;+y


# Logical circuits
- A logic circuit is composed of:
    - Inputs
    - Outputs
    - Functional specification
    - Timing specification

## The simplicity principle
Digital computers contain circuits that implement Boolean functions.
- The simpler that we can make a Boolean functionn, the smaller the circuit that will result
- Simpler circuits are cheaper to build, consume less power, and run faster than complex circuits.

With this in mind, we always want to reduce our Boolean functions to their simplest form. \
There are several aspects of Boolean algebra that help us to do this.

## Boolean simplification
- Axioms and theorems to simplify Boolean equations.
- Variables have only two values: 1 or 0; true or false
- Duality in axioms and theorems: \
Operators AND and OR, symbols 0 and 1 are interchangable.

## Boolean axioms
0 = false \
1 = true

|   | Axiom |   | Dual | Name |
--- | --- | --- | --- | --- |
A1 | B = 0 if B ≠ 1 | A1' | B = 1 if B ≠ 0 | Binary field
A2 | 0&#773; = 1 | A2' | 1&#773; = 0 | NOT
A3 | 0 · 0 = 0 | A3' | 1 + 1 = 1 | AND/OR
A4 | 1 · 1 = 1 | A4' | 0 + 0 = 0 | AND/OR
A5 | 0 · 1 = 1 · 0 = 0 | A5' | 1 + 0 = 0 + 1 = 1 | AND/OR

## Boolean theorems of one variable
|   | Theorem |   | Dual | Name |
--- | --- | --- | --- | --- |
T1 | B · 1 = B | T1' | B + 0 = B | Identity
T2 | B · 0 = 0 | T2' | B + 1 = 1 | Null Element
T3 | B · B = B | T3' | B + B = B | Idempotency
T4 |   | B&#831; = B |   | Involution
T5 | B · B&#773; = 0 | T5' | B + B&#773; = 1 | AND/OR

