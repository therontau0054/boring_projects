"""Main entry point for the Jury Trial agent system.

Usage:
    python -m jury_trial.main                 # interactive mode (default case)
    python -m jury_trial.main --auto          # run without pauses
    python -m jury_trial.main --dry-run       # print prompts without API calls
    python -m jury_trial.main --case <id>     # select a specific case
    python -m jury_trial.main --list-cases    # list all available cases
    python -m jury_trial.main --lang zh       # discussion in Chinese (default)
    python -m jury_trial.main --lang en       # discussion in English
"""

import argparse
import io
import sys

from .cases import get_case, list_cases


def _fix_stdout_encoding():
    """Reconfigure stdout to UTF-8 so Unicode characters (em dashes, superscript,
    yen sign, etc.) don't crash on Windows terminals with GBK encoding."""
    if hasattr(sys.stdout, "buffer") and sys.stdout.encoding != "utf-8":
        try:
            sys.stdout = io.TextIOWrapper(
                sys.stdout.buffer, encoding="utf-8", errors="replace"
            )
        except Exception:
            pass  # best-effort; if it fails, print() may still error on some chars


def main():
    _fix_stdout_encoding()
    parser = argparse.ArgumentParser(
        description="Jury Trial — Multi-Agent Murder Mystery Deliberation"
    )
    parser.add_argument(
        "--auto", action="store_true",
        help="Run without waiting for user input between rounds."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print the structure and prompts without making API calls."
    )
    parser.add_argument(
        "--case", type=str, default="alpine_express", metavar="CASE_ID",
        help="Case to load (default: alpine_express)."
    )
    parser.add_argument(
        "--list-cases", action="store_true",
        help="List all available cases and exit."
    )
    parser.add_argument(
        "--lang", "-l", type=str, default="zh", choices=["en", "zh"],
        help="Discussion language: en (English) or zh (Chinese). Default: zh."
    )
    args = parser.parse_args()

    if args.list_cases:
        _list_cases()
        return

    # Load the case module
    try:
        case_mod = get_case(args.case)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    if args.dry_run:
        _dry_run(case_mod)
        return

    from .orchestrator import Orchestrator  # lazy import — needs API key

    orch = Orchestrator(case_mod, interactive=not args.auto, lang=args.lang)
    try:
        orch.run()
    except KeyboardInterrupt:
        print("\n\nTrial adjourned by user.")
        sys.exit(0)


def _list_cases():
    """Print all available cases."""
    print("Available cases:")
    for case_id, case_name in list_cases():
        print(f"  {case_id}: {case_name}")


def _dry_run(case_mod):
    """Show the discussion structure without calling the API."""
    from .prompts import AGENT_NAMES

    print("=" * 60)
    print("  DRY RUN — No API calls will be made")
    print("=" * 60)
    print(f"\n  Case: {case_mod.CASE_NAME}")
    print(f"  {case_mod.CASE_DESC}")
    print(f"\n  Model: see .env configuration")
    print(f"\n  Agents ({len(AGENT_NAMES)}):")
    for aid, name in AGENT_NAMES.items():
        print(f"    - {name}")

    rounds = case_mod.CLUES_BY_ROUND
    print(f"\n  Rounds: {len(rounds)} evidence rounds + final deliberation")
    for rn in sorted(rounds):
        c = rounds[rn]
        print(f"\n    Round {rn}: {c['title']} ({len(c['clues'])} clues)")
        for i, clue in enumerate(c["clues"], 1):
            print(f"      [{i}] {clue[:80]}...")

    print(f"\n  Discussion flow per round:")
    print(f"    1. Judge introduces evidence")
    for i, aid in enumerate(["prosecution", "defense", "forensic", "psychologist"], 2):
        print(f"    {i}. {AGENT_NAMES[aid]} responds")
    print(f"    6. Judge summarizes")
    print(f"\n  Final deliberation: each agent names the murderer.")
    print(f"\n  Total estimated API calls: ~{(len(rounds) * 6) + 5}")
    print(f"\n  Use --auto to run without pauses, or no flag for interactive mode.")


if __name__ == "__main__":
    main()
