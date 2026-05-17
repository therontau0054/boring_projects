#!/usr/bin/env python
"""Convenience launcher for the Jury Trial project.

Run from the project root:
    python run.py
    python run.py --auto
    python run.py --dry-run
"""

from jury_trial.main import main

if __name__ == "__main__":
    main()
