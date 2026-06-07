# Data Types and Type Conversion

**Duration:** 30 minutes  **Difficulty:** Beginner  **Track:** Coding + DSA

In this lesson, you will learn about **data types** — how Python handles different kinds of values.
Understanding data types is essential because every value in Python has a specific type, and operations behave differently based on type.

## Learning Objectives

- Understand Python's built-in data types: `str`, `int`, `float`, `bool`
- Learn how to check a variable's type using `type()`
- Practice converting between types using `int()`, `float()`, `str()`
- 5 progressive exercises to test your understanding

## Exercise 1: Explore Data Types

Create variables of four different types: string, integer, float, boolean.
Print each variable and its type.

**Approach:**
1. Create variables: `name = "Student"`, `age = 20`, `score = 92.5`, `is_active = True`
2. Print each along with its type
3. Observe the output

**Solution:**
```python
name = "Student"
age = 20
score = 92.5
is_active = True

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Score: {score} (type: {type(score).__name__})")
print(f"Active: {is_active} (type: {type(is_active).__name__})")
```

### Key Concept
- `str` = text data enclosed in quotes
- `int` = whole numbers
- `float` = decimal numbers
- `bool` = True or False

## Exercise 2: Type Conversion - String to Integer

Read a number from the user as a string, then convert it to an integer and double it.

**Approach:**
1. Use `input()` to get text
2. Convert with `int()`
3. Multiply by 2

**Solution:**
```python
num_str = input("Enter a number: ")
num_int = int(num_str)
num_int = num_int * 2
print(f"Doubled: {num_int}")
```

### Key Concept
`int()` converts compatible strings like `"123"` → `123`. It fails on `"abc"`.

## Exercise 3: Type Conversion - Integer to Float

Take an integer input, convert it to float, divide by 2, and print the result.

**Approach:**
1. Use `int()` to get an integer
2. Convert with `float()`
3. Divide by 2

**Solution:**
```python
num_int = int(input("Enter an integer: "))
num_float = float(num_int)
num_float = num_float / 2
print(f"Half: {num_float}")
```

### Key Concept
`float()` converts integers and string numbers: `float(5)` → `5.0`, `float("3.5")` → `3.5`.

## Exercise 4: Type Conversion - Float to String

Read a float, convert to string, and concatenate with text.

**Approach:**
1. Use `input()` and `float()`
2. Convert back with `str()`
3. Concatenate

**Solution:**
```python
score = float(input("Enter score: "))
score_str = str(score)
print("Your score is: " + score_str + " points")
```

### Key Concept
`str()` converts any type to string: `str(3.14)` → `"3.14"`, `str(True)` → `"True"`.

## Exercise 5: Mixed Type Operations

Calculate the average of two numbers and print a formatted result.

**Approach:**
1. Read two numbers as strings
2. Convert both to floats
3. Calculate average
4. Format and print the result

**Solution:**
```python
n1_str = input("Enter first number: ")
n2_str = input("Enter second number: ")

n1 = float(n1_str)
n2 = float(n2_str)

average = (n1 + n2) / 2

print(f"TThe average of {n1} and {n2} is {average}")
```

### Key Concept
- Mixed operations: adding int + float → float
- Always convert before math operations
- Use f-strings for clean formatting

## Summary

Data types define how Python stores and processes values. Common types:
- `str`: text with quotes
- `int`: whole numbers
- `float`: decimal numbers
- `bool`: True/False

Conversion functions:
- `int("123")` → `123`
- `float("3.14")` → `3.14`
- `str(42)` → `"42"`

## Practice Ideas

- Try `int("3.5")` and observe the error — why does it fail?
- Create a tip calculator: read bill amount, convert to float, calculate 15% tip
- What happens when you `print(10 + "20")`? (Hint: type mismatch!)

---

*Next: Operators and Expressions*
