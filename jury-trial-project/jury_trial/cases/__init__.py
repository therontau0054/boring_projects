"""Case library — each module exports CLUES_BY_ROUND, TRUTH, CASE_NAME, CASE_DESC."""

from . import alpine_express, decagon_island, wedding_chamber

CASES = {
    "alpine_express": alpine_express,
    "decagon_island": decagon_island,
    "wedding_chamber": wedding_chamber,
}


def list_cases():
    """Return [(case_id, case_name), ...] for all available cases."""
    return [(cid, mod.CASE_NAME) for cid, mod in CASES.items()]


def get_case(case_id: str):
    """Load a case module by its ID."""
    if case_id not in CASES:
        available = ", ".join(CASES.keys())
        raise ValueError(f"Unknown case '{case_id}'. Available: {available}")
    return CASES[case_id]
