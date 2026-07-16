#!/usr/bin/env python3
"""Student progress tracking for Karunya Placement OS.

Supports two modes:
1. Classic mode — all data under progress/ (for CLI/manual use)
2. Auto-save mode — data saved directly to ~/.kpos/student.json (for /start flow)

No network access required.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Default progress file path
DEFAULT_KPOS_DIR = os.path.expanduser('~/.kpos')
AUTO_SAVE_FILE = os.path.join(DEFAULT_KPOS_DIR, 'student.json')


# Auto-save mode helpers (for /start flow) — student never touches these files
def _ensure_kpos_dir() -> None:
    os.makedirs(DEFAULT_KPOS_DIR, exist_ok=True)


def _load_auto_progress() -> dict:
    """Load progress from auto-save file (used by /start flow)."""
    _ensure_kpos_dir()
    if os.path.exists(AUTO_SAVE_FILE):
        return json.loads(Path(AUTO_SAVE_FILE).read_text(encoding="utf-8"))
    return {}


def _save_auto_progress(data: dict) -> None:
    """Save progress to auto-save file (used by /start flow)."""
    _ensure_kpos_dir()
    Path(AUTO_SAVE_FILE).write_text(json.dumps(data, indent=2), encoding="utf-8")


def _normalize_selected_path(path: str) -> str:
    """Map any path alias (coding, coding_dsa, coding-dsa, ...) to the canonical
    slug used by config/roadmap-*.json and the web UI (coding-dsa /
    aptitude-reasoning / full)."""
    path = (path or "").lower()
    if "full" in path:
        return "full"
    if "aptitude" in path:
        return "aptitude-reasoning"
    if "coding" in path:
        return "coding-dsa"
    return path


def create_auto_profile(selected_path: str = "coding-dsa") -> dict:
    """Create a new auto-save profile (called by /start)."""
    _ensure_kpos_dir()
    profile = {
        "student_id": "local-student",
        "name": "",
        "selected_path": _normalize_selected_path(selected_path),
        "current_day": 1,
        "days_completed_coding": [],
        "days_completed_aptitude": [],
        "scores": {},
        "weak_topics": [],
        "streak": 0,
        "last_active_day": None,
        "created_at": _now_iso(),
    }
    _save_auto_progress(profile)
    return profile


def get_current_day_auto() -> int:
    """Auto-detect current day from auto-save progress."""
    progress = _load_auto_progress()
    if not progress:
        return 1
    coding = progress.get("days_completed_coding", [])
    aptitude = progress.get("days_completed_aptitude", [])
    coding_max = max([d.get("day", 0) for d in coding]) if coding else 0
    apti_max = max([d.get("day", 0) for d in aptitude]) if aptitude else 0
    return max(coding_max, apti_max) + 1


def mark_day_complete_auto(path: str, day: int, topic: str) -> None:
    """Mark a day complete in auto-save progress."""
    progress = _load_auto_progress()
    if not progress:
        progress = create_auto_profile(path.split("_")[0] if "_" in path else path)
    
    if "coding" in path:
        list_key = "days_completed_coding"
    else:
        list_key = "days_completed_aptitude"
    
    already = [d.get("day") for d in progress.get(list_key, [])]
    if day not in already:
        progress.setdefault(list_key, []).append({
            "day": day,
            "topic": topic,
            "completed_at": _now_iso(),
        })
    
    # Advance current_day
    current = progress.get("current_day", 1)
    if day + 1 > current:
        progress["current_day"] = day + 1
    
    progress["last_active_day"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    _save_auto_progress(progress)


def score_day_auto(path: str, day: int, score: int, total: int = 5) -> None:
    """Record a score for an auto-saved day."""
    progress = _load_auto_progress()
    if not progress:
        progress = create_auto_profile("coding-dsa")
    key = f"{day}-" + path.split("_")[0] if "_" in path else path
    progress.setdefault("scores", {})[key] = {
        "path": path,
        "day": day,
        "score": score,
        "total": total,
        "timestamp": _now_iso(),
    }
    _save_auto_progress(progress)


def summarize_auto_progress() -> dict:
    """Produce a progress summary from auto-save data."""
    progress = _load_auto_progress()
    if not progress:
        return {"days_completed": 0, "scores": {}, "weak_topics": []}
    
    coding = progress.get("days_completed_coding", [])
    aptitude = progress.get("days_completed_aptitude", [])
    total = len(coding) + len(aptitude)
    scores = progress.get("scores", {})
    
    # Compute average score
    avg = sum(s.get("score", 0) for s in scores.values()) / max(len(scores), 1)
    
    return {
        "current_day": progress.get("current_day", 1),
        "days_completed": total,
        "coding_completed": len(coding),
        "aptitude_completed": len(aptitude),
        "scores": scores,
        "average_score": round(avg, 1),
        "weak_topics": progress.get("weak_topics", []),
        "streak": progress.get("streak", 0),
    }

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
# ROOT is set by kpos.py; when this module is imported directly, fall back.
try:
    ROOT  # noqa: F821
except NameError:
    ROOT = Path(__file__).resolve().parents[2]

PROGRESS_FILE = ROOT / "progress" / "progress.json"
EVENTS_FILE   = ROOT / "progress" / "events.jsonl"
REPORTS_DIR   = ROOT / "progress" / "reports"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _ensure_dirs() -> None:
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def _load_progress() -> dict:
    _ensure_dirs()
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    return {}


def _save_progress(data: dict) -> None:
    _ensure_dirs()
    PROGRESS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _append_event_raw(event: dict) -> None:
    _ensure_dirs()
    with open(EVENTS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _default_profile() -> dict:
    return {
        "student_id": "local-student",
        "name": "",
        "roll_number": "",
        "department": "",
        "section": "",
        "level": "beginner",
        "selected_path": "full",
        "current_day": 1,
        "started_days_coding": [],
        "completed_days_coding": [],
        "started_days_aptitude": [],
        "completed_days_aptitude": [],
        "minimum_days": [],
        "tests": {},
        "quizzes": {},
        "timed_drills": {},
        "mistakes": [],
        "streak": 0,
        "last_active_day": None,
        "created_at": _now_iso(),
    }


# ---------------------------------------------------------------------------
# Public API — 17 functions imported by kpos.py
# ---------------------------------------------------------------------------

def init_student(
    selected_path: str,
    student_id: str = "local-student",
    name: str = "",
    roll_number: str = "",
    department: str = "",
    section: str = "",
    level: str = "beginner",
) -> dict:
    """Create or reset the student progress profile."""
    _ensure_dirs()
    profile = {
        "student_id": student_id,
        "name": name,
        "roll_number": roll_number,
        "department": department,
        "section": section,
        "level": level,
        "selected_path": selected_path,
        "current_day": 1,
        "started_days_coding": [],
        "completed_days_coding": [],
        "started_days_aptitude": [],
        "completed_days_aptitude": [],
        "minimum_days": [],
        "tests": {},
        "quizzes": {},
        "timed_drills": {},
        "mistakes": [],
        "streak": 0,
        "last_active_day": None,
        "created_at": _now_iso(),
    }
    _save_progress(profile)
    return profile


def mark_day_started(path: str, day: int, topic: str) -> None:
    """Record that a day has been started."""
    progress = _load_progress()
    if not progress:
        progress = _default_profile()

    list_key = "started_days_coding" if "coding" in path else "started_days_aptitude"
    day_entry = {"day": day, "topic": topic, "started_at": _now_iso()}
    if day_entry not in progress.get(list_key, []):
        progress.setdefault(list_key, []).append(day_entry)

    # Update current_day if this day is ahead
    current = progress.get("current_day", 1)
    if day >= current:
        progress["current_day"] = day

    progress["last_active_day"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    _save_progress(progress)
    _append_event_raw({"event": "day_started", "path": path, "day": day, "topic": topic, "timestamp": _now_iso()})


def mark_day_completed(path: str, day: int, topic: str) -> None:
    """Record that a day has been fully completed."""
    progress = _load_progress()
    if not progress:
        progress = _default_profile()

    list_key = "completed_days_coding" if "coding" in path else "completed_days_aptitude"
    already = [d.get("day") for d in progress.get(list_key, [])]
    if day not in already:
        progress.setdefault(list_key, []).append({
            "day": day,
            "topic": topic,
            "completed_at": _now_iso(),
        })

    # Advance current_day
    current = progress.get("current_day", 1)
    if day + 1 > current:
        progress["current_day"] = day + 1

    # Update streak
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    last = progress.get("last_streak_day")
    if last == today:
        pass  # already counted today
    elif last == (datetime.now(timezone.utc) - __import__("datetime").timedelta(days=1)).strftime("%Y-%m-%d"):
        progress["streak"] = progress.get("streak", 0) + 1
    else:
        progress["streak"] = 1
    progress["last_streak_day"] = today
    progress["last_active_day"] = today

    _save_progress(progress)
    _append_event_raw({"event": "day_completed", "path": path, "day": day, "topic": topic, "timestamp": _now_iso()})


def mark_minimum_day(path: str, day: int, note: str) -> None:
    """Record a minimum viable day (habit preserved, not full task)."""
    progress = _load_progress()
    if not progress:
        progress = _default_profile()

    progress.setdefault("minimum_days", []).append({
        "path": path,
        "day": day,
        "note": note,
        "timestamp": _now_iso(),
    })
    progress["last_active_day"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    _save_progress(progress)
    _append_event_raw({"event": "minimum_day", "path": path, "day": day, "note": note, "timestamp": _now_iso()})


def record_tests(path: str, day: int, passed: int, total: int, topic: str) -> None:
    """Record test results for a day."""
    progress = _load_progress()
    if not progress:
        progress = _default_profile()

    key = f"{path}:{day}"
    progress.setdefault("tests", {})[key] = {
        "path": path,
        "day": day,
        "passed": passed,
        "total": total,
        "topic": topic,
        "timestamp": _now_iso(),
    }

    _save_progress(progress)
    _append_event_raw({"event": "tests_recorded", "path": path, "day": day, "passed": passed, "total": total, "topic": topic, "timestamp": _now_iso()})


def record_quiz(path: str, day: int, score: int, total: int, confidence: int | None, topic: str) -> None:
    """Record a quiz result for a day."""
    progress = _load_progress()
    if not progress:
        progress = _default_profile()

    key = f"{path}:{day}"
    progress.setdefault("quizzes", {})[key] = {
        "path": path,
        "day": day,
        "score": score,
        "total": total,
        "confidence": confidence,
        "topic": topic,
        "timestamp": _now_iso(),
    }

    _save_progress(progress)
    _append_event_raw({"event": "quiz_recorded", "path": path, "day": day, "score": score, "total": total, "topic": topic, "timestamp": _now_iso()})


def record_timed(path: str, day: int, correct: int, total: int, minutes: int | None, topic: str) -> None:
    """Record a timed drill result for a day."""
    progress = _load_progress()
    if not progress:
        progress = _default_profile()

    key = f"{path}:{day}"
    progress.setdefault("timed_drills", {})[key] = {
        "path": path,
        "day": day,
        "correct": correct,
        "total": total,
        "minutes": minutes,
        "topic": topic,
        "timestamp": _now_iso(),
    }

    _save_progress(progress)
    _append_event_raw({"event": "timed_recorded", "path": path, "day": day, "correct": correct, "total": total, "topic": topic, "timestamp": _now_iso()})


def log_mistake(path: str, day: int, mistake_type: str, note: str, topic: str) -> None:
    """Log a mistake for revision tracking."""
    progress = _load_progress()
    if not progress:
        progress = _default_profile()

    entry = {
        "path": path,
        "day": day,
        "mistake_type": mistake_type,
        "note": note,
        "topic": topic,
        "timestamp": _now_iso(),
    }
    progress.setdefault("mistakes", []).append(entry)

    _save_progress(progress)
    _append_event_raw({"event": "mistake_logged", "path": path, "day": day, "topic": topic, "mistake_type": mistake_type, "note": note, "timestamp": _now_iso()})


def append_event(event: str, **kwargs) -> None:
    """Append a generic event to the event log."""
    _append_event_raw({"event": event, "timestamp": _now_iso(), **kwargs})


def read_events() -> list[dict]:
    """Read all events from the event log."""
    if not EVENTS_FILE.exists():
        return []
    lines = EVENTS_FILE.read_text(encoding="utf-8").splitlines()
    result = []
    for line in lines:
        line = line.strip()
        if line:
            try:
                result.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return result


def summarize_progress() -> dict:
    """Produce a progress summary dict for reports and badges."""
    progress = _load_progress()
    if not progress:
        return {"badges": [], "days_completed": 0, "streak": 0, "selected_path": "none"}

    coding_done = len(progress.get("completed_days_coding", []))
    aptitude_done = len(progress.get("completed_days_aptitude", []))
    total_done = coding_done + aptitude_done
    streak = progress.get("streak", 0)

    # Compute test stats
    tests = progress.get("tests", {})
    total_passed = sum(t.get("passed", 0) for t in tests.values())
    total_tests = sum(t.get("total", 0) for t in tests.values())

    # Compute quiz stats
    quizzes = progress.get("quizzes", {})
    total_score = sum(q.get("score", 0) for q in quizzes.values())
    total_quiz_questions = sum(q.get("total", 0) for q in quizzes.values())

    # Badges
    badges = []
    if coding_done >= 1:
        badges.append("First Coding Day Completed")
    if aptitude_done >= 1:
        badges.append("First Aptitude Day Completed")
    if total_done >= 7:
        badges.append("Week One Complete")
    if total_done >= 5:
        badges.append("Halfway Hero")
    if total_done >= 10:
        badges.append("Sprint Champion")
    if streak >= 3:
        badges.append(f"{streak}-Day Streak")
    if total_passed >= 10:
        badges.append("10 Tests Passed")
    if total_passed >= 50:
        badges.append("50 Tests Passed")
    mistakes = progress.get("mistakes", [])
    if len(mistakes) >= 5:
        badges.append("Reflection: 5 Mistakes Logged")

    return {
        "selected_path": progress.get("selected_path", "none"),
        "current_day": progress.get("current_day", 1),
        "days_completed": total_done,
        "coding_days_completed": coding_done,
        "aptitude_days_completed": aptitude_done,
        "streak": streak,
        "tests_passed": total_passed,
        "tests_total": total_tests,
        "quiz_score": total_score,
        "quiz_total": total_quiz_questions,
        "mistake_count": len(mistakes),
        "badges": badges,
    }


def validate_progress_files() -> list[str]:
    """Validate progress data integrity. Return list of error strings (empty = OK)."""
    errors = []

    if PROGRESS_FILE.exists():
        try:
            data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
            if "selected_path" not in data:
                errors.append("progress.json missing 'selected_path'")
            # Check for day consistency
            for key in ["completed_days_coding", "completed_days_aptitude"]:
                days = data.get(key, [])
                day_nums = [d.get("day") for d in days if isinstance(d, dict) and d.get("day") is not None]
                if day_nums != sorted(set(n for n in day_nums if n is not None)):
                    errors.append(f"Duplicate or unordered entries in {key}")
        except json.JSONDecodeError:
            errors.append("progress.json is not valid JSON")
    else:
        # No progress yet is valid — just not initialized
        pass

    if EVENTS_FILE.exists():
        lines = EVENTS_FILE.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line:
                try:
                    json.loads(line)
                except json.JSONDecodeError:
                    errors.append(f"events.jsonl line {i} is not valid JSON")

    return errors


def render_report_markdown(summary: dict) -> str:
    """Render a Markdown report from a progress summary."""
    lines = [
        "# KPOS Progress Report",
        "",
        f"- **Path:** {summary.get('selected_path', 'none')}",
        f"- **Current day:** {summary.get('current_day', 1)}",
        f"- **Days completed:** {summary.get('days_completed', 0)}",
        f"  - Coding: {summary.get('coding_days_completed', 0)}",
        f"  - Aptitude: {summary.get('aptitude_days_completed', 0)}",
        f"- **Streak:** {summary.get('streak', 0)} days",
        f"- **Tests passed:** {summary.get('tests_passed', 0)}/{summary.get('tests_total', 0)}",
        f"- **Quiz score:** {summary.get('quiz_score', 0)}/{summary.get('quiz_total', 0)}",
        f"- **Mistakes logged:** {summary.get('mistake_count', 0)}",
        "",
        "## Badges",
        "",
    ]
    badges = summary.get("badges", [])
    if badges:
        for b in badges:
            lines.append(f"- {b}")
    else:
        lines.append("No badges yet. Start a day to earn your first badge.")

    lines.append("")
    return "\n".join(lines)


def write_report() -> Path:
    """Write a timestamped report to progress/reports/."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    summary = summarize_progress()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    report_path = REPORTS_DIR / f"report_{timestamp}.md"
    report_path.write_text(render_report_markdown(summary), encoding="utf-8")
    return report_path


def export_student_progress() -> Path:
    """Export progress data as a standalone JSON file."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    progress = _load_progress()
    summary = summarize_progress()
    export_data = {
        "exported_at": _now_iso(),
        "profile": progress,
        "summary": summary,
    }
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    export_path = REPORTS_DIR / f"export_{timestamp}.json"
    export_path.write_text(json.dumps(export_data, indent=2), encoding="utf-8")
    return export_path


def git_status_summary() -> str:
    """Return a short git status summary for student awareness."""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.stdout.strip():
            lines = result.stdout.strip().splitlines()
            count = len(lines)
            return f"You have {count} uncommitted file(s) in your repo."
        return "Your repo is clean — no uncommitted changes."
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return "Could not check git status (is this a git repo?)"
