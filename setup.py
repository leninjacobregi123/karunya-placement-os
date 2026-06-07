#!/usr/bin/env python3
"""
KPOS Universal Setup — Works on Windows, Mac, Linux
Handles: Python detection, Git check, progress folder, first-run config
"""

import sys
import os
import json
import shutil
import subprocess

def main():
    print("═══ KPOS — Setup ═══")
    print()
    
    # Check Python version
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"Python {version} ✓")
    
    # Check Git
    git_installed = False
    git_msg = "Not installed"
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            git_installed = True
            git_msg = result.stdout.strip()
    except FileNotFoundError:
        pass
    
    if git_installed:
        print(f"Git ✓ ({git_msg})")
    else:
        print("Git ✗ (needed for updates)")
        print("  - Windows: https://git-scm.com/download/win")
        print("  - Mac: brew install git")
        print("  - Linux: sudo apt install git")
    
    # Create progress path
    kpos_data = os.path.expanduser('~/.kpos')
    if not os.path.exists(kpos_data):
        os.makedirs(kpos_data)
        # Write default progress file
        default = {
            'name': '',
            'path': '',  # '' = not set (needs selection)
            'days_completed': [],
            'scores': [],
            'weak_topics': [],
            'next_day': 1
        }
        with open(os.path.join(kpos_data, 'student.json'), 'w') as f:
            json.dump(default, f, indent=2)
        print(f"\nProgress saved to: {kpos_data}")
    else:
        print(f"Progress file already exists")
    
    print("\n═══ Setup Complete ═══")
    print("Open START.md to begin Day 1")

if __name__ == '__main__':
    main()
