# String Methods — Day 08

**Duration:** 30 minutes  **Difficulty:** Beginner  **Track:** Coding + DSA

Python provides built-in **methods** — functions that work on strings directly.
Methods let you transform, search, split, and analyze text without writing new loops.
Think of them as a toolbox: each method solves a specific text problem.

## What You'll Learn

- Upper/lower case conversion
- Stripping whitespace
- Finding and replacing text
- Splitting and joining strings
- Practical problems combining multiple methods

## Common String Methods

| Method | What it does | Returns |
|---|---|---|
| .upper() | All uppercase | str |
| .lower() | All lowercase | str |
| .strip() | Remove leading/trailing whitespace | str |
| .replace(old, new) | Replace all occurrences | str |
| .split(separator) | Break into list | list |
| .find(substring) | Find position of substring | int or -1 |
| .startswith(prefix) | Check if starts with | bool |
| .endswith(suffix) | Check if ends with | bool |
| .count(substring) | Count occurrences | int |

## Exercise 1: Case Conversion

Create a username that might contain mixed case, then normalize it for comparison.

**Approach:**
1. Create a string with mixed case
2. Use .upper() and .lower()
3. Compare results

**Solution:**
```python
username = "StudentOne123"

print(f"Original: {username}")
print(f"Upper:    {username.upper()}")
print(f"Lower:    {username.lower()}")

# Check if it matches a known name (case-insensitive)
known_name = "studentone123"
print(f"Matches {known_name}: {username.lower() == known_name.lower()}")
```

**Expected output:**
```
Original: StudentOne123
Upper:    STUDENTONE123
Lower:    studentone123
Matches studentone123: True
```

### Key Concept
- .upper() and .lower() return NEW strings — they don't modify the original
- Methods are called with a dot: word.method()
- String methods can be chained: "hello".upper().strip()

## Exercise 2: Stripping and Normalizing

Read user input that has extra whitespace, then normalize and display it.

**Approach:**
1. Create a string with leading/trailing and internal whitespace
2. Use .strip() to remove outer whitespace
3. Use .replace(' ', '') to remove internal whitespace as well

**Solution:**
```python
raw_input = "   Hello, World!  "

# Outer whitespace
stripped = raw_input.strip()
print(f"Original:   '{raw_input}'")
print(f"Stripped:   '{stripped}'")
print(f"Len changed: {len(raw_input)} -> {len(stripped)}")

# Replace internal spaces with single space
cleaned = "  Hello  ,  World!  ".replace('  ', ' ').strip()
print(f"Cleaned:    '{cleaned}'")

# Remove all spaces entirely
no_spaces = "Hello     World".replace(' ', '')
print(f"No spaces:  '{no_spaces}'")
```

### Key Concept
- .strip() removes whitespace from BOTH ends
- .lstrip() removes ONLY from the left (beginning)
- .rstrip() removes ONLY from the right (end)
- .replace('old', 'new') replaces ALL occurrences of 'old' with 'new'

## Exercise 3: find(), count(), startswith(), endswith()

Given a sentence, find positions of words and check if it contains specific patterns.

**Approach:**
1. Use .find() to locate substrings
2. Use .count() to count occurrences
3. Use .startswith() and .endswith() for pattern matching

**Solution:**
```python
sentence = "Python is great and Python is powerful"

# Find first occurrence
pos = sentence.find("Python")
print(f"First 'Python' at position {pos}")   # 0

# Count occurrences
count = sentence.count("Python")
print(f"'Python' occurs {count} times")     # 2

# Check start/end
print(f"Starts with 'Python': {sentence.startswith('Python')}")  # True
print(f"Ends with 'Powerful': {sentence.endswith('powerful')}")   # True
print(f"Ends with 'Power!':   {sentence.endswith('Power!')}")     # False

# Find a word that doesn't exist
not_found = sentence.find("Java")
print(f"'Java' found at position: {not_found}")  # -1 means not found
```

### Key Concept
- .find() returns -1 when not found (unlike .index() which raises an error)
- .count() is useful for frequency analysis
- .startswith() and .endswith() take an optional tuple: word.startswith(('http', 'https', 'ftp'))

## Exercise 4: split() and join()

Break a sentence into words, and rejoin them with a different separator.

**Approach:**
1. Use .split(delimiter) to break a string into a list
2. Use a loop to process each word
3. Use ' '.join(list) to recombine

**Solution:**
```python
text = "Python is a great programming language"

# Split by spaces
words = text.split(' ')
print(f"Words: {words}")

# Process each word: capitalize first letter, lowercase rest
capitalized_words = [w.capitalize() for w in words]
print(f"Capitalized: {capitalized_words}")

# Join with a different separator (e.g., hyphens instead of spaces)
hyphenated = "-".join(capitalized_words)
print(f"Joined: {hyphenated}")

# Split by a specific delimiter
csv = "Alice,25,Mumbai,92.5"
fields = csv.split(',')
print(f"CSV fields: {fields}")
```

### Key Concept
- .split('delimiter') breaks on that separator and returns a list
- text.join(list) takes a string and joins all list items with that string as separator
- text.split() with no argument splits on any whitespace and removes empty strings
- "delimiter".join(list) is equivalent to: for item in list: result += item + delimiter

## Exercise 5: Practical — Build a Text Analyzer

Read a sentence and compute: word count, character count, most frequent word, and how many words start with a vowel.

**Approach:**
1. Clean the text (lowercase, strip, split)
2. Use len() for counts
3. Use .count() or a dictionary for frequency analysis
4. Use .startswith() for vowel checking

**Solution:**
```python
text = input("Enter a sentence: ").lower().strip()
words = text.split(' ')

# Counts
print(f"Character count: {len(text)}")
print(f"Word count:      {len(words)}")

# Most frequent word
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

most_common = max(freq, key=freq.get)
print(f"Most frequent word: '{most_common}' ({freq[most_common]} times)")

# Vowel starts
vowels = 'aeiou'
vowel_starts = [w for w in words if w[0] in vowels if w]
print(f"Words starting with vowel: {len(vowel_starts)} -> {vowel_starts}")
```

### Key Concept
- .lower().strip().split() is the standard text cleaning pipeline
- .get(key, default) safely accesses dictionary keys
- max(dict, key=dict.get) finds the key with the highest value
- List comprehensions make filtering concise: [w for w in words if condition]

## Summary

- .upper()/.lower() convert case
- .strip()/.lstrip()/.rstrip() manage whitespace  
- .replace(old, new) swaps text
- .find()/.index() locate substrings; .count() counts them
- .split() breaks into lists; .join() combines lists into strings
- Methods chain: text.lower().replace('x', 'y').strip()
- Methods return NEW strings — the original is unchanged

## Practice Ideas

- What happens when you split a string with .split('xyz') when 'xyz' never appears?
- Use .startswith() to check if a file name ends with ".py" or ".txt"
- Count how many words in a sentence are longer than 5 characters
- Write a function that takes a sentence and returns all unique words sorted alphabetically

---

*Next: String Formatting — creating readable, properly formatted output*
