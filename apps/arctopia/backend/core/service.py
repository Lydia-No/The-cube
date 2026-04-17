from core.models import ArcCase, ArcEvent, CreateCaseInput, CreateEventInput
from core.rules import validate_event_sequence
from core.store import JsonStore


class ArcService:
    def __init__(self):
        self.store = JsonStore()

    def create_case(self, data: CreateCaseInput) -> ArcCase:
        case = ArcCase(title=data.title, description=data.description)
        return self.store.create_case(case)

    def list_cases(self) -> list[ArcCase]:
        return self.store.list_cases()

    def get_case(self, case_id: str) -> ArcCase | None:
        return self.store.get_case(case_id)

    def list_case_events(self, case_id: str) -> list[ArcEvent]:
        return self.store.list_case_events(case_id)

    def create_event(self, data: CreateEventInput) -> ArcEvent:
        case = self.store.get_case(data.case_id)
        if not case:
            raise ValueError("Case not found.")

        existing = self.store.list_case_events(data.case_id)
        ok, msg = validate_event_sequence(existing, data.stage)
        if not ok:
            raise ValueError(msg)

        event = ArcEvent(
            case_id=data.case_id,
            stage=data.stage,
            title=data.title,
            content=data.content,
            source=data.source,
            parent_id=data.parent_id,
        )
        return self.store.create_event(event)

    def case_snapshot(self, case_id: str) -> dict:
        case = self.get_case(case_id)
        if not case:
            raise ValueError("Case not found.")

        events = self.list_case_events(case_id)
        return {
            "case": case.model_dump(),
            "events": [event.model_dump() for event in events],
            "event_count": len(events),
            "current_stage": events[-1].stage if events else None,
        }
