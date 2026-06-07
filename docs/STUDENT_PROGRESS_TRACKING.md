# Student Progress Tracking Guide

## Overview

KPOS tracks your learning progress entirely on your local machine. No data is sent to any server unless you choose to push your Git repo.

## What Is Tracked

- **Days started and completed** — when you begin and finish each day's task
- **Test results** — passed/total counts for coding problems
- **Quiz scores** — your score and self-reported confidence level
- **Timed drill results** — accuracy and speed for aptitude/reasoning
- **Mistake logs** — what went wrong and what you learned
- **Streak** — consecutive days of activity
- **Badges** — milestones you earn along the way

## How Data Is Stored

All progress lives in the `progress/` directory:

- `progress/progress.json` — Your main profile and completion data
- `progress/events.jsonl` — A chronological log of every action
- `progress/reports/` — Generated reports and exports

You can read these files directly — they are plain JSON.

## Privacy

- Your progress data never leaves your machine unless you `git push`.
- There is no login, no central server, and no analytics.
- Faculty may request an exported summary, but you control what to share.
- If you want to start fresh, simply delete `progress/progress.json` and `progress/events.jsonl`.

## Viewing Your Progress

```bash
# See a summary report
python scripts/kpos.py report

# View earned badges
python scripts/kpos.py passport

# Get revision suggestions based on mistakes
python scripts/kpos.py revise

# Export your progress as a standalone file
python scripts/kpos.py export-week
```

## Validating Your Data

If something seems off, validate your progress files:

```bash
python scripts/kpos.py validate-progress
```

## Starting Over

To reset your progress completely:

```bash
rm progress/progress.json progress/events.jsonl
python scripts/kpos.py start --path full
```

Remember: starting over is not failure — it means you are giving yourself another chance to learn consistently.
