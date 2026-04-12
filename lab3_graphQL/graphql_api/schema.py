import strawberry
from strawberry.types import Info

@strawberry.type
class WordType:
    id: str
    vocabulary_id: str 
    word_from_language: str
    word_to_language: str
    description: str
    language_from: str

@strawberry.type
class VocabularyType:
    id: str
    vocab_name: str
    vocab_description: str
    owner_id: str
    owner_name: str
    students_count: int
    language_to: str
    language_from: str

    @strawberry.field
    def words(self, info: Info) -> list[WordType]:
        word_service = info.context['word_service']
        words = word_service.get_words(self.id)
        if words:
            return [WordType(id=w.id, 
                            vocabulary_id=w.vocabulary_id, 
                            word_from_language = w.word_from_language,
                            word_to_language = w.word_to_language,
                            description = w.description,
                            language_from = w.language_from) for w in words]
        else:
            return []
        

@strawberry.type
class Query:
    @strawberry.field
    def vocabulary(self, info: Info, vocabulary_id: str) -> VocabularyType:
        vocab_service = info.context['vocabulary_service']
        v = vocab_service.get_vocabulary(vocabulary_id) 
        return VocabularyType(
            id=v.id,
            vocab_name=v.vocab_name,
            vocab_description=v.vocab_description,
            owner_id=str(v.owner_id),
            owner_name=v.owner_name,
            students_count=v.students_count,
            word_list=[],  
            language_to=v.language_to,
            language_from=v.language_from
        )

    @strawberry.field
    def words(self, info: Info, vocab_id: str) -> list[WordType]:
        word_service = info.context['word_service']
        words = word_service.get_words(vocab_id, page=1, size=10) ### CHANGE METHODS NAME AFTER SERVICES
        return [WordType(id=w.id, 
                            vocabulary_id=w.vocabulary_id, 
                            word_from_language = w.word_from_language,
                            word_to_language = w.word_to_language,
                            description = w.description,
                            language_from = w.language_from) for w in words]
    
    @strawberry.field
    def word(self, info: Info, vocab_id: str, word_id: str) -> Optional['WordType']:
        word_service = info.context['word_service']
        word = word_service.get_word(vocab_id, word_id)
        if word:
            return WordType(
                id=word.word_id,
                vocabulary_id=vocab_id,
                word_from_language=word.word_from_language,
                word_to_language=word.word_to_language,
                description=word.description,
                language_from=word.language_from)
        else:
            return []

        
schema = strawberry.Schema(query=Query)

