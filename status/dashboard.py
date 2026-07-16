#!/usr/bin/env python3
"""
KPOS Progress Dashboard
Run: python3 status/dashboard.py
Output: Human-readable study progress
"""
import os
import json
from pathlib import Path

def load_student():
    """Load student progress data"""
    kpos_data = os.path.expanduser('~/.kpos')
    student_file = os.path.join(kpos_data, 'student.json')
    if not os.path.exists(student_file):
        return None
    try:
        with open(student_file) as f:
            return json.load(f)
    except:
        return None

def compute_confidence(progress):
    """Compute confidence score 0-100 based on progress"""
    if not progress or not progress.get('scores'):
        return 0
    
    scores = progress.get('scores', {})
    days_completed = len(scores)
    avg_score = sum(scores.values()) / max(1, len(scores))
    
    # Confidence is weighted by: coverage (40%) + average score (60%)
    coverage = min(100, days_completed / 10 * 100)
    score_weighted = avg_score / 10 * 60
    confidence = min(100, int(coverage * 0.4 + score_weighted))
    
    return confidence

def get_recommended_day(progress):
    """Get recommended next action"""
    if not progress:
        return "Start Day 1"
    
    scores = progress.get('scores', {})
    days_completed = progress.get('days_completed', [])
    weak_topics = progress.get('weak_topics', [])
    next_day = progress.get('next_day', 1)
    
    if len(days_completed) == 0:
        return "Start Day 1"
    
    avg_score = sum(scores.values()) / max(1, len(scores))
    
    if avg_score >= 8:
        return f"Day {next_day} (you're ready!)"
    elif weak_topics:
        return f"Review: {weak_topics[-1]} (from wrong answers)"
    elif avg_score >= 6:
        return f"Day {next_day} (review weak spots first)"
    else:
        return f"Review Day {min(days_completed, 5)} (focus on weak topics)"

def main():
    progress = load_student()
    
    print("═══════════════════════════════════════")
    print("         KPOS — Placement Prep Status")
    print("═══════════════════════════════════════")
    print()
    
    if not progress:
        print("No progress recorded yet.")
        print("Run: python3 scripts/check-ready.py")
        print("\nTo start studying, follow START.md")
        return
    
    # Compute stats
    days_completed = progress.get('days_completed', [])
    scores = progress.get('scores', {})
    weak_topics = progress.get('weak_topics', [])
    coverage = len(scores)
    avg_score = sum(scores.values()) / max(1, len(scores)) if scores else 0
    confidence = compute_confidence(progress)
    
    # Print progress
    print(f"Days Completed:        {coverage}/10")
    print(f"Average Score:         {avg_score:.1f}/10")
    print(f"Confidence Level:      {confidence}/100")
    print(f"Weak Topics:           {weak_topics[:3] if weak_topics else 'None'}")
    print()
    
    # Per-day breakdown
    if scores:
        print("Score History:")
        for day_name, score in scores.items():
            bar = "#" * (score * 2) + "." * (20 - score * 2)
            status = "✓" if score >= 7 else "-" if score >= 5 else "x"
            print(f"  [{status}] {day_name:30} {score}/10  |{bar}")
        print()
    
    # Recommendation
    recommended = get_recommended_day(progress)
    print(f"Recommended:           {recommended}")
    print()
    print("═══════════════════════════════════════")
    print("  Tip: Be consistent. 30 min daily > 4 hrs on weekends.")
    print("════════════════════════════════════════════════")

if __name__ == '__main__':
    main()
