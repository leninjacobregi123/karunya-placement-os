# Progress.md — Karunya Placement OS (KPOS)

## Last Updated
2026-06-07

## Structural Change — Topic-Based Reorganization
All content moved from day-based to topic-based directory structure:
- `content/coding-dsa/day-NN-slug/` → `content/coding/slug/`
- `content/aptitude/day-NN-slug/` → `content/aptitude/slug/`
- Roadmap JSON: `day` → `sequence`, dead `module_ref` dropped
- CLI `kpos.py`: rewritten for topic resolution via sequence→slug→path
- Test files renamed: `test_day_XX.py` → `test_<slug>.py` (hyphens → underscores)

## Feature Tracker

### feat-001: Phase 0
Status: complete
Evidence: KPOS_PROJECT_BASIS_EXTRACTED_SUMMARY.md, AGENTS.md at repo root

### feat-002: Phase 1 — Repository Skeleton
Status: complete
Evidence: README.md, configs/, manifest.json, question-index.csv

### feat-003: Phase 2 — CLI and Engine
Status: complete
Evidence: engines/progress_tracker.py (17 functions), kpos.py self-check works (topic-based)

### feat-004: Phase 3 — Content Generation
Status: in-progress
Progress: 20/60 topics (10 coding + 10 aptitude)
content/coding/ has 10 topic directories, all with valid content
content/aptitude/ has 10 topic directories, all with valid content
Remaining: 40 topics (sequences 11-30 for both tracks)
Quality limits: README 300-800 words per topic

### feat-005: Phase 4 — Model Lessons
Status: complete
Evidence: dp-intuition, percentages, syllogisms — each with full files

### feat-006: Phase 5 — Validation
Status: complete
Evidence: All validators passed after reorganization

### feat-007: Phase 6 — Release Readiness
Status: complete
Evidence: External source index, AI safety policy, faculty/pod guides, CONTRIBUTING, LICENSE

## Fixes Applied During Reorg
- Fixed `aptitude/number-basics/tasks.json` (was empty markdown in .json file)
- Fixed `aptitude/profit-loss/timed-drill.json` (was markdown in .json file, replaced with valid JSON)
- Added missing `answers.json` to aptitude topics 1-5
- Stripped `"day": N` from 60 JSON files across 20 topics
- Stripped dead `"read"` refs to nonexistent `modules/` from 20 tasks.json
- Stripped "Day N:" from all 20 README headings
- Fixed `config/paths.yaml` (coding-dsa → coding, days → topics)
- Renamed 10 test files (hyphens → underscores for unittest discover compat)
