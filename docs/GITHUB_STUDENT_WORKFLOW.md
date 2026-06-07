# GitHub Student Workflow Guide

## For Students Who Want to Track Progress with Git

Git is optional. KPOS works perfectly without it. But if you want to track your progress over time, here is a simple workflow.

## Setup

1. Clone the repo:
   ```bash
   git clone <repo-url>
   cd karunya-placement-os
   ```

2. Initialize your KPOS profile:
   ```bash
   python scripts/kpos.py start --path full
   ```

## Daily Workflow

After completing your daily practice:

```bash
# Check your progress
python scripts/kpos.py report

# See what changed
python scripts/kpos.py git-status

# Save your progress
git add progress
git commit -m "Complete day X"
git push
```

You do not need to commit everything — just your `progress/` folder.

## Branch Strategy

- Work on your `master` branch directly.
- You do not need pull requests or feature branches for personal progress.
- If you want to try something without affecting your main progress, create a branch:
  ```bash
  git checkout -b practice-day-5
  ```

## What Not to Commit

Never commit:
- Half-finished code that you are still working on
- Personal notes unrelated to KPOS
- AI chat exports

Only commit when you have completed a day or made meaningful progress.

## Recovery After a Missed Day

If you missed several days:

```bash
git pull  # Get latest if you have other machines
python scripts/kpos.py recover
```

Recovery mode will suggest a 15-minute task to get back on track.

## Sharing Progress with Faculty

If a faculty member asks for your progress:

```bash
# Generate a report
python scripts/kpos.py report --write

# Export your data
python scripts/kpos.py export-week
```

Then share the exported file from `progress/reports/`. You control what to share and when.

## Remember

Git is a tool for you, not a requirement. If it feels confusing, focus on the daily practice first. You can learn Git at your own pace.
