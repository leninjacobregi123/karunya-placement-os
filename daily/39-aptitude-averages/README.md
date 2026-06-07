# Averages and Mean

**Duration:** 30 minutes  **Difficulty:** Beginner  **Track:** Aptitude + Reasoning

**Learning Goal:** Understand how to calculate averages, work backward from averages, and solve average-based word problems commonly found in placement tests.

## What You'll Learn

An average (arithmetic mean) is the central value of a set of numbers. It is calculated by dividing the total sum by the count of numbers. Understanding averages is crucial because placement tests frequently use average-based problems involving:
- Class scores, ages, or speeds
- Adding or removing items and calculating the resulting change
- Finding missing values when the average is known

The key insight: **Total = Average × Count**. This reversibility is everything.

---

## Exercise 1 — Basic Average

Find the average of: 12, 24, 36, 48, 60

**Approach:**
1. Write down the numbers to be averaged.
2. Add all of them together to get the total sum.
3. Count how many numbers there are.
4. Divide the sum by the count.

**Solution:**
Sum = 12 + 24 + 36 + 48 + 60 = 180
Count = 5
Average = 180 / 5 = 36

### Key Concept
Average = Sum of all terms ÷ Count of terms

---

## Exercise 2 — Average with a New Person

The average age of a class is 20 years. After a teacher joins, the average becomes 22 years. Find the teacher's age.

**Approach:**
1. Let there be N students in the class.
2. Total age of students = N × 20 = 20N
3. After the teacher joins, there are N + 1 people, and total = (N + 1) × 22
4. The teacher's age is the difference between the new total and the old total.

**Solution:**
- Teacher's total = (N + 1) × 22 = 22N + 22
- Students' total = 20N
- Teacher's age = (22N + 22) - 20N = 2N + 22

But wait — we need the actual number. Let's say we don't know N. The key is: **the teacher brought in 2 years for every student (22 - 20 = 2), plus their own base of 22.**

Teacher's age = 22 + 2N

If we knew N = 10 students, teacher = 22 + 20 = 42. But without N, we express it as **22 + 2N**.

### Key Concept
When an average changes after adding a person, that person's value = old average + (change in average × count of originals)

---

## Exercise 3 — Removal Problem

The average of 6 numbers is 15. If one number is removed, the average becomes 13. Find the removed number.

**Approach:**
1. Calculate the total before removal: Sum_before = 6 × 15 = 90
2. Calculate the total after removal: Sum_after = 5 × 13 = 65
3. The removed number is the difference.

**Solution:**
Removed number = 90 - 65 = 25

### Key Concept
The removed/added value = (count_before × avg_before) - (count_after × avg_after)

---

## Exercise 4 — Average of First N Numbers

Find the average of the first 100 natural numbers.

**Approach:**
1. The first 100 natural numbers are: 1, 2, 3, ..., 99, 100
2. Use the formula for the sum of the first n natural numbers: Sum = n(n+1)/2
3. Then divide by n to get the average.

**Solution:**
Sum of first 100 = 100 × 101 / 2 = 5050
Average = 5050 / 100 = 50.5

Shortcut: For an arithmetic sequence, Average = (first + last) / 2 = (1 + 100) / 2 = 50.5

**Note:** This shortcut works because the numbers are evenly spaced (an arithmetic progression). For general averages, always use Sum/Count.

### Key Concept
For first n natural numbers: Average = (n + 1) / 2

---

## Exercise 5 — Target Average

The average of 5 cricket scores is: 45, 60, 80, 25, 90. How many runs are needed in the 6th match to bring the average to 65?

**Approach:**
1. Calculate the sum of the 5 known scores.
2. Find the target sum for 6 matches with average 65.
3. The difference is the required runs.

**Solution:**
Sum of 5 scores = 45 + 60 + 80 + 25 + 90 = 300
Target sum for 6 matches = 6 × 65 = 390
Runs needed in 6th match = 390 - 300 = 90

### Key Concept
Target Sum = Target Average × Total Count

---

## Formulas

- Average = Sum of all terms / Count of terms
- Sum = Average × Count
- For first n natural numbers: Average = (n + 1) / 2
- Value needed to reach target average = (Target Avg × New Count) - Current Sum

## Practice Ideas

- If the average of 8 numbers is 25 and the average of 3 of them is 20, find the average of the remaining 5.
- A student has an average of 75 in 4 tests. What score is needed in the 5th test to raise the average to 80?
- The average age of a family of 5 is 30. After the grandmother joins, the average becomes 35. What is the grandmother's age?

---

*Next: Profit and Loss (Day 40) — Applying averages to commerce problems*
