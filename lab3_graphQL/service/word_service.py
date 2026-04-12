import uuid
from lab3_graphQL.model.dto.word_dto import WordDTO

class WordService:
    
    def create_word(self, vocab_id, request_data) -> WordDTO:
        return WordDTO(
            id=str(uuid.uuid4()),
            vocabulary_id=vocab_id,
            word_from_language=request_data.word_from_language,
            word_to_language=request_data.word_to_language,
            description=request_data.description,
            language_from=request_data.language_from
        )
    
    def update_word(self, vocab_id, word_id, request_data) -> WordDTO:
        return WordDTO(
            id=word_id,
            vocabulary_id=vocab_id,
            word_from_language=request_data.word_from_language,
            word_to_language=request_data.word_to_language,
            description=request_data.description,
            language_from=request_data.language_from
        )
    
    def get_word(self, vocab_id, word_id) -> WordDTO:
        return WordDTO(
            id=word_id,
            vocabulary_id=vocab_id,
            word_from_language='apple',
            word_to_language='яблуко',
            description='A fruit',
            language_from='en'
        )
    
    def get_words(self, vocab_id) -> list[WordDTO]:
        return [self.get_word(vocab_id, str(uuid.uuid4()))]
    

def get_word_service() -> WordService:
    return WordService()     
    