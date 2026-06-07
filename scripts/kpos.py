#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config"
PROGRESS = ROOT / "progress" / "progress.json"

# Allow running without installing the repo as a package.
sys.path.insert(0, str(ROOT))
from engine.progress_tracker import (  # noqa: E402
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


def roadmap_for(path_name: str):
    if path_name == "coding-dsa":
        return load_json(CONFIG / "roadmap-coding-dsa-30-days.json", [])
    if path_name == "aptitude-reasoning":
        return load_json(CONFIG / "roadmap-aptitude-reasoning-30-days.json", [])
    if path_name == "full":
        return load_json(CONFIG / "roadmap-full-30-days.json", [])
    raise SystemExit(f"Unknown path: {path_name}")


def day_topic(path_name: str, day: int) -> str:
    data = roadmap_for(path_name)
    if not 1 <= day <= len(data):
        return ""
    item = data[day - 1]
    if path_name == "full":
        return f"{item['coding_dsa']['topic']} + {item['aptitude_reasoning']['topic']}"
    return item.get("topic", "")


def day_slug(path_name: str, day: int) -> str:
    data = roadmap_for(path_name)
    if not 1 <= day <= len(data):
        return ""
    item = data[day - 1]
    if path_name == "full":
        return "full"
    return item.get("slug", "")


def day_folder(path_name: str, day: int) -> Path | None:
    if path_name == "full":
        return None
    slug = day_slug(path_name, day)
    return ROOT / "paths" / path_name / f"day-{day:02d}-{slug}"


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
    print("Then: python scripts/kpos.py start-day --day 1")


def cmd_start(args):
    # Backward-compatible alias for init.
    cmd_init(args)


def print_day(path_name: str, day: int):
    data = roadmap_for(path_name)
    item = data[day - 1]
    print(f"Karunya Placement OS - Day {day}")
    print(f"Path: {path_name}")
    if path_name == "full":
        c = item["coding_dsa"]
        a = item["aptitude_reasoning"]
        print(f"Coding + DSA: {c['topic']} (30 min)")
        print(f"Aptitude + Reasoning: {a['topic']} (30 min)")
        print(f"Open: content/coding-dsa/day-{day:02d}-{c['slug']}/README.md")
        print(f"Open: content/aptitude/day-{day:02d}-{a['slug']}/README.md")
    else:
        print(f"Topic: {item['topic']} (30 min)")
        print(f"Open: content/{path_name}/day-{day:02d}-{item['slug']}/README.md")
    print("Minimum day: python scripts/kpos.py minimum --path", path_name, "--day", day)


def cmd_today(args):
    progress = load_json(PROGRESS, {}) or {}
    path_name = args.path or progress.get("selected_path", "full")
    day = args.day or int(progress.get("current_day", 1))
    print_day(path_name, day)
    append_event("today_viewed", path=path_name, day=day, topic=day_topic(path_name, day))


def cmd_start_day(args):
    topic = day_topic(args.path, args.day)
    mark_day_started(args.path, args.day, topic)
    print(f"Started {args.path} Day {args.day}: {topic}")
    print("After practice, record progress with check, quiz, timed, log-mistake, and complete-day.")


def run_unittest_for_day(path_name: str, day: int) -> tuple[int, int]:
    folder = day_folder(path_name, day)
    if folder is None:
        raise SystemExit("Use --path coding-dsa for test execution. Full mode combines separate paths.")
    code_dir = folder / "code"
    test_files = sorted(code_dir.glob("test_*.py")) if code_dir.exists() else []
    if not test_files:
        print("No local test files found. Use --passed and --total to record manually.")
        return (0, 0)
    result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", str(code_dir)], cwd=code_dir, text=True, capture_output=True)
    output = (result.stdout or "") + (result.stderr or "")
    print(output.strip())
    # unittest does not expose counts via CLI easily; for tracking, treat return code as one local check.
    return (1 if result.returncode == 0 else 0, 1)


def cmd_check(args):
    topic = day_topic(args.path, args.day)
    if args.passed is not None and args.total is not None:
        passed, total = args.passed, args.total
    else:
        passed, total = run_unittest_for_day(args.path, args.day)
    record_tests(args.path, args.day, passed, total, topic)
    print(f"Recorded tests for {args.path} Day {args.day}: {passed}/{total}")


def cmd_quiz(args):
    topic = day_topic(args.path, args.day)
    if args.score is None or args.total is None:
        print("Record quiz result with --score and --total.")
        print(f"Example: python scripts/kpos.py quiz --path {args.path} --day {args.day} --score 4 --total 5 --confidence 3")
        return
    record_quiz(args.path, args.day, args.score, args.total, args.confidence, topic)
    print(f"Recorded quiz for {args.path} Day {args.day}: {args.score}/{args.total}")


def cmd_timed(args):
    topic = day_topic(args.path, args.day)
    if args.correct is None or args.total is None:
        print("Record timed drill with --correct and --total.")
        print(f"Example: python scripts/kpos.py timed --path {args.path} --day {args.day} --correct 8 --total 12 --minutes 12")
        return
    record_timed(args.path, args.day, args.correct, args.total, args.minutes, topic)
    print(f"Recorded timed drill for {args.path} Day {args.day}: {args.correct}/{args.total}")


def cmd_log_mistake(args):
    topic = args.topic or day_topic(args.path, args.day)
    note = args.note or "No note provided."
    log_mistake(args.path, args.day, args.type, note, topic)
    print(f"Logged mistake: {args.type} for {args.path} Day {args.day}")


def cmd_complete_day(args):
    topic = day_topic(args.path, args.day)
    mark_day_completed(args.path, args.day, topic)
    print(f"Completed {args.path} Day {args.day}: {topic}")


def cmd_minimum(args):
    topic = day_topic(args.path, args.day)
    mark_minimum_day(args.path, args.day, args.note or topic)
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
        print(f"- {item.get('path')} Day {item.get('day')} ({item.get('topic')}): revisit {item.get('mistake_type')}")


def cmd_passport(args):
    summary = summarize_progress()
    badges = summary.get("badges", [])
    print("KPOS Placement Passport")
    if not badges:
        print("No badges yet. Start a day to earn your first badge.")
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
    elif args.bank_action == "day":
        call([sys.executable, str(helper), "day", "--path", args.path, "--day", str(args.day)])


def cmd_self_check(args):
    required = [
        "README.md",
        "ROADMAP.md",
        "AGENTS.md",
        "HOW_TO_USE_AI.md",
        "config/roadmap-coding-dsa-30-days.json",
        "config/roadmap-aptitude-reasoning-30-days.json",
        "engines/progress_tracker.py",
        "docs/STUDENT_PROGRESS_TRACKING.md",
    ]
    missing = [p for p in required if not (ROOT / p).exists()]
    for path_name in ["coding-dsa", "aptitude-reasoning"]:
        for d in range(1, 31):
            matches = list((ROOT / "content" / path_name).glob(f"day-{d:02d}-*"))
            if not matches:
                missing.append(f"content/{path_name}/day-{d:02d}-*")
    if missing:
        print("SELF-CHECK FAILED")
        for m in missing:
            print("missing:", m)
        sys.exit(1)
    print("SELF-CHECK PASSED")


def placeholder(name):
    def inner(args):
        print(f"{name} command scaffold is present. Hermes can expand this implementation.")
    return inner


def add_common_day_args(parser, include_path=True):
    if include_path:
        parser.add_argument("--path", default="coding-dsa", choices=["coding-dsa", "aptitude-reasoning"])
    parser.add_argument("--day", type=int, default=1)


def main():
    parser = argparse.ArgumentParser(description="Karunya Placement OS CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="Initialize student-side progress tracking")
    p.add_argument("--path", default="full", choices=["coding-dsa", "aptitude-reasoning", "full"])
    p.add_argument("--student-id", default="local-student")
    p.add_argument("--name", default="")
    p.add_argument("--roll-number", default="")
    p.add_argument("--department", default="")
    p.add_argument("--section", default="")
    p.add_argument("--level", default="beginner", choices=["beginner", "developing", "confident"])
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("start", help="Backward-compatible alias for init")
    p.add_argument("--path", default="full", choices=["coding-dsa", "aptitude-reasoning", "full"])
    p.add_argument("--student-id", default="local-student")
    p.add_argument("--name", default="")
    p.add_argument("--roll-number", default="")
    p.add_argument("--department", default="")
    p.add_argument("--section", default="")
    p.add_argument("--level", default="beginner", choices=["beginner", "developing", "confident"])
    p.set_defaults(func=cmd_start)

    p = sub.add_parser("today")
    p.add_argument("--path", default=None, choices=["coding-dsa", "aptitude-reasoning", "full"])
    p.add_argument("--day", type=int, default=None)
    p.set_defaults(func=cmd_today)

    p = sub.add_parser("start-day")
    add_common_day_args(p)
    p.set_defaults(func=cmd_start_day)

    p = sub.add_parser("check")
    p.add_argument("--path", default="coding-dsa", choices=["coding-dsa"])
    p.add_argument("--day", type=int, default=1)
    p.add_argument("--passed", type=int, default=None)
    p.add_argument("--total", type=int, default=None)
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("quiz")
    add_common_day_args(p)
    p.add_argument("--score", type=int, default=None)
    p.add_argument("--total", type=int, default=None)
    p.add_argument("--confidence", type=int, choices=[1, 2, 3, 4, 5], default=None)
    p.set_defaults(func=cmd_quiz)

    p = sub.add_parser("timed")
    add_common_day_args(p)
    p.add_argument("--correct", type=int, default=None)
    p.add_argument("--total", type=int, default=None)
    p.add_argument("--minutes", type=int, default=None)
    p.set_defaults(func=cmd_timed)

    p = sub.add_parser("log-mistake")
    add_common_day_args(p)
    p.add_argument("--type", default="other")
    p.add_argument("--note", default="")
    p.add_argument("--topic", default="")
    p.set_defaults(func=cmd_log_mistake)

    p = sub.add_parser("complete-day")
    add_common_day_args(p)
    p.set_defaults(func=cmd_complete_day)

    p = sub.add_parser("minimum")
    add_common_day_args(p)
    p.add_argument("--note", default="")
    p.set_defaults(func=cmd_minimum)

    p = sub.add_parser("report")
    p.add_argument("--write", action="store_true")
    p.set_defaults(func=cmd_report)

    p = sub.add_parser("export-week")
    p.set_defaults(func=cmd_export)

    p = sub.add_parser("git-status")
    p.set_defaults(func=cmd_git_status)

    p = sub.add_parser("revise")
    p.set_defaults(func=cmd_revise)

    p = sub.add_parser("passport")
    p.set_defaults(func=cmd_passport)

    p = sub.add_parser("validate-progress")
    p.set_defaults(func=cmd_validate_progress)

    for name in ["recover", "hint", "radar"]:
        p = sub.add_parser(name)
        p.add_argument("--path", default="coding-dsa")
        p.add_argument("--day", type=int, default=1)
        p.set_defaults(func=placeholder(name))

    p = sub.add_parser("bank")
    p.add_argument("bank_action", choices=["stats", "day"], default="stats")
    p.add_argument("--path", default="coding-dsa", choices=["coding-dsa", "aptitude-reasoning"])
    p.add_argument("--day", type=int, default=1)
    p.set_defaults(func=cmd_bank)

    p = sub.add_parser("self-check")
    p.set_defaults(func=cmd_self_check)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
