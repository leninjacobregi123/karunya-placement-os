# Karunya Placement OS (KPOS)

A local-first, AI-assisted placement preparation system for final-year students at Karunya Institute of Technology and Sciences.

## Quick Start

### Option A: Local CLI (Claude Code)
```bash
git clone https://github.com/leninjacobregi123/karunya-placement-os.git
cd karunya-placement-os
claude          # or codex
/start coding   # or /start aptitude, /start full
```

### Option B: Docker (GPU-Enabled Web UI)
Ensure you have Docker and NVIDIA Container Toolkit installed/configured.
```bash
git clone https://github.com/leninjacobregi123/karunya-placement-os.git
cd karunya-placement-os
docker compose up -d
```
This will start Ollama, download the `llama3.2:latest` & `mxbai-embed-large:latest` models, and spin up the Next.js Web UI at `http://localhost:3000`. Progress is stored in a Docker volume `kpos_progress`.


## What You Get

**30 topics of placement prep in two tracks:**

- **Coding + DSA** — Python foundations, arrays, two pointers, sliding window, stacks, queues, sorting, binary search, recursion, trees, graphs, dynamic programming, greedy algorithms
- **Aptitude + Reasoning** — Number basics, percentages, ratios, averages, profit-loss, interest, time-work, probability, syllogisms, seating arrangements, data interpretation

**One path** (30 min/session) or **Full Mode** (both tracks, 60 min/session).

## How It Works

1. `/start` — Choose your path. Claude Code creates your profile, detects your current day, and launches the lesson.
2. Do exercises in chat — paste code, get auto-grading, hints if stuck. Progress saves automatically.
3. `/showprogress` — See your scores, weak areas, confidence level.
4. `/hints` — Get ONE hint (never a full answer) for any exercise.
5. `/skip` or `/review` — Move forward or revisit earlier material.

That's the entire flow. No CLI commands, no manual files. Just chat.

## AI Tutor Rules

AI is your coach, not your crutch. Use it to think better, not to skip thinking.

- **Attempt first.** Always try before asking for help.
- **Paste only what matters.** Share your code, the error, the concept you don't understand.
- **Ask for one hint, not the solution.** "Give me the first hint" works.
- **Explain it back.** After AI helps, close the chat and explain the solution out loud.
- **Never submit AI code you can't explain.** If you can't walk through it line by line, you haven't solved it.

AI is there to help you learn, not to do the learning for you. The goal is placement readiness — being able to solve problems without any assistant present.

## CLI (Advanced Users)

For manual control, CLI commands are available but not required:

```bash
python scripts/kpos.py start --path coding-dsa --day 1     # Initialize and start
python scripts/kpos.py today --path coding-dsa               # See today's task
python scripts/kpos.py self-check                            # Validate repo
```

Most students should use `/start` in Claude Code instead.

## Repository Structure

```
karunya-placement-os/
├── README.md              # This file
├── START.md               # Detailed student guide
├── ROADMAP.md             # 30-day roadmap (all topics)
├── .claude/
│   └── AGENTS.md          # AI tutor system prompt (auto-loaded)
├── configs/                # Path and rubric configs
├── content/                # Learning days (coding-dsa + aptitude)
├── concepts/               # Deep-dive concept lessons
├── questions/              # 600+ searchable question bank
├── students/               # Student progress data (auto-managed)
├── docs/                   # Guides
├── scripts/                # CLI tools
├── faculty/                # Faculty materials
└── peer-pods/              # Peer learning guides
```

## No Network Required

Everything runs locally. No API keys, no login, no cloud service.

## License

MIT
