# KPOS Faculty Guide

## For Professors

Karunya Placement OS (KPOS) is a 30-day placement preparation system developed for final-year students at Karunya Institute. This guide helps faculty oversee student progress.

## How to Help Students Use KPOS

### Daily Structure
Each student works on a 30-minute daily path:
- **Coding + DSA** — data structures, algorithms, Python problems
- **Aptitude + Reasoning** — percentages, probability, number theory, logic puzzles
- **Full Mode** — both paths (60 min/day)

### Tracking Student Progress

Use the CLI to monitor individual students:
```bash
python scripts/kpos.py report --student-id STUDENT_ID
```

Or have students run this and share the output:
```bash
python scripts/kpos.py check
python scripts/kpos.py passport
```

The passport command generates a shareable progress summary students can show faculty.

### Key Metrics to Watch
- **Streak**: Are students showing daily consistency?
- **Tests passed**: How many problems solved correctly?
- **Quiz scores**: Pattern recognition and speed
- **Mistakes logged**: Which topics cause repeated errors?
- **Mistake categories**: Syntax, logic, or concept gap?

## When to Intervene

Intervene when a student:
1. Breaks streak for 3+ consecutive days
2. Has quiz score below 40% on 3+ consecutive days
3. Logs mistakes in the same topic repeatedly
4. Shows no progress after 15 days

## Intervention Strategies

1. **Low streak:** Reduce daily commitment to 15 minutes for consistency
2. **Low quiz score:** Focus on the specific failing topic — refer to the AI assistant for targeted practice
3. **Repeated same mistakes:** Check if student has foundation gaps in that topic
4. **No progress after 15 days:** Switch from "Full Mode" to one path only (start fresh)

## Creating a Study Pod

Encourage students to form study pods of 3-4 peers. The peer-pod guide (in `peer-pods/GUIDE.md`) has a structured format for collaboration.

## What KPOS Does NOT Do

- No automated grading of student essays or explanations
- No faculty-facing database — progress stays local to student machines
- No internet required — everything runs offline
- No data sharing with anyone outside the student's device
