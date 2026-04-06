import uuid

from vocabulary.model.dto.vocabulary import Vocabulary
from vocabulary.model.mapper.vocabulary_mapper import VocabularyMapper
from models import Page

class VocabularyFilters:
    def __init__(self, owner_id=None, language_to=None, language_from=None):
        self.owner_id = owner_id
        self.language_to = language_to
        self.language_from = language_from

class VocabularyService:
    def __init__(self):
        self.vocabularies_mapper = VocabularyMapper()
        self.store: dict[str, Vocabulary] = {}
    
    def create_vocabulary(self, request_data) -> Vocabulary:
        if not request_data.name:
            raise ValueError("Vocabulary name is a required field.")

        vocabulary = self.vocabularies_mapper.map_request(request_data)
        vocabulary.vocab_id = str(uuid.uuid4())
        self.store[vocabulary.vocab_id] = vocabulary
        return vocabulary

    def update_vocabulary(self, vocab_id, request_data) -> Vocabulary:
        if not vocab_id:
            raise ValueError('Vocabulary id was not provided.')
        if vocab_id not in self.store:
            raise KeyError(f"Vocabulary {vocab_id} not found")
        
        vocabulary = self.vocabularies_mapper.map_request(request_data)
        vocabulary.vocab_id = vocab_id
        self.store[vocab_id] = vocabulary
        return vocabulary

    def get_vocabulary(self, vocabulary_id) -> Vocabulary:
        if vocabulary_id not in self.store:
            raise ValueError(f"Vocabulary {vocabulary_id} not found")
        
        return self.store[vocabulary_id]

    def get_vocabularies(self, filters: VocabularyFilters, page: int, size: int) -> Page[Vocabulary]:
        vocabs = list(self.store.values())

        if not any([filters.owner_id, filters.language_to, filters.language_from]):
            raise ValueError("Must provide at least one filter.")

        if filters.owner_id:
            vocabs = [v for v in vocabs if str(v.owner_id) == str(filters.owner_id)]
        if filters.language_to:
            vocabs = [v for v in vocabs if v.language_to == filters.language_to]
        if filters.language_from:
            vocabs = [v for v in vocabs if v.language_from == filters.language_from]

        start = (page - 1) * size
        chunk = vocabs[start:start + size]
        total_pages = max(1, -(-len(vocabs) // size))
        return Page(size=size, page=page, total_pages=total_pages, content=chunk)