import uuid

from word.model.dto.word import Word
from word.model.mapper.word_mapper import WordMapper
from models import Page

class WordFilters:
    def __init__(self, word_id):
        self.word_id = word_id

class WordService:
    def __init__(self, vocabulary_service):
        self.word_mapper = WordMapper()
        self.store: dict[str, list[Word]] = {}
        self.vocabulary_service = vocabulary_service
    
    def create_word(self, vocab_id, request_data) -> Word:
        if not vocab_id:
            raise ValueError('Vocabulary id for word creation must be provided.')

        word = self.word_mapper.map_request(request_data)
        word.word_id = str(uuid.uuid4())
        if vocab_id not in self.store:
            self.store[vocab_id] = []
        self.store[vocab_id].append(word)

        #add this word to respective vocab word list
        vocab = self.vocabulary_service.get_vocabulary(vocab_id)
        vocab.word_list.append(word)

        return word

    def update_word(self, vocab_id, word_id, request_data) -> Word:
        if not vocab_id:
            raise ValueError('Vocabulary id for word updating must be provided.')
        
        words = self.store.get(vocab_id, [])

        for i, w in enumerate(words):
            if str(w.word_id) == str(word_id):
                updated = self.word_mapper.map_request(request_data)
                updated.word_id = word_id
                words[i] = updated
                return updated
            
        raise ValueError(f"Word {word_id} not found")

    def get_word(self, vocab_id, word_id) -> Word:
        if not vocab_id:
            raise ValueError('Vocabulary id for word searching must be provided.')
        words = self.store.get(vocab_id, [])
        for w in words:
            if str(w.word_id) == str(word_id):
                return w
        raise KeyError(f"Word {word_id} not found")

    def get_words(self, vocab_id, page: int, size: int) -> Page[Word]:
        if not vocab_id:
            raise ValueError('Vocabulary id for word searching must be provided.')
        words = self.store.get(vocab_id, [])
        start = (page - 1) * size
        chunk = words[start:start + size]
        total_pages = max(1, -(-len(words) // size))
        return Page(size=size, page=page, total_pages=total_pages, content=chunk)

    