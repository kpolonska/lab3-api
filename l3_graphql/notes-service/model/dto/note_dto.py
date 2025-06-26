
from datetime import datetime
from pydantic import BaseModel


class NoteDTO(BaseModel):
    id: str
    user_id: str
    content: str
    created_at: datetime
    tags: list[str] = []