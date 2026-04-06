import uuid
from dataclasses import dataclass

@dataclass
class Word:
    word_id: uuid.UUID
    vocabulary_id: str
    word_from_language: str
    word_to_language: str
    description: str
    language_from: str