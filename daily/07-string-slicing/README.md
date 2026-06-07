# String Slicing — Day 07

**Duration:** 30 minutes  **Difficulty:** Beginner  **Track:** Coding + DSA

In this lesson, you'll learn about **string slicing** — the art of cutting out
the exact portion of text you need from a longer string. Think of slicing as
using scissors: you decide exactly where to start cutting and where to stop.

## What You'll Learn

- Basic slicing syntax: word[start:end]
- What "exclusive" means for the end index
- Omitted indices and default values
- Negative slicing and stepping through text
- Practical problems involving slicing

## How Slicing Works

Slicing extracts a range of characters. The golden rule: start is inclusive, end is exclusive.

```python
word = "PYTHON"
word[0:2] = "PY"     # starts at 0, stops before 2
word[1:4] = "YTH"    # starts at 1, stops before 4
```

## Exercise 1: Basic Slicing

Create word = "COMPUTER" and slice it to extract different portions.

**Approach:**
1. Define the string
2. Use word[a:b] to slice
3. Print each with a descriptive label

**Solution:**
```python
word = "COMPUTER"

print(f"First 3:  {word[0:3]}")      # "COM"
print(f"Next 3:   {word[3:6]}")      # "PUT"
print(f"Last 2:   {word[7:9]}")      # "ER"
print(f"Middle:   {word[2:6]}")      # "MPUTE"
print(f"Skipped:  {word[0:7:2]}")    # "CMUT" (every 2nd)
```

**Expected output:**
```
First 3:  COM
Next 3:   PUT
Last 2:   ER
Middle:   MPUTE
Skipped:  CMUT
```

### Key Concept
- word[a:b] extracts from index a (inclusive) up to index b (exclusive)
- word[0:3] gives indices 0, 1, 2 (stops BEFORE 3)
- The length of a slice is always b - a (when both indices are positive)

## Exercise 2: Omitted Indices and Defaults

Use omitted indices to extract: first half, last half, full reversal, and a copy.

**Approach:**
1. Use word[:n] for first n characters
2. Use word[n:] for characters from index n onward
3. Use word[::step] for stepping through characters

**Solution:**
```python
word = "PYTHONPROGRAMMING"

# Omitted start = 0
first_5 = word[:5]
print(f"First 5: {first_5}")           # "PYTHON"

# Omitted end = len(word)
last_5 = word[-5:]
print(f"Last 5: {last_5}")             # "RAMMING"

# Omitted both = copy
copy = word[:]
print(f"Copy = word: {copy == word}")  # True

# Reverse using step
reversed_word = word[::-1]
print(f"Reverse: {reversed_word}")     # "GNNIMARGMARNO"
```

### Key Concept
- word[:n] = word[0:n] (from start to index n)
- word[n:] = word[n:len(word)] (from index n to end)
- word[:] = word[0:len(word)] (a full copy)
- word[::2] = word[0::2] = every second character
- word[::-1] = word[5:-6:-1] in some sense = entire string reversed

## Exercise 3: Slicing with Step

Extract vowels from a string using slicing with a step parameter.

**Approach:**
1. Create a string
2. Use [start:end:step] to extract characters at intervals
3. Demonstrate both positive and negative steps

**Solution:**
```python
word = "INFORMATION"

# Get every 3rd character
every_3rd = word[::3]
print(f"Every 3rd: {every_3rd}")       # "IORM"

# Get every 2nd character starting from index 2
every_2nd_from_2 = word[2::2]
print(f"Every 2nd from index 2: {every_2nd_from_2}")  # "FM"

# Reverse using step -1
reversed_word = word[::-1]
print(f"Reverse: {reversed_word}")     # "NOITAMROFNI"

# Reverse but skip every character: take every other from reverse
reversed_skip = word[::-2]
print(f"Reversed (skip 1): {reversed_skip}")  # "NMOFRI"
```

### Key Concept
- word[start:end:step]: default start=0 (for positive step) or end-1 (for negative)
- Default end=len(word) (for positive step) or -1 (for negative)
- Positive step = left to right
- Negative step = right to left
- word[a:b:-1] = from a going backwards until just before b

## Exercise 4: Practical — Extract Name from "Last, First" Format

Given a string "Sharma,Amit", extract the last name and first name using slicing.

**Approach:**
1. Get the combined string
2. Find the comma position
3. Slice before and after the comma

**Solution:**
```python
name = "Sharma,Amit"

# Find the comma position
comma_pos = name.find(',')

if comma_pos != -1:
    last_name = name[:comma_pos].strip()
    first_name = name[comma_pos+1:].strip()
    
    print(f"Last name:  {last_name}")
    print(f"First name: {first_name}")
    
    # Reconstruct as "First Last"
    print(f"Reformatted: {first_name} {last_name}")
else:
    print("No comma found — format should be 'Last,First'")
```

**Expected output:**
```
Last name:  Sharma
First name: Amit
Reformatted: Amit Sharma
```

### Key Concept
- .find(',') returns the position of the comma (-1 if not found)
- name[:comma_pos] extracts everything before it
- name[comma_pos+1:] extracts everything after it
- .strip() removes whitespace from both ends

## Exercise 5: Practical — Extract Date Components

Given a date string "2026-06-15" (YYYY-MM-DD format), extract year, month, and day using slicing.

**Approach:**
1. Define the date string
2. Use slicing with fixed positions (YYYY is always positions 0-4)
3. Convert components to integers

**Solution:**
```python
date_str = "2026-06-15"

year = date_str[0:4]
month = date_str[5:7]
day = date_str[8:10]

print(f"Year:  {int(year):>4d}")    # Right-align in 4-wide field
print(f"Month: {int(month):>2d}")   # Right-align in 2-wide field
print(f"Day:   {int(day):>2d}")     # Right-align in 2-wide field

# Verify by reconstructing
reconstructed = f"{year}-{month}-{day}"
print(f"Matches? {reconstructed == date_str}")
```

**Expected output:**
```
Year:   2026
Month:    6
Day:    15
Matches? True
```

### Key Concept
- Fixed-width formats (YYYY-MM-DD, SS:MM:HH) can always be sliced by position
- int(str) converts back to a number for calculations
- f-strings with formatting: f"{value:>4d}" right-aligns in a 4-character space

## Summary

- word[start:end] = substring from start (inclusive) to end (exclusive)
- word[:n] = first n characters; word[n:] = last len(word)-n characters
- word[::step] = stepping through; word[::-1] = reverse
- Always use .find() or len() first when the slice point is dynamic
- For fixed-width formats, slicing by position is reliable (YYYY-MM-DD is always positions 0, 5, 8)

## Practice Ideas

- Extract the TLD (top-level domain) like "com" from "www.example.com" using slicing
- What does word[len(word):len(word)] return? Try it — it gives an empty string, not an error!
- Slice a string in reverse groups of 3: "HELLOWORLD" -> "WORLDHLEL"
- Read any text input and reverse only the last 10 characters

---

*Next: String Methods — built-in techniques for manipulating strings*
