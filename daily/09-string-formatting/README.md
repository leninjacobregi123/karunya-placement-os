# String Formatting — Day 09

**Duration:** 30 minutes  **Difficulty:** Beginner  **Track:** Coding + DSA

In this lesson, you'll learn about **string formatting** — how to build clean, readable
output with variables and computed values. Instead of awkward concatenation with `+`,
you'll learn Python's cleaner and more powerful formatting techniques.

## What You'll Learn

- f-strings (formatted string literals) — the recommended approach
- str.format() — the older but still useful approach
- How to pad, align, and format numbers
- Building multi-line reports with consistent column widths
- Practical problems combining formatting with real data display

## Method 1: f-Strings (Formatted String Literals)

f-strings are the most Pythonic way to format strings. Prefix a string with `f` and put
expressions inside curly braces `{}`:

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 25 years old.
```

## Exercise 1: Basic f-Strings

Create variables for student information and display them using f-strings.

**Approach:**
1. Create variables: name, age, grade, city
2. Use f-strings to insert values into text
3. Display them in different formats

**Solution:**
```python
name = "Priya Sharma"
age = 20
grade = "A"
city = "Mumbai"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Grade: {grade}")
print(f"City: {city}")

# Combine them into a single formatted string
print(f"\nStudent: {name}")
print(f"Age: {age}, Grade: {grade}, City: {city}")
print(f"This semester, {name} got a {grade} and lives in {city}.")
```

**Expected output:**
```
Name: Priya Sharma
Age: 20
Grade: A
City: Mumbai

Student: Priya Sharma
Age: 20, Grade: A, City: Mumbai
This semester, Priya Sharma got a A and lives in Mumbai.
```

### Key Concept
- f-strings evaluate Python expressions inside `{}` — not just variable names!
- You can call methods: `f"Name: {name.upper()}"`
- You can do math: `f"Next year: {age + 1}"`
- You can use conditions: `f"Status: {'PASS' if grade >= 'B' else 'FAIL'}"`

## Exercise 2: Format Numbers with f-strings

Display prices, scores, and percentages with consistent decimal places.

**Approach:**
1. Use `:.nf` for n decimal places
2. Use `:>n` for right alignment (padding with spaces)
3. Use `:<n` for left alignment

**Solution:**
```python
# Decimal places
pi = 3.14159265
print(f"Pi rounded to 2: {pi:.2f}")    # 3.14
print(f"Pi rounded to 4: {pi:.4f}")    # 3.1416
print(f"Pi rounded to 8: {pi:.8f}")    # 3.14159265

# Right alignment with padding
print(f"\nRight-aligned (10 chars): '{pi:>10.2f}'")
print(f"Right-aligned (15 chars): '{pi:>15.2f}'")

# Left alignment
print(f"Left-aligned (10 chars): '{pi:<10.2f}'")

# Zero padding for integers
print(f"\nZero-padded: {42:>08d}")       # 00000042
print(f"Zero-padded: {7:>05d}")          # 00007
```

**Expected output:**
```
Pi rounded to 2: 3.14
Pi rounded to 4: 3.1416
Pi rounded to 8: 3.14159265

Right-aligned (10 chars): '      3.14'
Right-aligned (15 chars): '          3.14'
Left-aligned (10 chars): '3.14        '

Zero-padded: 00000042
Zero-padded: 00007
```

### Key Concept
- `:.nf` = n decimal places (rounding happens automatically)
- `:>n` = right-align in n characters (pads with spaces on the left)
- `:<n` = left-align in n characters (pads with spaces on the right)
- `:0n` = zero-pad (for integers): `{:08d}` gives 8 digits with leading zeros

## Exercise 3: Build a Formatted Report

Create a student report card with aligned columns for name, marks, and grade.

**Approach:**
1. Prepare data as a list of tuples or dictionaries
2. Use f-strings with consistent column widths
3. Print a header line, separator, then each row

**Solution:**
```python
students = [
    ("Alice", 92.5, "A"),
    ("Bob", 87.3, "B+"),
    ("Charlie", 78.9, "B"),
    ("Diana", 45.2, "F"),
    ("Eve", 63.1, "C")
]

# Header
print(f"{'Name':<12} {'Marks':>7} {'Grade':>5} {'Status':<8}")
print("-" * 35)

