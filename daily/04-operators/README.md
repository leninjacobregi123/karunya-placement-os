# Operators and Expressions — Day 04

**Duration:** 30 minutes  **Difficulty:** Beginner  **Track:** Coding + DSA

In this lesson, you'll learn about **operators** — the symbols that let you perform calculations on values.
You already know +, -, *, /. Now you'll learn about more operators and how Python handles them.

## What You'll Learn

- Arithmetic operators: +, -, *, /, //, %, and **
- How operator precedence works in Python
- Building complex mathematical expressions
- Practical problems that use these operators

## Operators Quick Reference

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | 5 + 3 | 8 |
| `-` | Subtraction | 10 - 4 | 6 |
| `*` | Multiplication | 7 * 2 | 14 |
| `/` | Division (float) | 15 / 4 | 3.75 |
| `//` | Floor division | 15 // 4 | 3 |
| `%` | Modulus (remainder) | 15 % 4 | 3 |
| `**` | Exponent | 2 ** 3 | 8 |

## Exercise 1: Explore All Arithmetic Operators

Define two variables a = 17 and b = 5. Then use each arithmetic operator on them and print clear results.

**Approach:**
1. Create variables a and b
2. Use each operator one at a time
3. Print with descriptive labels

**Solution:**
```python
a = 17
b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")
```

**Expected output:**
```
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.4
17 // 5 = 3
17 % 5 = 2
17 ** 5 = 1419857
```

### Key Concept
- `/` always returns a float (3.4 not 3)
- `//` returns an int (the quotient)
- `%` returns the remainder
- `**` raises to a power (17^5)

## Exercise 2: Modulo Operator — Classroom Tables

A class has 34 students. Each table seats 6. How many full tables fit, and how many students sit alone at the last table?

**Approach:**
1. Use `//` to find full tables
2. Use `%` to find the remainder
3. Add 1 to full tables if there's a remainder

**Solution:**
```python
students = 34
seats = 6
full = students // seats
rem = students % seats
print(f"Full tables: {full}")
print(f"Remainder students: {rem}")
print(f"Total tables needed: {full + 1 if rem > 0 else full}")
```

**Expected output:**
```
Full tables: 5
Remainder students: 4
Total tables needed: 6
```

### Key Concept
Modulo `%` answers: What's left over after dividing? Common uses: finding remainders, checking even/odd, cycling patterns.

## Exercise 3: Operator Precedence

Calculate this expression: 10 + 20 * 3 - 2 ** 2
First work it out manually using PEMDAS, then verify in Python.

**Approach:**
1. Exponents first: 2 ** 2 = 4
2. Multiplication: 20 * 3 = 60
3. Addition/subtraction left to right: 10 + 60 - 4

**Solution:**
```python
result = 10 + 20 * 3 - 2 ** 2
print(f"Result: {result}")

# Step by step with intermediate results
print(f"2 ** 2 = {2 ** 2}")       # 4
print(f"20 * 3 = {20 * 3}")        # 60
print(f"10 + 60 - 4 = {10 + 60 - 4}")  # 66
```

**Expected output:**
```
Result: 66
```

### Key Concept
Operator precedence in Python:
1. `**` (exponent) 
2. `*`, `/`, `//`, `%` (multiplication/division)
3. `+`, `-` (addition/subtraction)
Use parentheses `()` to override precedence: `(10 + 20) * 3` = 90 instead of 70.

## Exercise 4: Parentheses Override Precedence

Compare `(10 + 20) / (3 * 2)` with `10 + 20 / 3 * 2`

**Approach:**
1. Calculate both expressions
2. Print both results side by side
3. Explain why they differ

**Solution:**
```python
expr1 = (10 + 20) / (3 * 2)
expr2 = 10 + 20 / 3 * 2
print(f"With parentheses: {expr1}")
print(f"Without parentheses: {expr2}")
print(f"Difference: {expr2 - expr1}")
```

**Expected output:**
```
With parentheses: 5.0
Without parentheses: 43.33333...
```

### Key Concept
Parentheses are the most powerful grouping tool—they override ALL precedence rules. Always use them when an expression could be ambiguous.

## Exercise 5: Temperature Converter

Build a Celsius to Fahrenheit converter using the formula: F = C × 9/5 + 32

**Approach:**
1. Define a Celsius temperature
2. Apply the formula
3. Print the result

**Solution:**
```python
celsius = 37
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Test with more values
for c in [0, 100, -40, 37]:
    f = (c * 9 / 5) + 32
    print(f"{c}°C = {f}°F")
```

**Expected output:**
```
37°C = 98.6°F
0°C = 32.0°F
100°C = 212.0°F
-40°C = -40.0°F
```

### Key Concept
- `-40°C = -40°F` — the only temperature where both scales match
- The formula is a standard linear conversion: multiply by 9/5, then add 32
- Parentheses ensure multiplication happens before addition: `(c * 9 / 5) + 32`

## Summary

- Python has 7 arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Floor division `//` gives the quotient (no decimals)
- Modulus `%` gives the remainder — essential for cycles and groups
- Exponent `**` raises to a power
- Operator precedence: `**` > `*`, `/`, `//`, `%` > `+`, `-`
- Parentheses `()` override all precedence — use them liberally!

## Practice Ideas

- Calculate: 100 % 7 (what remainder do you get?)
- What does 2 ** 10 equal? (This is 1024)
- Solve: (15 + 5 * 3) // 8 — do it manually, then check
- Create an expression using at least 4 different operators that equals exactly 6

---

*Next: Input, Output, and String Formatting*