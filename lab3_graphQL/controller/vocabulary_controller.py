from fastapi import Request, APIRouter, Depends
from model.dto.vocabulary_dto import VocabularyDTO
from model.dto.word_dto import WordDTO
from service.vocabulary_service import VocabularyService, get_vocabulary_service
from service.word_service import WordService, get_word_service


router = APIRouter(prefix="/api", tags=["vocabularies"])

@router.get("/vocabulary/{vocab_id}/words")
def get_words(vocab_id: str, service: WordService = Depends(get_word_service))-> list[WordDTO]:
    return service.get_words(vocab_id)

@router.get("/vocabulary/{vocab_id}")
def get_vocabulary(vocab_id: str, service: VocabularyService = Depends(get_vocabulary_service))-> VocabularyDTO:
    return service.get_vocabulary(vocab_id)