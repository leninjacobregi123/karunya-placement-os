import json, os

base = "/home/ewards/workspace/kpos/hermes/kpos_hermes_build_pack/repo_seed/karunya-placement-os"

apt_days = [
    {"num": 6, "dir": "day-06-simple-interest", "topic": "Simple and Compound Interest", "slug": "simple-interest",
     "warmup": "What is the simple interest on Rs. 1000 at 5% per annum for 3 years? How is it different?",
     "must_do": "Calculate simple interest"},
    {"num": 7, "dir": "day-07-time-work", "topic": "Time and Work", "slug": "time-work",
     "warmup": "If A finishes a task in 6 days and B in 8 days, how long together?",
     "must_do": "Find combined work time"},
    {"num": 8, "dir": "day-08-pipes-cisterns", "topic": "Pipes and Cisterns", "slug": "pipes-cisterns",
     "warmup": "If a pipe fills a tank in 4 hours and another empties it in 6 hours, what is the net rate?",
     "must_do": "Net filling time with pipes"},
    {"num": 9, "dir": "day-09-speed-distance", "topic": "Speed, Time, and Distance", "slug": "speed-distance",
     "warmup": "A car travels 120 km at 60 km/h and returns at 40 km/h. What is the average speed?",
     "must_do": "Find average speed"},
    {"num": 10, "dir": "day-10-trains", "topic": "Trains and Boats", "slug": "trains",
     "warmup": "A 150 m train crosses a pole in 12 seconds. What is its speed in km/h?",
     "must_do": "Train speed from crossing time"},
]

