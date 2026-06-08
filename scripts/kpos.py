#!/usr/bin/env python3
"""Karunya Placement OS CLI — topic-based content resolution.

Roadmap entries use "sequence" (1..30) and "slug" (topic name).
Content lives under content/coding/<slug>/ or content/aptitude/<slug>/
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config"
PROGRESS = ROOT / "progress" / "progress.json"
CONTENT_CODING = ROOT / "content" / "coding"
CONTENT_APTITUDE = ROOT / "content" / "aptitude"

# Allow running without installing the repo as a package.
sys.path.insert(0, str(ROOT))
from engines.progress_tracker import (  # noqa: E402
    append_event,
    export_student_progress,
    git_status_summary,
    init_student,
    log_mistake,
    mark_day_completed,
    mark_day_started,
    mark_minimum_day,
    read_events,
    record_quiz,
    record_tests,
    record_timed,
    render_report_markdown,
    summarize_progress,
    validate_progress_files,
    write_report,
)


def load_json(path: Path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


# ── Roadmap helpers (sequence-based, topic-first) ──────────────────────────

def roadmap_for(path_name: str):
    """Load the sequence-based roadmap for the given path."""
    if path_name == "coding-dsa":
        return load_json(CONFIG / "roadmap-coding-dsa-30-days.json", [])
    if path_name == "aptitude-reasoning":
        return load_json(CONFIG / "roadmap-aptitude-reasoning-30-days.json", [])
    if path_name == "full":
        return load_json(CONFIG / "roadmap-full-30-days.json", [])
    raise SystemExit(f"Unknown path: {path_name}")


def entry_by_sequence(data: list, seq: int):
    """Return the roadmap entry at the given sequence position."""
    if not 1 <= seq <= len(data):
        return None
    return data[seq - 1]


def seq_topic(data: list, seq: int) -> str:
    """Get topic name for a sequence number (single-path roadmap)."""
    entry = entry_by_sequence(data, seq)
    return entry["topic"] if entry else ""


def seq_slug(data: list, seq: int) -> str:
    """Get slug for a sequence number (single-path roadmap)."""
    entry = entry_by_sequence(data, seq)
    return entry["slug"] if entry else ""


def topic_folder(path_name: str, slug: str) -> Path | None:
    """Resolve content folder from path + slug.

    content/coding/<slug>/  or  content/aptitude/<slug>/
    """
    if path_name == "full":
        return None
    if path_name == "coding-dsa":
        base = CONTENT_CODING / slug
    elif path_name == "aptitude-reasoning":
        base = CONTENT_APTITUDE / slug
    else:
        return None
    if base.is_dir():
        return base
    return None


def seq_folder(path_name: str, seq: int) -> Path | None:
    """Resolve content folder from path + sequence number."""
    data = roadmap_for(path_name)
    slug = seq_slug(data, seq)
    return topic_folder(path_name, slug) if slug else None


# Backward compat aliases — CLI still accepts --day but we treat it as --sequence
day_topic = seq_topic
day_slug = seq_slug
day_folder = seq_folder


# ── Commands ───────────────────────────────────────────────────────────────

def cmd_init(args):
    profile = init_student(
        selected_path=args.path,
        student_id=args.student_id,
        name=args.name,
        roll_number=args.roll_number,
        department=args.department,
        section=args.section,
        level=args.level,
    )
    print("KPOS student tracking initialized.")
    print("Selected path:", profile["selected_path"])
    print("Next: python scripts/kpos.py today")
    print("Then: python scripts/kpos.py start-day --sequence 1")


def cmd_start(args):
    """Backward-compatible alias for init."""
    cmd_init(args)


def print_topic(path_name: str, seq: int):
    """Print info about a topic at the given sequence position."""
    data = roadmap_for(path_name)
    entry = entry_by_sequence(data, seq)
    if entry is None:
        print(f"Sequence {seq} not found. Valid range: 1-{len(data) if data else 0}")
        return
    print(f"Karunya Placement OS - Sequence {seq}")
    print(f"Path: {path_name}")
    if path_name == "full":
        c = entry["coding_dsa"]
        a = entry["aptitude_reasoning"]
        print(f"  Coding + DSA: {c['topic']} (30 min)")
        print(f"  Aptitude + Reasoning: {a['topic']} (30 min)")
        print(f"  Open: content/coding/{c['slug']}/README.md")
        print(f"  Open: content/aptitude/{a['slug']}/README.md")
    else:
        print(f"  Topic: {entry['topic']} (30 min)")
        print(f"  Open: content/{'coding' if 'coding' in path_name else 'aptitude'}/{entry['slug']}/README.md")
    print(f"Minimum: python scripts/kpos.py minimum --path {path_name} --sequence {seq}")


def cmd_today(args):
    progress = load_json(PROGRESS, {}) or {}
    path_name = args.path or progress.get("selected_path", "full")
    seq = args.sequence or args.day or int(progress.get("current_day", 1))
    print_topic(path_name, seq)
    data = roadmap_for(path_name)
    if path_name == "full":
        entry = entry_by_sequence(data, seq)
        topic_name = f"{entry['coding_dsa']['topic']} + {entry['aptitude_reasoning']['topic']}" if entry else ""
    else:
        topic_name = seq_topic(data, seq)
    append_event("today_viewed", path=path_name, sequence=seq, topic=topic_name)


def cmd_start_day(args):
    data = roadmap_for(args.path)
    topic = seq_topic(data, args.sequence)
    mark_day_started(args.path, args.sequence, topic)
    print(f"Started {args.path} Sequence {args.sequence}: {topic}")
    print("After practice, record progress with check, quiz, timed, log-mistake, and complete-day.")


def run_unittest_for_topic(path_name: str, seq: int) -> tuple[int, int]:
    """Run unittest for a coding topic's code/ directory."""
    folder = seq_folder(path_name, seq)
    if folder is None:
        raise SystemExit("Use --path coding-dsa for test execution. Full mode combines separate paths.")
    code_dir = folder / "code"
    if not code_dir.exists():
        print("No code/ directory found. Use --passed and --total to record manually.")
        return (0, 0)
    test_files = sorted(code_dir.glob("test_*.py"))
    if not test_files:
        print("No test files found. Use --passed and --total to record manually.")
        return (0, 0)
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(code_dir)],
        cwd=str(code_dir),
        text=True,
        capture_output=True,
    )
    output = (result.stdout or "") + (result.stderr or "")
    print(output.strip())
    return (1 if result.returncode == 0 else 0, 1)


