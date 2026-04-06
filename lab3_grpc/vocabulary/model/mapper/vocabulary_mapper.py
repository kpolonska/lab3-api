import uuid
from vocabulary.model.dto.vocabulary import Vocabulary

class VocabularyMapper:
    def map_request(self, request_data):
        return Vocabulary(
            vocab_id=request_data.id or str(uuid.uuid4()),
            vocab_name=request_data.name,
            vocab_description='',
            owner_id=request_data.owner_id,
            owner_name='',
            students_count=0,
            word_list=list(request_data.word_list),
            language_to=request_data.language_to,
            language_from=request_data.language_from)
    
    def map_entity_to_dto(self, entity):
        return Vocabulary(
            vocab_id=entity.vocab_id,
            vocab_name=entity.vocab_name,
            vocab_description=entity.vocab_description,
            owner_id=entity.owner_id,
            owner_name=entity.owner_name,
            students_count=entity.students_count,
            word_list=entity.word_list,
            language_to=entity.language_to,
            language_from=entity.language_from
        )