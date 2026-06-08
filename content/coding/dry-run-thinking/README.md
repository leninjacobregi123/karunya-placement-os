# Dry Run Thinking

## Today's Goal

Predict the output of code snippets by manually tracing execution. Never guess — trace every variable, every loop, every branch.

## Time: 30 minutes

## Warm Up (1 min)

Look at this code. What does it print? Trace it on paper:
```python
x = 10
for i in range(3):
    x = x + i
print(x)
```

## Learn (8 min)

Read the module: [`modules/coding-foundations/dry-run-thinking/01-simple.md`](../../../modules/coding-foundations/dry-run-thinking/01-simple.md)

## Practice (14 min)

### Must-Do: Trace and verify

Implement a function that traces through a given Python code snippet and returns the value of the last print or return statement.

This trains the skill of mental execution — one of the most valuable debugging skills.

Function signature: `execute_and_verify(code_snippet, expected)`

Function signature: `execute_and_verify(code_snippet, expected)`

Open `code/starter.py` and implement the function. Run:

```bash
python -m unittest code/test_day_02.py
```

## Quiz (5 min)

Answer 5 questions in `quiz.json`, then record:

```bash
python scripts/kpos.py quiz --path coding-dsa --sequence 2 --score YOUR_SCORE --total 5
```

## Reflect (3 min)

Write honest answers to the reflection questions in `reflection.md`.

## Hints

- [Hint 1](hints/hint-1.md)
- [Hint 2](hints/hint-2.md)
- [Hint 3](hints/hint-3.md)

Read hints in order. Try each hint before moving to the next.

## AI Help

Read [ai-help.md](ai-help.md) before asking AI for help.

## Complete the Day

```bash
python scripts/kpos.py complete-day --path coding-dsa --sequence 2
```