def cmd_check(args):
    data = roadmap_for(args.path)
    topic = seq_topic(data, args.sequence)
    if args.passed is not None and args.total is not None:
        passed, total = args.passed, args.total
    else:
        passed, total = run_unittest_for_topic(args.path, args.sequence)
    record_tests(args.path, args.sequence, passed, total, topic)
    print(f"Recorded tests for {args.path} Sequence {args.sequence}: {passed}/{total}")


def cmd_quiz(args):
    data = roadmap_for(args.path)
    topic = seq_topic(data, args.sequence)
    if args.score is None or args.total is None:
        print("Record quiz result with --score and --total.")
        print(f"Example: python scripts/kpos.py quiz --path {args.path} --sequence {args.sequence} --score 4 --total 5 --confidence 3")
        return
    record_quiz(args.path, args.sequence, args.score, args.total, args.confidence, topic)
    print(f"Recorded quiz for {args.path} Sequence {args.sequence}: {args.score}/{args.total}")


def cmd_timed(args):
    data = roadmap_for(args.path)
    topic = seq_topic(data, args.sequence)
    if args.correct is None or args.total is None:
        print("Record timed drill with --correct and --total.")
        print(f"Example: python scripts/kpos.py timed --path {args.path} --sequence {args.sequence} --correct 8 --total 12 --minutes 12")
        return
    record_timed(args.path, args.sequence, args.correct, args.total, args.minutes, topic)
    print(f"Recorded timed drill for {args.path} Sequence {args.sequence}: {args.correct}/{args.total}")


def cmd_log_mistake(args):
    data = roadmap_for(args.path)
    topic = args.topic or seq_topic(data, args.sequence)
    note = args.note or "No note provided."
    log_mistake(args.path, args.sequence, args.type, note, topic)
    print(f"Logged mistake: {args.type} for {args.path} Sequence {args.sequence}")


def cmd_complete_day(args):
    data = roadmap_for(args.path)
    topic = seq_topic(data, args.sequence)
    mark_day_completed(args.path, args.sequence, topic)
    print(f"Completed {args.path} Sequence {args.sequence}: {topic}")


def cmd_minimum(args):
    data = roadmap_for(args.path)
    topic = seq_topic(data, args.sequence)
    mark_minimum_day(args.path, args.sequence, args.note or topic)
    print("Minimum viable day recorded.")
    print("You preserved the habit. Continue with the full task when possible.")


def cmd_report(args):
    summary = summarize_progress()
    report = render_report_markdown(summary)
    print(report)
    if args.write:
        path = write_report()
        print(f"\nReport written to: {path.relative_to(ROOT)}")


