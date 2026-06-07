# Contributing to KPOS

## How to Add New Content

### Adding a New DSA Lesson

1. Create a new folder under `modules/coding-foundations/`:
   ```
   modules/coding-foundations/new-topic/
   ├── 01-simple.md          (under 600 words)
   ├── 02-deeper.md          (under 1200 words)
   ├── pattern-card.md       (under 200 words)
   └── ai-help.md            (under 120 words)
   ```

2. 01-simple.md: Core concept, code examples, interview cues
3. 02-deeper.md: Variants, edge cases, complexity analysis, stretched problems
4. pattern-card.md: One-page reference
5. ai-help.md: Socratic hints (no solutions)

### Adding a New Aptitude Topic

Same structure, adapted for math/reasoning:
- Concept explanation (under 600 words)
- Formula/reasoning card
- 10 practice questions with answer key
- Error clinic mapping common mistakes

### Adding Questions

Add to `question-bank/self-contained/`:
- `coding-dsa/` for programming problems
- `aptitude-reasoning/` for math/reasoning problems

Every question must include:
- `id`: unique identifier
- `source_type`: "original" (never "external")
- `license_status`: "kpos_original"
- Difficulty (easy/medium/hard)
- Topic mapping

## Validation

Before committing, run:
```bash
python scripts/kpos.py self-check
python validation_harness/validate_kpos_repo.py .
python validation_harness/validate_self_contained_question_bank.py .
```

## Style Guide

- Use simple English — write for a weak student
- Code examples must follow Python PEP 8
- No external links in question statements
- All problems must be self-contained (no context linking)
