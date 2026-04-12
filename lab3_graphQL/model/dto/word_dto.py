from datetime import datetime
from pydantic import BaseModel


class WordDTO(BaseModel):
    id: str
    vocabulary_id: str 
    word_from_language: str
    word_to_language: str
    description: str
    language_from: str