def cmd_export(args):
    path = export_student_progress()
    print(f"Export written to: {path.relative_to(ROOT)}")
    print("This export is for your own backup/reflection. Keep it private unless you choose to share it.")


def cmd_git_status(args):
    print(git_status_summary())
    print("Suggested student-side commit:")
    print("git add progress")
    print('git commit -m "Update KPOS progress"')
    print("git push")


def cmd_revise(args):
    events = read_events()
    mistakes = [e for e in events if e.get("event") == "mistake_logged"][-5:]
    if not mistakes:
        print("No mistakes logged yet. Review one pattern card and log one insight today.")
        return
    print("Revision suggestions based on recent mistakes:")
    for item in reversed(mistakes):
        seq = item.get("sequence") or item.get("day", "?")
        print(f"- {item.get('path')} Sequence {seq} ({item.get('topic')}): revisit {item.get('mistake_type')}")


def cmd_passport(args):
    summary = summarize_progress()
    badges = summary.get("badges", [])
    print("KPOS Placement Passport")
    if not badges:
        print("No badges yet. Start a topic to earn your first badge.")
    else:
        for badge in badges:
            print("-", badge)


def cmd_validate_progress(args):
    errors = validate_progress_files()
    if errors:
        print("PROGRESS VALIDATION FAILED")
        for err in errors:
            print("-", err)
        sys.exit(1)
    print("PROGRESS VALIDATION PASSED")


def cmd_bank(args):
    from subprocess import call
    helper = ROOT / "scripts" / "question_bank.py"
    if args.bank_action == "stats":
        call([sys.executable, str(helper), "stats"])
    elif args.bank_action == "topic":
        call([sys.executable, str(helper), "topic", "--path", args.path, "--sequence", str(args.sequence)])


def cmd_self_check(args):
    """Validate repo structure — topic-based scan."""
    required_files = [
        "README.md",
        "ROADMAP.md",
        "AGENTS.md",
        "config/roadmap-coding-dsa-30-days.json",
        "config/roadmap-aptitude-reasoning-30-days.json",
        "engines/progress_tracker.py",
        "docs/STUDENT_PROGRESS_TRACKING.md",
    ]
    missing = [p for p in required_files if not (ROOT / p).exists()]

    # Scan content directories for existing topic folders (don't require all 30)
    for path_name, content_dir in [("coding-dsa", CONTENT_CODING), ("aptitude-reasoning", CONTENT_APTITUDE)]:
        roadmap = load_json(CONFIG / f"roadmap-{path_name}-30-days.json", [])
        for entry in roadmap:
            slug = entry.get("slug", "")
            topic_dir = content_dir / slug
            if not topic_dir.is_dir():
                missing.append(f"content/{'coding' if 'coding' in path_name else 'aptitude'}/{slug}/ (sequence {entry.get('sequence')})")
            else:
                # Check key files exist in existing folders
                key_files = ["README.md", "quiz.json"]
                for kf in key_files:
                    if not (topic_dir / kf).exists():
                        missing.append(f"content/{'coding' if 'coding' in path_name else 'aptitude'}/{slug}/{kf}")

    if missing:
        print("SELF-CHECK FAILED")
        for m in missing:
            print("  missing:", m)
        sys.exit(1)
    print("SELF-CHECK PASSED")


def placeholder(name):
    def inner(args):
        print(f"{name} command scaffold is present. Hermes can expand this implementation.")
    return inner


def add_common_seq_args(parser, include_path=True):
    """Add common arguments with both --sequence and --day (backward compat)."""
    if include_path:
        parser.add_argument("--path", default="coding-dsa", choices=["coding-dsa", "aptitude-reasoning"])
    parser.add_argument("--sequence", "-s", type=int, default=1, help="Topic sequence number (1-30)")
    parser.add_argument("--day", type=int, default=None, help="(deprecated, use --sequence)")


