import uuid
from lab3_graphQL.model.dto.vocabulary_dto import VocabularyDTO

class VocabularyService:
    
    def create_vocabulary(self, request_data) -> VocabularyDTO:
        return VocabularyDTO(
            id=str(uuid.uuid4()),
            vocab_name=request_data.vocab_name,
            vocab_description=request_data.vocab_description,
            owner_id=request_data.owner_id,
            owner_name=request_data.owner_name,
            students_count=0,
            word_list=[],
            language_to=request_data.language_to,
            language_from=request_data.language_from
        )
    
    def update_vocabulary(self, vocab_id, request_data) -> VocabularyDTO:
        return VocabularyDTO(
            id=vocab_id,
            vocab_name=request_data.vocab_name,
            vocab_description=request_data.vocab_description,
            owner_id=request_data.owner_id,
            owner_name=request_data.owner_name,
            students_count=0,
            word_list=[],
            language_to=request_data.language_to,
            language_from=request_data.language_from
        )
    
    def get_vocabulary(self, vocabulary_id) -> VocabularyDTO:
        return VocabularyDTO(
            id=vocabulary_id,
            vocab_name='some vocab',
            vocab_description='klknpkl',
            owner_id='1',
            owner_name='John',
            students_count=0,
            word_list=[],
            language_to='uk',
            language_from='en'
        )
    
    def get_vocabularies(self) -> list[VocabularyDTO]:
        return [self.get_vocabulary(str(uuid.uuid4()))]
    
def get_vocabulary_service() -> VocabularyService:
    return VocabularyService()     