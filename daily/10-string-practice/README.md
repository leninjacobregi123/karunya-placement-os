# String Practice Problems — Day 10

**Duration:** 30 minutes  **Difficulty:** Beginner  **Track:** Coding + DSA

In this lesson, you'll consolidate everything about strings by solving
practical problems that combine multiple concepts from previous days.
This is where the pieces come together.

## What You'll Practice

- Combining indexing, slicing, and methods
- Building real-world string manipulations
- Problem decomposition (breaking tasks into smaller steps)
- Error handling with string operations
- Clean code style for string processing

## Problem 1: Phone Number Formatter

Read a 10-digit number as a string and format it as (XXX) XXX-XXXX.

**Approach:**
1. Read the phone number as a string
2. Validate it has exactly 10 digits
3. Slice it into parts
4. Format using concatenation or f-strings

**Solution:**
```python
phone = input("Enter a 10-digit number: ").replace(' ', '').replace('-', '')

if len(phone) != 10 or not phone.isdigit():
    print("Error: must be exactly 10 digits")
else:
    area = phone[0:3]
    exchange = phone[3:6]
    subscriber = phone[6:10]
    print(f"Formatted: ({area}) {exchange}-{subscriber}")
    
    # Also show other formats
    print(f"Together: {phone}")
    print(f"With dashes: {area}-{exchange}-{subscriber}")
    print(f"With dots: {area}.{exchange}.{subscriber}")
```

**Expected output (for "9876543210"):**
```
Formatted: (987) 654-3210
Together: 9876543210
With dashes: 987-654-3210
With dots: 987.654.3210
```

## Problem 2: Text Counter

Count vowels, consonants, digits, and spaces in a sentence.

**Approach:**
1. Create counters for each category
2. Loop through each character
3. Use .isdigit(), .isalpha(), and membership checks

**Solution:**
```python
text = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = total_count = len(text)

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char == ' ':
        space_count += 1

print(f"Text:   '{text}'")
print(f"Length: {total_count}")
print(f"Vowels:   {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Digits:   {digit_count}")
print(f"Spaces:   {space_count}")
print(f"Other:    {total_count - vowel_count - consonant_count - digit_count - space_count}")
```

**Expected output (for "Hello World 123"):**
```
Text:   'Hello World 123'
Length: 15
Vowels:   3
Consonants: 7 
Digits:   3
Spaces:   2
Other:    0
```

## Problem 3: Palindrome Checker

Check if a string reads the same forwards and backwards (ignoring spaces and case).

**Approach:**
1. Clean the string (lowercase, remove spaces)
2. Compare with its reverse
3. Display the result

**Solution:**
```python
word = input("Enter a word or phrase: ").lower().replace(' ', '')

# Method 1: Slice reversal
is_palindrome_1 = word == word[::-1]

# Method 2: Manual check
manual_check = True
for i in range(len(word) // 2):
    if word[i] != word[-1-i]:
        manual_check = False
        break

print(f"Input: '{word}'")
print(f"Reversed: '{word[::-1]}'")
print(f"Is palindrome: {is_palindrome_1 and manual_check}")

# Test with common palindromes
test_phrases = ["racecar", "madam", "hello", "Was it a car or a cat I saw"]
for phrase in test_phrases:
    cleaned = phrase.replace(' ', '').lower()
    is_pali = cleaned == cleaned[::-1]
    print(f"{'Yes' if is_pali else 'No':>3} - '{phrase}'")
```

## Problem 4: Word Frequency Counter

Count how many times each word appears in a sentence.

**Approach:**
1. Clean and split the text into words
2. Use a dictionary to count occurrences
3. Display results sorted by frequency

**Solution:**
```python
text = input("Enter a sentence: ").lower()
words = text.split(' ')

frequencies = {}
for word in words:
    if word:  # Skip empty strings
        frequencies[word] = frequencies.get(word, 0) + 1

# Sort by frequency (highest first)
sorted_items = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

print(f"\nWord frequencies in: '{text}'")
print(f"{'Word':<15} {'Count':>5}")
print("-" * 22)
for word, count in sorted_items:
    print(f"{word:<15} {count:>5}")
```

**Expected output (for "the cat and the dog and the bird"):**
```
Word frequencies in: 'the cat and the dog and the bird'
Word            Count
----------------------
the                  3
and                  2
cat                  1
dog                  1
bird                 1
```

## Problem 5: Password Strength Checker

Create a program that checks if a password meets minimum strength requirements.

**Approach:**
1. Read the password
2. Check length, uppercase, lowercase, digit, and special character
3. Score it and display suggestions if weak

**Solution:**
```python
password = input("Enter a password: ")

score = 0
feedback = []

# Length check
if len(password) >= 8:
    score += 1
    feedback.append("[OK] At least 8 characters")
else:
    feedback.append(f"[!] Too short: {len(password)} chars (need 8+)")

# Uppercase check
has_upper = any(c.isupper() for c in password)
if has_upper:
    score += 1
    feedback.append("[OK] Has uppercase letter")
else:
    feedback.append("[!] Add uppercase letter")

# Lowercase check
has_lower = any(c.islower() for c in password)
if has_lower:
    score += 1
    feedback.append("[OK] Has lowercase letter")
else:
    feedback.append("[!] Add lowercase letter")

# Digit check
has_digit = any(c.isdigit() for c in password)
if has_digit:
    score += 1
    feedback.append("[OK] Has digit")
else:
    feedback.append("[!] Add a number")

# Special character check
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
has_special = any(c in special_chars for c in password)
if has_special:
    score += 1
    feedback.append("[OK] Has special character")
else:
    feedback.append("[!] Add a special character (!, @, #, etc.)")

# Overall score
strength = ["Very Weak", "Weak", "Average", "Strong", "Very Strong"][min(score, 4)]
print(f"\nPassword: {'*' * len(password)}")
print(f"Score: {score}/5 — {strength}")

for fb in feedback:
    print(f"  {fb}")
```

## Summary

- Combine methods: `.lower().replace().split()` is a common cleanup pipeline
- Slice by position for fixed-width formats (phone numbers, dates)
- Use `.isdigit()`, `.isalpha()`, `.isupper()`, `islower()` for character-level checks
- `.count()` counts substrings; loops count individual characters
- `.find()` finds position; -1 means not found
- Always validate input before processing — check length, characters, etc.
- Clean, readable output comes from consistent formatting and clear labels

## Practice Ideas

- Write a function that takes a word and returns all possible anagrams
- Check if someone's name contains only alphabetic characters
- Create a ROT13 cipher that shifts each letter by 13 positions
- What does `"Hello".split('l')` return? Try it — think about it first, then verify.
- Count how many characters in a string appear exactly once

---

*Congratulations! You've completed the 10-day introductory Python course.*
