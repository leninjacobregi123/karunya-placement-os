#!/usr/bin/env python3
"""
KPOS Answer Validator & Progress Tracker
Run: python3 scripts/check-ready.py
Reads: daily/NN-slug/answers.json + answer-key.json
Writes: ~/.kpos/student.json
Output: Score + recommendations
"""
import sys
import os
import json
import re
import pathlib
import pathlib as pb
from pathlib import Path

def load_file(path):
    """Load JSON file safely"""
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {path} not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: {path} has invalid JSON")
        return None

def check_answer(expected, actual, qtype="exact"):
    """Check if answer matches (exact, pattern, or numeric)"""
    if not actual or not expected:
        return False
    
    actual = str(actual).strip()
    expected = str(expected).strip()
    
    if qtype == "exact":
        return actual == expected
    elif qtype == "pattern":
        try:
            # Convert our simple patterns to regex
            pattern = expected
            if ".." in pattern:
                pattern = pattern.replace("..", ".*")
            regex = re.compile(pattern)
            return bool(regex.search(actual))
        except:
            return False
    elif qtype == "numeric":
        try:
            tolerance = 0.01
            exp_val = float(expected)
            actual_val = float(actual)
            return abs(exp_val - actual_val) <= tolerance
        except:
            return False
    return False

def get_current_day():
    """Find which day we should be on"""
    kpos_data = os.path.expanduser('~/.kpos')
    student_file = os.path.join(kpos_data, 'student.json')
    if os.path.exists(student_file):
        progress = load_file(student_file)
        if progress:
            days_completed = progress.get('days_completed', [])
            return max([0] + days_completed) + 1
    return 1  # Default to day 1

def main():
    # Find the project root (where this script lives)
    script_dir = Path(__file__).parent.parent
    
    # Get current day
    current_day = get_current_day()
    
    # Look for daily folder
    daily_dir = script_dir / 'daily'
    daily_folders = [d for d in daily_dir.iterdir() if d.is_dir()]
    if not daily_folders:
        print("Error: No daily folders found in daily/")
        print("Run ./setup.sh first")
        sys.exit(1)
    
    # Find current day folder (by number or slug)
    target_folder = None
    target_slug = None
    
    # Try to match current day number
    for folder in sorted(daily_folders):
        folder_name = folder.name
        # Check if folder starts with current day number
        if folder_name.startswith(f"{current_day:02d}-"):
            target_folder = folder
            target_slug = folder_name
            break
    
    if not target_folder:
        # Try first available
        target_folder = sorted(daily_folders)[0]
        target_slug = target_folder.name
        print(f"Note: Day {current_day} not found. Opening first available: {target_slug}")
    
    print(f"=== KPOS Study Day ===")
    print(f"Opening: {target_slug}")
    print()
    
    # Load answers
    answers_file = target_folder / 'answers.json'
    key_file = target_folder / 'answer-key.json'
    
    if not answers_file.exists():
        print(f"answers.json not found in {target_slug}/")
        print("Paste the prompt from claude_code.md into your AI, complete all exercises, then paste your answers here.")
        sys.exit(1)
    
    answers = load_file(answers_file)
    answer_key = load_file(key_file)
    
    if not answers or not answer_key:
        print("Error loading files. Run setup.sh first.")
        sys.exit(1)
    
    # Grade answers
    total = len(answer_key)
    correct = 0
    topics = []
    
    for qid in answer_key:
        qdata = answer_key[qid]
        qtype = qdata.get('type', 'exact')
        expected = qdata['expected']
        
        actual = answers.get(qid, '')
        is_correct = check_answer(expected, actual, qtype)
        correct += 1 if is_correct else 0
        topics.append({
            'id': qid,
            'correct': is_correct,
            'expected': expected,
            'actual': actual
        })
    
    score = int((correct / total) * 10) if total > 0 else 0
    
    # Display results
    print(f"Score: {correct}/{total} ({score}/10)")
    print()
    
    # Show weak areas
    wrong = [t for t in topics if not t['correct']]
    if wrong:
        print("Review needed:")
        for w in wrong:
            print(f"  x {w['id']}: got '{w['actual']}', expected '{w['expected']}'")
        print()
    else:
        print("All correct! Well done.")
        print()
    
    # Recommendations
    if score >= 7:
        feedback = "Strong work! You're ready to attempt Day 2."
    elif score >= 4:
        feedback = "Review the wrong topics above, try them again, then submit."
    else:
        feedback = "Take your time. Re-read the README section on weak topics, then try the wrong exercises again."
    
    print(f"Next: {feedback}")
    print()
    
    # Update progress
    kpos_data_path = os.path.expanduser('~/.kpos')
    student_file = os.path.join(kpos_data_path, 'student.json')
    
    # Load or create student progress
    progress = {}
    if os.path.exists(student_file):
        progress = load_file(student_file) or {}
    
    # Update progress
    if 'days_completed' not in progress:
        progress['days_completed'] = []
    if current_day not in progress['days_completed']:
        progress['days_completed'].append(current_day)
    
    if 'scores' not in progress:
        progress['scores'] = {}
    progress['scores'][target_slug] = score
    
    # Update next day
    progress['next_day'] = current_day + 1
    
    if 'weak_topics' not in progress:
        progress['weak_topics'] = []
    for w in wrong:
        if w['id'] not in progress['weak_topics']:
            progress['weak_topics'].append(w['id'])
    
    # Always save
    progress['last_day'] = target_slug
    progress['overall_score'] = int(sum(progress['scores'].values()) / max(1, len(progress['scores'])))
    
    with open(student_file, 'w') as f:
        json.dump(progress, f, indent=2)
    
    print(f"Progress saved to: {student_file}")

if __name__ == '__main__':
    main()
