from datetime import datetime
from pydantic import BaseModel
from lab3_graphQL.model.dto.word_dto import WordDTO


class VocabularyDTO(BaseModel):
    id: str
    vocab_name: str
    vocab_description: str
    owner_id: str
    owner_name: str
    students_count: int
    word_list: list[WordDTO] = []
    language_to: str
    language_from: str