for name, marks, grade in students:
    status = "PASS" if marks >= 50 else "FAIL"
    print(f"{name:<12} {marks:>7.1f} {grade:>5} {status:<8}")
```

**Expected output:**
```
Name         Marks    Grade Status  
-----------------------------------
Alice          92.5      A PASS    
Bob            87.3     B+ PASS    
Charlie        78.9      B PASS    
Diana          45.2      F FAIL    
Eve            63.1      C PASS    
```

### Key Concept
- `:<12` = left-align name in 12 characters
- `:>7.1f` = right-align number in 7 characters with 1 decimal
- `"-" * 35` = repeat the dash 35 times to make a line
- Keep column widths consistent for a clean report

## Exercise 4: Percentage Calculator with Formatted Output

Build a program that reads marks obtained and total marks, then displays the percentage.

**Approach:**
1. Read two numbers from the user
2. Calculate the percentage
3. Display with different formatting options

**Solution:**
```python
obtained = float(input("Marks obtained: "))
total = float(input("Total marks: "))
percentage = (obtained / total) * 100

# Display in multiple ways
print(f"\n--- Results ---")
print(f"Percentage: {percentage}%")
print(f"Percentage: {percentage:.1f}%")
print(f"Percentage: {percentage:6.2f}%")
print(f"Percentage: {percentage:>10.1f}%")

# Bar visualization
print(f"\nScore bar: {'#' * int(percentage // 5)}{'.' * (20 - int(percentage // 5))}")
```

**Expected output (for 45/100):**
```
--- Results ---
Percentage: 45.0%
Percentage: 45.0%
Percentage:  45.00%
Percentage:       45.0%

Score bar: ###########.............
```

### Key Concept
- You can combine expressions with formatting: `{percentage:6.2f}%`
- `int(percentage // 5)` converts to an integer for the bar length
- `'%' * count` repeats the bar character
- Formatting with `:.1f` rounds and shows exactly 1 decimal place

## Exercise 5: Temperature Converter with Formatting

Build a program that converts between Celsius and Fahrenheit with formatted output.

**Approach:**
1. Read a temperature value and the input scale
2. Apply the conversion formula
3. Display results with consistent formatting

**Solution:**
```python
celsius = float(input("Enter temperature in Celsius: "))

# Conversions
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

# Display in a nice table
print(f"\n{'Temperature':<20} {'Celsius':>10} {'Fahrenheit':>12} {'Kelvin':>10}")
print("-" * 55)
print(f"{'Input':<20} {celsius:>10.1f} {fahrenheit:>12.1f} {kelvin:>10.1f}")

# Special case: -40°C = -40°F (the one point where they match)
c_special = -40
f_special = (c_special * 9 / 5) + 32
print(f"\nFun fact: {c_special}°C = {f_special}°F (they match!)")

# Table of common temperatures
print(f"\n{'C':>6} {'F':>10}")
print("-" * 18)
for c in [0, 100, -40, -273.15]:
    f = (c * 9 / 5) + 32
    print(f"{c:>6.1f} {f:>10.1f}")
```

**Expected output:**
```
Enter temperature in Celsius: 37

Temperature              Celsius   Fahrenheit    Kelvin
-------------------------------------------------------
Input                     37.0       98.6        310.2

Fun fact: -40°C = -40.0°F (they match!)

     C       F
------------------
   0.0      32.0
 100.0     212.0
 -40.0     -40.0
-273.2    -459.7
```

### Key Concept
- Formatting makes data presentation clean and readable
- Column widths should accommodate the longest value in that column
- Use `.1f` or `.2f` for decimals — always show the same number of places
- Table formatting with fixed widths is a powerful visualization technique

## Summary

- f-strings `f"text {variable}"` are the recommended way to format strings
- `:.nf` controls decimal places (e.g., `{pi:.2f}` = 3.14)
- `:>n` right-aligns; `:<n` left-aligns; `:^n` centers
- For integers: `{:08d}` zero-pads to 8 digits
- Consistent column widths make reports readable
- You can embed any Python expression inside f-string braces

## Practice Ideas

- Format a bank statement showing deposits, withdrawals, and balance
- Print a multiplication table with aligned columns
- What does `f"{3.14159:>15.10f}"` produce? Try it.
- Build a BMI calculator that displays the result with formatted text and a color status indicator

---

*Next: String Practice Problems — apply everything you've learned in practical exercises*
