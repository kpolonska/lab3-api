from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from graphql_api.schema import schema
from service.vocabulary_service import VocabularyService
from service.word_service import WordService

vocabulary_service = VocabularyService()
word_service = WordService()

app = FastAPI(title="Vocabulary App", description="Vocabulary app apishka", version="0.1.0")

def get_graphql_context():
    return {
        "vocabulary_service": vocabulary_service,
        "word_service": word_service
    }

graphql_app = GraphQLRouter(
    schema=schema,
    context_getter=get_graphql_context
)

app.include_router(graphql_app, prefix="/graphql", tags=["graphql"])