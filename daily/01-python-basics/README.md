# Python Basics — Day 01

**Duration:** 30 minutes  **Difficulty:** Beginner  **Tracks:** coding

## What This Lesson Covers

In this first lesson, you'll learn the most fundamental building blocks of Python — how to display information, collect user input, and understand data types. These are the basics you'll use every single time you write Python code.

This lesson includes:
- Displaying text to the screen using `print()`.
- Collecting input from the user with `input()`.
- Understanding Python's core data types: `str`, `int`, `float`, and `bool`.
- Using `type()` to verify what kind of data a value holds.

## What to Expect Before Starting

You should know how to open a terminal and run Python code. If you have never written Python before, this lesson is designed for complete beginners. You will build five small, progressive exercises that start with the simplest possible code and grow in complexity.

Each exercise comes with:
- A clear description of what to do.
- A reference code block you can study.
- The expected output so you can verify your work.
- A key concept that tells you the most important rule to remember.

## What You'll Build

Five exercises that take you from "Hello World" to reading user input.

---

## Exercise 1 — Hello World

Write Python code that prints:

```
Hello, World!
```

**Type this exactly:**
```python
print("Hello, World!")
```

**Expected output:**
```
Hello, World!
```

**Key Concept:** `print()` is a Python function. Its job is to send output to the screen. Everything inside the parentheses becomes what the user sees. Use double quotes, single quotes, or a mix — just be sure they match (open with `"` and close with `"`).

---

## Exercise 2 — Your Name

Ask the user for their name using `input()` and print a greeting.

**Code:**
```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

**Expected output:** (if user types Alice)
```
What is your name? Alice
Hello, Alice!
```

**Key Concept:** `input()` pauses the program and waits for the user to type something. Whatever the user types is stored as a **string** (text), even if they type numbers. `+` joins strings together — this is called *concatenation*.

---

## Exercise 3 — Numbers

Print the sum of two numbers.

**Code:**
```python
a = 10
b = 25
print("Sum:", a + b)
```

**Expected output:**
```
Sum: 35
```

**Key Concept:** Variables (`a`, `b`) store values so you can reuse them. Numbers without quotes are treated as numeric values and support math: `a + b = 35`, `a - b = -15`, `a * b = 250`, etc.

---

## Exercise 4 — Type Check

Print the data type of a variable.

**Code:**
```python
age = 25
print(type(age))
```

**Expected output:**
```
<class 'int'>
```

**Key Concept:** `type()` tells you what kind of data a variable holds. Python's core types are:
- `str` (string): text like `"hello"`.
- `int` (integer): whole numbers like `25`.
- `float` (floating point): decimal numbers like `3.14`.
- `bool`: `True` or `False`.

---

## Exercise 5 — Mixed Input

Read age from the user, then print its type. Notice the output.

**Code:**
```python
age = input("Enter your age: ")
print("Type:", type(age))
```

**Expected output:** (if user types 25)
```
Enter your age: 25
Type: <class 'str'>
```

**Key Concept:** This is the most important lesson in this exercise: **`input()` always returns a string**, even if the user types a number. To use the value as a number, you must convert it: `int(age)`. This is a common beginner pitfall — always remember to convert when needed.

---

## Summary

- `print()` displays text or values to the screen.
- `input()` reads text from the user. It always returns a string.
- `type()` shows what kind of data a value is.
- Every variable in Python has exactly one type, and it is set when the variable is created.
- `+` can add numbers AND join strings — depending on what the inputs are.
- Converting types: `int("25")` → `25`, `str(25)` → `"25"`.

## Practice Ideas

- Write a program that prints your full name on one line, then prints its total character count.
- Try: `age = input("Enter age: ")` and then `print(age * 3)` — what happens and why?
- Experiment with `float("3.14")` and `str(3.14)` to see type conversion in action.
- Write a program that collects a person's name, age, and city, then greets them back with all three.

---

*Next: Variables & Data Types (Day 02) — Deepen your understanding of Python's core data model*
