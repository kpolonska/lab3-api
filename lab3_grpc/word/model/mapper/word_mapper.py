import uuid
from word.model.dto.word import Word

class WordMapper:
    def map_request(self, request_data):
        return Word(
            word_id=request_data.id or str(uuid.uuid4()),
            vocabulary_id=request_data.vocabulary_id,
            word_from_language=request_data.word_from_language,
            word_to_language=request_data.word_to_language,
            description=request_data.description,
            language_from=''
        )
    
    def map_entity_to_dto(self, entity):
        return Word(
            word_id=entity.word_id,
            vocabulary_id=entity.vocabulary_id,
            word_from_language=entity.word_from_language,
            word_to_language=entity.word_to_language,
            description=entity.description,
            language_from=entity.language_from
        )