# String Fundamentals — Day 05

**Duration:** 30 minutes  **Difficulty:** Beginner  **Track:** Coding + DSA

In this lesson, you'll explore **strings** — the Python data type used to store text.
Strings are everywhere: names, addresses, messages, file paths, URLs. Understanding them is essential for every Python program.

## What You'll Learn

- Creating strings with single, double, or triple quotes
- String escaping and special characters
- Basic string operations: length, joining, repeating
- The difference between str type and number types
- Practice problems that build from basics to practical applications

## Creating Strings

Strings in Python are created by wrapping text in quotes. Python treats single quotes `'hello'` and double quotes `"hello"` identically — the difference comes when you need to include a quote inside the string.

```python
# Single quotes for simple strings
name = 'Student One'

# Double quotes when the string contains an apostrophe
msg = "It's a beautiful day"

# Triple quotes for strings that span multiple lines
poem = '''First line
Second line
Third line'''
```

## Exercise 1: Create and Display Strings

Create three strings using different quote styles, then print each with an explanation.

**Approach:**
1. Create one string with single quotes (no special characters)
2. Create one string with double quotes (contains an apostrophe)
3. Create one string with triple quotes (contains both types of quotes)
4. Print each one with a label

**Solution:**
```python
# Single quotes — no internal quotes needed
first_name = 'Amit'
print(f"Name: {first_name}")

# Double quotes — string contains an apostrophe
message = "Don't worry about the exam"
print(f"Message: {message}")

# Triple double quotes — string contains both types
quote = """He said, "It's simple" — and she agreed"""
print(f'Quote: {quote}')
```

**Expected output:**
```
Name: Amit
Message: Don't worry about the exam
Quote: He said, "It's simple" — and she agreed
```

### Key Concept
Use single quotes when your string doesn't contain a single quote. Use double quotes when it contains a single quote. Use triple quotes when the string needs internal quotes of both types.

## Exercise 2: String Length

Write a program that reads a user's name and prints how many characters it contains. Then print the first character, last character, and whether the length is even or odd.

**Approach:**
1. Get input from the user
2. Use `len()` to find the length
3. Access the first character with `[0]` and the last with `[-1]`
4. Use `%` to check even/odd

**Solution:**
```python
name = input("Enter your name: ")
length = len(name)
print(f"Name: {name}")
print(f"Length: {length} characters")
print(f"First character: {name[0]}")
print(f"Last character: {name[-1]}")
print(f"Length is {'even' if length % 2 == 0 else 'odd'}")
```

**Expected output (for "Amit"):**
```
Name: Amit
Length: 4 characters
First character: A
Last character: t
Length is even
```

### Key Concept
- `len(string)` returns the number of characters
- Index `[0]` gives the first character
- Index `[-1]` gives the last character (counting backwards in Python)
- Index `[-2]` gives the second-to-last character

## Exercise 3: String Concatenation and Repetition

Create a program that builds a pattern line using string repetition, then combines two student names with a separator.

**Approach:**
1. Use `*` to repeat a character into a line
2. Use `+` to join two strings
3. Use `*` to repeat a string pattern

**Solution:**
```python
# Repeat a character to make a line of equal length
name = "Student One"
underline = "-" * len(name)
print(f"Name: {name}")
print(f"Underline: {underline}")

# Join two names with different separators
first = "Priya"
last = "Sharma"
print(f"Full name (space): {first + ' ' + last}")
print(f"Full name (dot): {first + '.' + last}")
print(f"Full name (underscore): {first + '_' + last}")

# Repeat a short string
print("Ha! " * 3)  # "Ha! Ha! Ha! "
```

**Expected output:**
```
Name: Student One
Underline: ------------
Full name (space): Priya Sharma
Full name (dot): Priya.Sharma
Full name (underscore): Priya_Sharma
Ho! Ho! Ho!
```

### Key Concept
- `str + str` concatenates (joins) strings
- `str * n` repeats the string n times
- `" " * 5` gives `"     "` — a 5-space string
- Be careful: you cannot add `(+)` a string with an int directly — convert first

## Exercise 4: String Escape Characters

Demonstrate how to include special characters in strings using escape sequences.

**Approach:**
1. Create strings containing newlines, tabs, quotes, and backslashes
2. Print each one and observe the output

**Solution:**
```python
# Newline (\n)
story = "Once upon a time\nIn a land far away\nThey lived happily ever after."
print("Story with newlines:")
print(story)
print("---")

# Tab (\t)
table_row = "Name\tAge\tCity"
print(f"Table: {table_row}")
print("   " + "Alice\t25\tMumbai")
print("   " + "Bob\t30\tDelhi")
print("---")

# Escaped quotes
single_quote = 'She said \'hello\''
double_quote = "He said \"bye\""
backslash = "Path: C:\\Users\\Admin\\file.txt"
print(single_quote)
print(double_quote)
print(backslash)
```

**Expected output:**
```
Story with newlines:
Once upon a time
In a land far away
They lived happily ever after.
---
Table: Name	Age	City
   Alice	25	Mumbai
   Bob	30	Delhi
---
She said 'hello'
He said "bye"
Path: C:\Users\Admin\file.txt
```

### Key Concept
Backslash `\` is the escape character in Python strings:
- `\n` = newline
- `\t` = tab
- `\'` = literal single quote
- `\"` = literal double quote
- `\\` = literal backslash

## Exercise 5: Practical Application — Student ID Generator

Create a program that generates a student ID based on their name and department.

**Approach:**
1. Get the student's name and department
2. Extract the first 3 letters of the name
3. Add the last 2 letters of the department
4. Combine with the current year

**Solution:**
```python
name = input("Enter your name: ")        # e.g., "Aarav"
dept = input("Enter your department: ")   # e.g., "CSE"
year = "2026"

# Extract first 3 characters of name
initials = name[0:3].upper()

# Extract last 2 characters of department
dept_code = dept[-2:].upper()

# Generate the ID
student_id = f"{dept_code}{year}{initials}"
print(f"Your student ID: {student_id}")
```

**Expected output (for "Aarav" and "CSE"):**
```
Your student ID: SEC2026AAR
```

### Key Concept
- String slicing `name[0:3]` extracts characters from index 0 up to (but not including) index 3
- `.upper()` converts to uppercase (a string method you'll learn in detail next)
- Combining pieces of strings with `+` is how you build structured data like IDs
- f-strings (covered in the next lesson) are the cleaner way to do this

## Summary

- Strings store text: use `'single'`, `"double"`, or `'''triple'''` quotes
- `len(string)` gives the length in characters
- `+` joins strings (concatenation)
- `*` repeats strings (e.g., `"-" * 10`)
- `[0]` = first character, `[-1]` = last character
- Escape characters (`\n`, `\t`, `\\`, etc.) let you include special characters
- String slicing `string[a:b]` extracts a substring

## Practice Ideas

- Print your own name in reverse order using indexing
- What happens if you try `"Hello" + 5`? (Try it — it will crash. How would you fix it?)
- Create a pattern that looks like a staircase using string repetition
- Read any string from the user and check: is it a palindrome? (reads the same backwards)

---

*Next: String Indexing (Day 06) — deeper look at accessing individual characters*