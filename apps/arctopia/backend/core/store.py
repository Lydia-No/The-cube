import json
from pathlib import Path
from typing import List, Dict, Any

from core.models import ArcCase, ArcEvent


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CASES_FILE = DATA_DIR / "cases.json"
EVENTS_FILE = DATA_DIR / "events.json"


class JsonStore:
    def __init__(self):
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if not CASES_FILE.exists():
            CASES_FILE.write_text("[]", encoding="utf-8")
        if not EVENTS_FILE.exists():
            EVENTS_FILE.write_text("[]", encoding="utf-8")

    def _read_json(self, path: Path) -> List[Dict[str, Any]]:
        return json.loads(path.read_text(encoding="utf-8"))

    def _write_json(self, path: Path, data: List[Dict[str, Any]]) -> None:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    def list_cases(self) -> List[ArcCase]:
        return [ArcCase(**item) for item in self._read_json(CASES_FILE)]

    def get_case(self, case_id: str) -> ArcCase | None:
        for case in self.list_cases():
            if case.id == case_id:
                return case
        return None

    def create_case(self, case: ArcCase) -> ArcCase:
        cases = self._read_json(CASES_FILE)
        cases.append(case.model_dump())
        self._write_json(CASES_FILE, cases)
        return case

    def list_events(self) -> List[ArcEvent]:
        return [ArcEvent(**item) for item in self._read_json(EVENTS_FILE)]

    def list_case_events(self, case_id: str) -> List[ArcEvent]:
        events = [event for event in self.list_events() if event.case_id == case_id]
        return sorted(events, key=lambda e: e.created_at)

    def create_event(self, event: ArcEvent) -> ArcEvent:
        events = self._read_json(EVENTS_FILE)
        events.append(event.model_dump())
        self._write_json(EVENTS_FILE, events)
        return event
