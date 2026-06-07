#!/usr/bin/env bash
# KPOS Setup Script — One-time configuration for all students
# Handles: Python detection, progress folder creation, validation
# Designed for non-CS students: minimal errors, clear messages

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "═══════════════════════"
echo "  KPOS — Setup Complete"
echo "═══════════════════════"
echo ""

# Check Python 3
if command -v python3 &>/dev/null; then
    echo "  ✓ Python 3 found"
else
    echo "  ✗ Python 3 not found. Install Python 3.8+ from python.org"
    exit 1
fi

# Check and create progress folder
KPOS_DATA="$HOME/.kpos"
if [ ! -d "$KPOS_DATA" ]; then
    mkdir -p "$KPOS_DATA"
    echo "  ✓ Progress folder created at $KPOS_DATA"
else
    echo "  ✓ Progress folder already exists"
fi

# Check critical files
if [ -f "$SCRIPT_DIR/scripts/check-ready.py" ]; then
    echo "  ✓ Validator ready"
else
    echo "  ✗ Missing: scripts/check-ready.py"
    exit 1
fi

echo ""
echo "╔═════════════════════════════════════════╗"
echo "║  You're ready! Open START.md to begin  ║"
echo "╚═════════════════════════════════════════╝"
echo ""