files_written = 0
for day in apt_days:
    dpath = os.path.join(base, "paths/aptitude-reasoning", day["dir"])

    # README.md
    readme = """# Day {}

## Today's Goal
Learn {} concepts and practice with real problems.

## Time: 30 minutes

## Warm Up (2 min)

{}

## Learn (8 min)

Study the key formulas and examples in the module.

## Practice (12 min)

### Must-Do: {}

Open `answers.json` and solve the practice problem. Then check your answer.

### Check

```bash
python scripts/kpos.py check --path aptitude-reasoning --day {}
```

## Quiz (5 min)

Open `quiz.json` and answer 5 questions.

### Record

```bash
python scripts/kpos.py quiz --path aptitude-reasoning --day {} --score YOUR_SCORE --total 5
```

## Reflect (3 min)

Read `reflection.md` and write your answers.

## Hints

If you get stuck, read:

- [Hint 1](hints/hint-1.md)
- [Hint 2](hints/hint-2.md)
- [Hint 3](hints/hint-3.md)

## AI Help

Read [ai-help.md](ai-help.md) before asking AI for help.

## Complete the Day

```bash
python scripts/kpos.py complete-day --path aptitude-reasoning --day {}
```
""".format(day["num"], day["topic"], day["warmup"], day["must_do"], day["num"], day["num"], day["num"])
    
    with open(os.path.join(dpath, "README.md"), "w") as fout:
        fout.write(readme)
    files_written += 1

    # ai-help.md
    ai = """# AI Help: {}

**Goal:** Help the student understand {}.

**Do not solve the problem directly.**
**Ask one question at a time.**
**Maximum response:** 180 words.

**Before hinting, ask:** What formula or pattern applies to this problem?

**Guiding questions:**
- What information is given vs. what needs to be found?
- Which formula connects them?

**Pro tip:** Always write down given values before picking a formula.
""".format(day["topic"], day["topic"])
    
    with open(os.path.join(dpath, "ai-help.md"), "w") as fout:
        fout.write(ai)
    files_written += 1

    # answer-key.md
    answer_key = """# Answer Key for Day {}

## Quiz Answers

### Q1
Practice with the basic formula.

### Q2
Apply the concept to a new scenario.

### Q3
Compare two different approaches.

### Q4
Work through an edge case.

### Q5
Generalize the result for any values.

## Tips
- Always write down your known values first
- Check units before calculating
- Show your work step by step
""".format(day["num"])
    
    with open(os.path.join(dpath, "answer-key.md"), "w") as fout:
        fout.write(answer_key)
    files_written += 1

    # reflection.md
    reflection = """# Day {} Reflection: {}

Take 3 minutes. Answer these honestly:

- What felt easiest today?
- What felt hardest? Why?
- Give one example where you would use this in practice.
- One question to practice more:

--

What I learned today:

>
""".format(day["num"], day["topic"])
    
    with open(os.path.join(dpath, "reflection.md"), "w") as fout:
        fout.write(reflection)
    files_written += 1

    # quiz.json
    quiz_questions = [
        {"question": "What is the basic formula for {} in this context?".format(day["topic"].split(",")[0].split(" and ")[0]),
         "choices": ["Formula 1", "Formula 2", "Formula 3", "Formula 4"],
         "answer": 0,
         "explanation": "Apply the {} formula.".format(day["topic"].split(",")[0].split(" and ")[0])},
        {"question": "If you know value A and need to find value B, which approach works?",
         "choices": ["Direct substitution", "Work backward", "Eliminate options", "Use a table"],
         "answer": 0,
         "explanation": "Work through the problem systematically."},
        {"question": "Which condition changes the approach for {} problems?"
         .format(day["topic"].split(",")[0].split(" and ")[0]),
         "choices": ["Only the units", "The given vs unknown relationship", "Always the same formula", "Random factors"],
         "answer": 1,
         "explanation": "Identify what changes and what stays constant."},
        {"question": "For {}, what is the most common error students make?",
         "format": day["topic"].split(",")[0].split(" and ")[0],
         "choices": ["Unit conversion", "Sign errors", "Wrong formula application", "Calculation mistakes"],
         "answer": 2,
         "explanation": "Always verify you pick the right formula first.",},
        {"question": "How do you verify your answer?",
         "choices": ["Plug it back in", "Estimate first", "Compare with examples", "All of the above"],
         "answer": 3,
         "explanation": "Use multiple verification methods."}
    ]
    
    quiz = {"day": day["num"], "topic": day["topic"], "questions": quiz_questions}
    with open(os.path.join(dpath, "quiz.json"), "w") as fout:
        json.dump(quiz, fout, indent=2)
    files_written += 1

    # tasks.json
    tasks = {"day": day["num"], "topic": day["topic"], "slug": day["slug"],
             "path": "aptitude-reasoning", "time_minutes": 30, "warmup": day["warmup"],
             "read": "modules/aptitude-foundations/{}/01-simple.md".format(day["num"]),
             "practice": [{"type": "must_do", "title": day["must_do"], "file": "answers.json"}],
             "quiz_file": "quiz.json", "timed_drill_file": "timed-drill.json",
             "reflection_file": "reflection.md"}
    with open(os.path.join(dpath, "tasks.json"), "w") as fout:
        json.dump(tasks, fout, indent=2)
    files_written += 1

    # timed-drill.json
    timed = {"day": day["num"], "topic": day["topic"], "time_limit_seconds": 120,
             "questions": [
                 {"question": "What is the primary formula for {}?".format(day["topic"].split(",")[0].split(" and ")[0]),
                  "choices": ["Formula A", "Formula B", "Formula C", "Formula D"], "answer": 0},
                 {"question": "If given rate and time, find work:",
                  "choices": ["Rate x Time", "Rate + Time", "Rate / Time", "Rate - Time"], "answer": 0},
                 {"question": "What does 'average speed' always mean?",
                  "choices": ["Total distance/total time", "Average of speeds", "Median of speeds", "Sum of speeds"], "answer": 0},
                 {"question": "What is the most common mistake in {} problems?".format(day["topic"].split(",")[0].split(" and ")[0]),
                  "choices": ["Using wrong formula", "Unit errors", "Sign mistakes", "Arithmetic errors"], "answer": 0},
                 {"question": "How should you verify your answer?",
                  "choices": ["All of the above", "Only check units", "Only plug back in", "Only compare"], "answer": 0}
             ]}
    with open(os.path.join(dpath, "timed-drill.json"), "w") as fout:
        json.dump(timed, fout, indent=2)
    files_written += 1

    # hints
    hint_texts = {
        "hint-1": "# Hint 1\n\nAlways write down the formula you need before plugging in values.\nStart with: What do I know? What do I need to find?\n",
        "hint-2": "# Hint 2\n\nIdentify the key relationship between given values and the unknown.\nTry substituting in the formula step by step.\n",
        "hint-3": "# Hint 3\n\nCheck your answer by plugging it back in.\nDoes it make sense? Try an estimate first.\n"
    }
    for hname, htext in hint_texts.items():
        with open(os.path.join(dpath, "hints", hname), "w") as fout:
            fout.write(htext)
    files_written += 3

    # answers.json placeholder
    answers = {"day": day["num"], "topic": day["topic"],
               "must_do_question": "Solve: apply {} concepts to a real scenario.".format(day["topic"].lower()),
               "answers": [{"q": "Practice 1", "my_answer": "", "is_correct": False},
                            {"q": "Practice 2", "my_answer": "", "is_correct": False},
                            {"q": "Practice 3", "my_answer": "", "is_correct": False},
                            {"q": "Practice 4", "my_answer": "", "is_correct": False},
                            {"q": "Practice 5", "my_answer": "", "is_correct": False}]}
    with open(os.path.join(dpath, "answers.json"), "w") as fout:
        json.dump(answers, fout, indent=2)
    files_written += 1

    print("Day {:02d} aptitude ({}): 6 files written".format(day["num"], day["topic"]))

print("\nAptitude days 6-10: {} total files written".format(files_written))

for day in apt_days:
    dpath = os.path.join(base, "paths/aptitude-reasoning", day["dir"])
    fc = sum(len(files) for _, _, files in os.walk(dpath))
    print("  {:s}: {:d} files".format(day["dir"], fc))
