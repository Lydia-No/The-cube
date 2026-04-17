from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime, UTC
from uuid import uuid4


Stage = Literal["activity", "evidence", "assessment", "verification", "recognition"]


class ArcEvent(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())
    case_id: str
    stage: Stage
    title: str
    content: str
    source: Optional[str] = None
    parent_id: Optional[str] = None


class ArcCase(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())
    title: str
    description: str = ""
    status: str = "open"


class CreateCaseInput(BaseModel):
    title: str
    description: str = ""


class CreateEventInput(BaseModel):
    case_id: str
    stage: Stage
    title: str
    content: str
    source: Optional[str] = None
    parent_id: Optional[str] = None
