# Variables and Data Types — Day 02

**Duration:** 30 minutes  **Difficulty:** Beginner  **Track:** Coding + DSA

In this lesson, you will learn about **variables** — how to store data in Python.
Variables are named containers that hold values. Python makes this easy by
detecting the type automatically.

## What You'll Learn

- Naming variables correctly
- Data types: str, int, float, bool
- Printing multiple values
- Type conversions
- Practice problems with progressive difficulty

## Exercise 1: Create Variables

Assign your name to a variable called `name` and your age to a variable called
`age`. Then print them both.

**Approach:**
1. Create `name = "Your Name"`
2. Create `age = 20`
3. Print both on one line

**Solution:**
```python
name = "Alice"
age = 20
print(name, age)
```

### Key Concept
Variables store values. Use descriptive names: `student_name` not `x1`.

## Exercise 2: Data Types

Create variables for a student's name (string), roll number (integer),
and percentage (float). Print each with its type.

**Approach:**
1. Create each variable with the right type
2. Use `type()` to show each one

**Solution:**
```python
name = "Bob"
roll = 101
percentage = 92.5
print(type(name), type(roll), type(percentage))
```

### Key Concept
Python assigns the type automatically: `"text"` is str, `123` is int, `3.14` is float.

## Exercise 3: Type Conversion

Read a number as a string, then convert it to integer and float.

**Approach:**
1. Use `input()` to get a number
2. Convert with `int()` and `float()`
3. Print all three values

**Solution:**
```python
num_str = input("Enter a number: ")
num_int = int(num_str)
num_float = float(num_str)
print("String:", num_str)
print("Int:", num_int)
print("Float:", num_float)
```

### Key Concept
`int("25")` → 25, `float("25")` → 25.0, `str(25)` → "25". Conversion only works when the value IS compatible.

## Exercise 4: Boolean Logic

Create boolean variables for conditions. Print their types.

**Approach:**
1. Create `is_passed = True`, `is_active = False`
2. Print the values and their types

**Solution:**
```python
is_passed = True
is_active = False
print(is_passed, type(is_passed))
print(is_active, type(is_active))
```

### Key Concept
Boolean values are `True` or `False` (capital T and F in Python). They represent logical states.

## Exercise 5: Mixed Output

Print a formatted sentence using variables of different types.

**Approach:**
1. Create variables of different types
2. Use `str()` to convert non-strings
3. Concatenate with `+` and `print()`

**Solution:**
```python
name = "Charlie"
age = 22
marks = 88.5
print(name + " is " + str(age) + " years old with " + str(marks) + " marks")
```

### Key Concept
Only strings can be concatenated with `+`. Convert other types with `str()` first.

## Summary

- Variables store data with automatic type detection
- `str` = text, `int` = whole numbers, `float` = decimals, `bool` = True/False
- Use `int()`, `float()`, `str()` for type conversion
- Use `type()` to verify what a variable holds
- Always use descriptive names: camelCase or snake_case

## Practice Ideas

- Store your full details (name, age, city, grade) and print them
- Convert between int and string: what happens with `int("hello")`? Try it.
- Explore: what does `type(True)` return vs `type(true)`? (Hint: capitalization matters!)

---

*Next: Operators and Expressions (Day 03)*