def main():
    parser = argparse.ArgumentParser(description="Karunya Placement OS CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # init
    p = sub.add_parser("init", help="Initialize student-side progress tracking")
    p.add_argument("--path", default="full", choices=["coding-dsa", "aptitude-reasoning", "full"])
    p.add_argument("--student-id", default="local-student")
    p.add_argument("--name", default="")
    p.add_argument("--roll-number", default="")
    p.add_argument("--department", default="")
    p.add_argument("--section", default="")
    p.add_argument("--level", default="beginner", choices=["beginner", "developing", "confident"])
    p.set_defaults(func=cmd_init)

    # start (alias for init)
    p = sub.add_parser("start", help="Backward-compatible alias for init")
    p.add_argument("--path", default="full", choices=["coding-dsa", "aptitude-reasoning", "full"])
    p.add_argument("--student-id", default="local-student")
    p.add_argument("--name", default="")
    p.add_argument("--roll-number", default="")
    p.add_argument("--department", default="")
    p.add_argument("--section", default="")
    p.add_argument("--level", default="beginner", choices=["beginner", "developing", "confident"])
    p.set_defaults(func=cmd_start)

    # today
    p = sub.add_parser("today", help="Show current topic")
    p.add_argument("--path", default=None, choices=["coding-dsa", "aptitude-reasoning", "full"])
    p.add_argument("--sequence", "-s", type=int, default=None)
    p.add_argument("--day", type=int, default=None)
    p.set_defaults(func=cmd_today)

    # start-day
    p = sub.add_parser("start-day", help="Mark a topic as started")
    add_common_seq_args(p)
    p.set_defaults(func=cmd_start_day)

    # check
    p = sub.add_parser("check", help="Run tests and record results")
    p.add_argument("--path", default="coding-dsa", choices=["coding-dsa"])
    p.add_argument("--sequence", "-s", type=int, default=1)
    p.add_argument("--day", type=int, default=None)
    p.add_argument("--passed", type=int, default=None)
    p.add_argument("--total", type=int, default=None)
    p.set_defaults(func=cmd_check)

    # quiz
    p = sub.add_parser("quiz", help="Record quiz result")
    add_common_seq_args(p)
    p.add_argument("--score", type=int, default=None)
    p.add_argument("--total", type=int, default=None)
    p.add_argument("--confidence", type=int, choices=[1, 2, 3, 4, 5], default=None)
    p.set_defaults(func=cmd_quiz)

    # timed
    p = sub.add_parser("timed", help="Record timed drill result")
    add_common_seq_args(p)
    p.add_argument("--correct", type=int, default=None)
    p.add_argument("--total", type=int, default=None)
    p.add_argument("--minutes", type=int, default=None)
    p.set_defaults(func=cmd_timed)

    # log-mistake
    p = sub.add_parser("log-mistake", help="Log a mistake for revision")
    add_common_seq_args(p)
    p.add_argument("--type", default="other")
    p.add_argument("--note", default="")
    p.add_argument("--topic", default="")
    p.set_defaults(func=cmd_log_mistake)

    # complete-day
    p = sub.add_parser("complete-day", help="Mark a topic as completed")
    add_common_seq_args(p)
    p.set_defaults(func=cmd_complete_day)

    # minimum
    p = sub.add_parser("minimum", help="Record minimum viable day")
    add_common_seq_args(p)
    p.add_argument("--note", default="")
    p.set_defaults(func=cmd_minimum)

    # report
    p = sub.add_parser("report", help="Show progress report")
    p.add_argument("--write", action="store_true")
    p.set_defaults(func=cmd_report)

    # export-week
    p = sub.add_parser("export-week", help="Export weekly progress")
    p.set_defaults(func=cmd_export)

    # git-status
    p = sub.add_parser("git-status", help="Show git status")
    p.set_defaults(func=cmd_git_status)

    # revise
    p = sub.add_parser("revise", help="Suggest revision topics")
    p.set_defaults(func=cmd_revise)

    # passport
    p = sub.add_parser("passport", help="Show earned badges")
    p.set_defaults(func=cmd_passport)

    # validate-progress
    p = sub.add_parser("validate-progress", help="Validate progress data")
    p.set_defaults(func=cmd_validate_progress)

    # Placeholder commands
    for name in ["recover", "hint", "radar"]:
        p = sub.add_parser(name)
        p.add_argument("--path", default="coding-dsa")
        p.add_argument("--sequence", "-s", type=int, default=1)
        p.set_defaults(func=placeholder(name))

    # bank
    p = sub.add_parser("bank", help="Question bank operations")
    p.add_argument("bank_action", choices=["stats", "topic"], default="stats")
    p.add_argument("--path", default="coding-dsa", choices=["coding-dsa", "aptitude-reasoning"])
    p.add_argument("--sequence", "-s", type=int, default=1)
    p.set_defaults(func=cmd_bank)

    # self-check
    p = sub.add_parser("self-check", help="Validate repo structure")
    p.set_defaults(func=cmd_self_check)

    args = parser.parse_args()

    # Backward compat: --day -> --sequence
    if hasattr(args, "day") and args.day is not None:
        if hasattr(args, "sequence") and args.sequence is None:
            args.sequence = args.day
        elif not hasattr(args, "sequence"):
            args.sequence = args.day

    args.func(args)


if __name__ == "__main__":
    main()
