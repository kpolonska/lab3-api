from datetime import datetime
from pydantic import BaseModel
from model.dto.word_dto import WordDTO


class VocabularyDTO(BaseModel):
    id: str
    vocab_name: str
    vocab_description: str
    owner_id: str
    owner_name: str
    students_count: int
    language_to: str
    language_from: str