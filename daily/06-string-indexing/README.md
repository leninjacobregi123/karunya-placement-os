# String Indexing — Day 06

**Duration:** 30 minutes  **Difficulty:** Beginner  **Track:** Coding + DSA

In this lesson, you'll learn about **string indexing** — how to access individual characters
within a string. Think of a string as a row of boxes, each holding one character.
Indexing is how you open the right box.

## What You'll Learn

- Positive indexing: accessing characters from the front (0, 1, 2...)
- Negative indexing: accessing characters from the back (-1, -2, -3...)
- Index out of bounds errors and how to avoid them
- Combining indexing with len() for safe access
- Practical problems using character access

## How Indexing Works

Every character in a string has a position called its index. Python uses **zero-based** indexing,
meaning the first character is at index 0, not 1.

```
word = "PYTHON"
index:  0  1  2  3  4  5
char:   P  Y  T  H  O  N
         -6 -5 -4 -3 -2 -1  (negative)
```

## Exercise 1: Explore Positive Indexing

Create a string called `word = "PYTHON"` and print the character at each index (0 through 5).

**Approach:**
1. Create the string variable
2. Access each character by its index
3. Print each result with a label

**Solution:**
```python
word = "PYTHON"
print(f"Index 0: {word[0]}")
print(f"Index 1: {word[1]}")
print(f"Index 2: {word[2]}")
print(f"Index 3: {word[3]}")
print(f"Index 4: {word[4]}")
print(f"Index 5: {word[5]}")

print("--- Looping ---")
for i in range(len(word)):
    print(f"word[{i}] = {word[i]}")
```

**Expected output:**
```
Index 0: P
Index 1: Y
Index 2: T
Index 3: H
Index 4: O
Index 5: N
--- Looping ---
word[0] = P
word[1] = Y
...
```

### Key Concept
- Index starts at 0, not 1
- `len(word)` tells you how many characters there are
- The last index is always `len(word) - 1`
- You cannot access `word[6]` because there are only 6 characters (indices 0 to 5)

## Exercise 2: Negative Indexing

Use negative indexing to access characters from the end of the string `"ALGORITHM"`.
Print the last 3 characters and the first 2 characters using negative indices.

**Approach:**
1. Create the string
2. Use -1 for the last char, -2 for the second-to-last, etc.
3. Combine with positive indexing to show both directions

**Solution:**
```python
word = "ALGORITHM"

print(f"First char (positive): {word[0]}")
print(f"Last char (negative):  {word[-1]}")
print(f"Second char (positive): {word[1]}")
print(f"Last-2 (negative):    {word[-2]}")
print(f"Last-3 (negative):    {word[-3]}")
print(f"Middle char: {word[len(word)//2]}")

print("--- All negative indices ---")
print(f"word[-1] = {word[-1]}")
print(f"word[-2] = {word[-2]}")
print(f"word[-3] = {word[-3]}")
```

**Expected output:**
```
First char (positive): A
Last char (negative):  T
Second char (positive): L
Last-2 (negative):    G
Last-3 (negative):    M
--- All negative indices ---
word[-1] = T
word[-2] = G
word[-3] = M
```

### Key Concept
Negative indices count from the end:
- `word[-1]` = last character
- `word[-len(word)]` = first character (same as `word[0]`)
- If string has 9 chars, `word[-9]` == `word[0]`

## Exercise 3: Safe Indexing with len()

Write a function that safely gets the nth character of any string, handling cases where n is out of bounds.

**Approach:**
1. Use len() to get the string length
2. Check if n is within bounds before accessing
3. Return a message if out of bounds

**Solution:**
```python
word = "PYTHON"
n = 10  # Try 6, 7, 10 to see different cases

if abs(n) < len(word):
    if n >= 0:
        print(f"Position {n}: {word[n]}")
    else:
        print(f"Negative position {n}: {word[n]}")
else:
    print(f"Index {n} is out of range for string of length {len(word)}")

print(f"Valid range: 0 to {len(word) - 1} (positive)\nValid range: {-len(word)} to -1 (negative)")
```

**Expected output (for n=10):**
```
Index 10 is out of range for string of length 6
Valid range: 0 to 5 (positive)
Valid range: -6 to -1 (negative)
```

### Key Concept
- `abs(n) < len(word)` checks if the index is within bounds regardless of sign
- Safe indexing prevents `IndexError: string index out of range` crashes

## Exercise 4: Extract Specific Characters

Take a string and extract: first 2 chars, last 3 chars, and the middle char(s).

**Approach:**
1. Use indexing for first characters `[0:n]`
2. Use negative indexing for last `[-n:]`
3. For middle, use `len(word) // 2`

**Solution:**
```python
word = "INFORMATION"
length = len(word)

first_two = word[0:2]
last_three = word[-3:]
middle = word[length // 2]

print(f"Word: {word}")
print(f"First 2 characters: {first_two}")
print(f"Last 3 characters: {last_three}")
print(f"Middle character: {middle}")
```

**Expected output:**
```
Word: INFORMATION
First 2 characters: IN
Last 3 characters: ORN
Middle character: O
```

### Key Concept
- `word[0:2]` extracts indices 0 and 1 (stops BEFORE index 2)
- `word[-3:]` extracts the last 3 characters
- For odd-length strings, `len//2` gives the exact middle index

## Exercise 5: Practical — Palindrome Checker

Build a program that reads a word and checks if it reads the same forwards and backwards.

**Approach:**
1. Read the word from input
2. Create the reverse using negative indexing with a loop
3. Compare the original with the reversed version

**Solution:**
```python
word = input("Enter a word: ").upper()

# Build the reverse using indexing
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print(f"Original: {word}")
print(f"Reversed: {reversed_word}")
print(f"Is palindrome: {word == reversed_word}")

# Simple way:
print(f"Is palindrome (simple): {word == word[::-1]}")
```

**Expected output (for "LEVEL"):**
```
Original: LEVEL
Reversed: LEVEL
Is palindrome: True
Is palindrome (simple): True
```

### Key Concept
- `[::-1]` is Python's slice syntax for reversing strings
- `[::-1]` means: start=None, stop=None, step=-1
- A palindrome reads the same forwards and backwards (LEVEL, MADAM, RACECAR)

## Summary

- Use positive indices (0, 1, 2...) to count from the front
- Use negative indices (-1, -2, -3...) to count from the back
- `word[0]` = first, `word[-1]` = last
- Always check `len(word)` before accessing to avoid IndexError
- `word[a:b]` extracts from a (inclusive) to b (exclusive)
- `word[::-1]` reverses the string

## Practice Ideas

- What is `word[-len(word)]` equal to for any string?
- Extract the vowels (A, E, I, O, U) from a word by checking each index
- Print each letter on its own line using a loop with indexing
- What happens if you try `word[len(word)]`? Catch and explain the error

---

*Next: String Slicing — extracting substrings with [start:end]*