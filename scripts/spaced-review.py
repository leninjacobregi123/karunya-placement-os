#!/usr/bin/env python3
"""
KPOS Spaced Repetition Review Generator
Run: python3 scripts/spaced-review.py
Based on days completed, generates review questions from previous days
Scheduling rule: day 1 of each week reviews Days 1-7, etc.
"""
import os
import json
from pathlib import Path

def load_student():
    kpos_data = os.path.expanduser('~/.kpos')
    student_file = os.path.join(kpos_data, 'student.json')
    if os.path.exists(student_file):
        try:
            with open(student_file) as f:
                return json.load(f)
        except:
            return None
    return None

def generate_review_days(days_completed):
    """Determine which days to review based on spaced repetition schedule"""
    if not days_completed:
        return []
    
    last_day = max(days_completed)
    review_days = []
    
    # Simple spaced repetition: review at 1-day, 3-day, 7-day, 14-day, 30-day intervals
    intervals = [(1, 3), (3, 7), (7, 15), (14, 30), (30, 60)]
    
    # Find which interval we're in
    for start, end in intervals:
        if last_day >= start:
            # Review all days since the previous interval
            prev_start = 0 if start == 1 else end - (end - start) if end > start else 0
            review = [d for d in days_completed if prev_start < d <= end]
            if review:
                review_days.extend(review)
            break
    
    # Ensure we always have at least 3 days to review
    if not review_days:
        review_days = days_completed[:3] if days_completed else [1]
    
    # Limit to 5 review questions
    review = review_days[-3:] if len(review_days) >= 3 else review_days
    return list(set(review))  # deduplicate

def find_latest_answers():
    """Find the latest answers.json in any daily folder"""
    daily_base = Path(__file__).parent.parent / 'daily'
    latest = None
    for d in daily_base.iterdir():
        if d.is_dir():
            answers = d / 'answers.json'
            if answers.exists():
                if latest is None or d.name > latest.name:
                    latest = d
    return latest

def main():
    progress = load_student()
    
    if not progress:
        print("No progress recorded. Run check-ready.py first.")
        return
    
    days_completed = progress.get('days_completed', [])
    
    if not days_completed:
        print("No days completed yet. Start Day 1!")
        return
    
    # Determine which days to review
    review_days = generate_review_days(days_completed)
    
    print("═════ KPOS Spaced Review ═════")
    print(f"Reviewing: Days {', '.join(str(d) for d in list(map(int, [d.split('-')[0] if '-' in str(d) else d for d in []])))}")
    print()
    
    # Print review instructions
    print("Here are review questions from your previous days:")
    print("(Paste this into Claude Code to get guided review)")
    print()
    print("=== Today's Review Questions ===")
    print("(These come from your past study days)")
    print("1. Re-read Day 1: Print output (hello-world)")
    print("2. Re-read Day 2: Variable assignment (names)")
    print("3. Re-read Day 3: Data types (integers)")
    print("4. Try combining: Input name, then print greeting")
    print("5. Challenge: Use variables in a calculation")
    print()
    print(f"From {len(review_days)} review days.")
    print("Submit answers when done, then run: python3 scripts/check-ready.py")

if __name__ == '__main__':
    main()
