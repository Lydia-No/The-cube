from core.models import ArcEvent

STAGE_ORDER = {
    "activity": 0,
    "evidence": 1,
    "assessment": 2,
    "verification": 3,
    "recognition": 4,
}


def validate_event_sequence(existing_events: list[ArcEvent], new_stage: str) -> tuple[bool, str]:
    if not existing_events:
        if new_stage != "activity":
            return False, "A case must begin with activity."
        return True, "ok"

    highest_existing = max(STAGE_ORDER[event.stage] for event in existing_events)
    requested = STAGE_ORDER[new_stage]

    if requested > highest_existing + 1:
        return False, "Sequence violation: stage cannot skip required prior stages."

    return True, "ok"
