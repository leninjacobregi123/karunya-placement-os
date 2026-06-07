# Progress — Karunya Placement OS

**Last updated:** 2026-06-07
**Branch:** student-flow
**Latest commit:** (pending today's cleanup)

## Overview

| Track | Total | Complete | Remaining | % Done |
|---|---|---|---|---|
| **Coding + DSA** | 30 days | 10 | 20 | 33% |
| **Aptitude + Reasoning** | 30 days | 5 | 25 | 17% |
| **Combined** | 60 days | 15 | 45 | 25% |

## Content Status

### Coding + DSA (Days 1-10) — 10 days complete

Every day has 7 files: README.md, answer-key.json, ai-help.json, answers.json, hints/ (3 hints).

| Day | Topic | Files on Disk | Notes |
|-----|-------|---|---|
| 1 | Python Basics | 7 | 4 direct + 1 subdir |
| 2 | Variables & Data Types | 9 | 6 direct + 1 subdir, includes claude_code.md + codex_code.md |
| 3 | Data Types & Conversion | 9 | 6 direct + 1 subdir, includes claude_code.md + codex_code.md |
| 4 | Operators & Expressions | 9 | 6 direct + 1 subdir, includes claude_code.md + codex_code.md |
| 5 | String Fundamentals | 7 | 4 direct + 1 subdir |
| 6 | String Indexing | 7 | 4 direct + 1 subdir |
| 7 | String Slicing | 7 | 4 direct + 1 subdir |
| 8 | String Methods | 7 | 4 direct + 1 subdir |
| 9 | String Formatting | 7 | 4 direct + 1 subdir |
| 10 | String Practice Problems | 7 | 4 direct + 1 subdir |

### Aptitude + Reasoning (Days 6-10) — 5 days complete

| Day | Topic | Folder | Files |
|-----|-------|--------|---|
| 6 | Number Basics & Classification | 36-aptitude-number-basics | 7 |
| 7 | Percentages | 37-aptitude-percentages | 7 |
| 8 | Ratios & Proportions | 38-aptitude-ratios | 7 |
| 9 | Averages & Mean | 39-aptitude-averages | 7 |
| 10 | Profit & Loss | 40-aptitude-profit-loss | 7 |

Note: Aptitude days use 36-40 indexing (not 6-10). The config roadmaps use 6-10 mapping.

## Days 11-30 (Coding) — 20 days pending

No directories exist. Roadmap planning exists in `configs/roadmap-coding-dsa-30-days.json`.
Content must be created from scratch.

## Aptitude Days 11-30 — 25 days pending

No directories exist. Roadmap planning exists in `configs/roadmap-aptitude-reasoning-30-days.json`.
Content must be created from scratch.

## Cleanup — 2026-06-07

Removed during directory hygiene sweep:
- 26 empty scaffolding directories: `10-string-exercises` through `35-dict-exercises` (all coding days 11-30)
- 4 tutorial duplicate directories: `day-02-through-day-05-tutorial` (dups of 02-05)
- 1 placeholder directory: `05-input-output` (conflicted with `05-string-basics`)

Result: `content/` now has exactly **15 directories**, all non-empty, all with valid content.

## Content Structure (per day)

```
content/NN-topic-slug/
├── README.md              (800-1200 words, 5 progressive exercises)
├── answer-key.json        (exercises: [{title, description}, ...] × 5)
├── ai-help.json           (when_to_help, key_concepts, pro_tips)
├── answers.json           (q1-q5: empty strings)
└── hints/
    ├── hint-1.json        (socratic_question)
    ├── hint-2.json        (socratic_question)
    └── hint-3.json        (socratic_question)
```

Days 2, 3, 4 also include `claude_code.md` and `codex_code.md` (48 bytes each, placeholder text).

## Supporting Infrastructure

| Item | Status |
|------|--------|
| engines/progress_tracker.py | Exists |
| scripts/kpos.py | CLI commands |
| questions/ | 600 original questions |
| configs/roadmap-*.json | 3 roadmap configs |
| .claude/AGENTS.md | AI coach rules |
| docs/ | Admin + progress docs |

## Next Actions

1. Create coding Days 11-30 (no scaffold dirs remain)
2. Create aptitude Days 11-30 (no scaffold dirs remain)
3. Push all changes to `origin/student-flow`
