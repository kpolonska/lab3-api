import uuid
from dataclasses import dataclass

@dataclass
class Vocabulary:
    vocab_id: uuid.UUID
    vocab_name: str
    vocab_description: str
    owner_id: uuid.UUID
    owner_name: str
    students_count: int
    word_list: list
    language_to: str
    language_from: str
