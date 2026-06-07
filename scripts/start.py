"""
KPOS /start Command Handler

Use: When student types /start [path] in Claude Code

This script:
1. Checks Python environment
2. Creates progress file if needed
3. Auto-detects which day to start
4. Loads the lesson directory
5. Returns progress object for further use
"""
import os
import json
import subprocess
import sys
from pathlib import Path


def get_python_version():
    """Check Python 3 is installed"""
    try:
        ver = subprocess.run(
            ['python3', '--version'],
            capture_output=True, text=True, timeout=5
        )
        if ver.returncode == 0:
            return ver.stdout.strip()
    except:
        pass
    return None


def create_or_load_progress(base_dir):
    """Create or load student progress file"""
    kpos_dir = os.path.expanduser('~/.kpos')
    student_file = os.path.join(kpos_dir, 'student.json')
    
    if not os.path.exists(student_file):
        os.makedirs(kpos_dir, exist_ok=True)
        progress = {
            'name': '',
            'path': '',
            'days_completed': [],
            'scores': {},
            'current_day': 1,
            'weak_topics': [],
            'last_day': None
        }
        with open(student_file, 'w') as f:
            json.dump(progress, f, indent=2)
        return progress
    
    with open(student_file) as f:
        return json.load(f)


def auto_detect_day(progress, daily_dir):
    """Auto-detect which day to work on"""
    days_completed = progress.get('days_completed', [])
    
    if not days_completed:
        # First time - start day 01
        return daily_dir / '01-python-basics'
    
    # Map day numbers to folder names
    folder_map = {}
    for d in daily_dir.iterdir():
        if d.is_dir():
            name = d.name
            if name.startswith('0') or name.startswith('0'):
                day_num = int(name[:2])
                folder_map[day_num] = d
    
    # Get current day
    current = max(days_completed) if days_completed else 1
    
    # Look for next folder
    next_num = current + 1
    return folder_map.get(next_num, daily_dir / '01-python-basics')


def main():
    base_dir = Path(__file__).parent.parent
    daily_dir = base_dir / 'daily'
    
    # Check Python
    py_ver = get_python_version()
    if not py_ver:
        print("ERROR: Python 3 not found")
        print("Install Python 3.8+:")
        print("  Windows: https://python.org")
        print("  Mac: brew install python3")
        print("  Linux: sudo apt install python3")
        sys.exit(1)
    
    print("Environment OK")
    
    # Load/create progress
    progress = create_or_load_progress(base_dir)
    
    # Auto-detect day
    if not progress.get('days_completed'):
        target = daily_dir / '01-python-basics'
    else:
        target = auto_detect_day(progress, daily_dir)
    
    print("Ready for Day 1!")
    print("Start exercises in:", target.name)
    
    return progress


if __name__ == '__main__':
    main()
