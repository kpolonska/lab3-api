from fastapi import FastAPI, Depends
from controller.notes_controller import router as notes_router
from service.notes_service import get_notes_service
from service.user_service import get_user_service

app = FastAPI( title="Awesome note-taking app", description="API for note-taking service", version="0.1.0")
app.include_router(notes_router)

import strawberry.fastapi
from graphqlapi.schema import schema

def get_graphql_context( 
                        notes_service = Depends(get_notes_service),
                        user_service = Depends(get_user_service)
                        ):
    return {"notes_service": notes_service, "user_service": user_service}

graphql_app = strawberry.fastapi.GraphQLRouter(
    schema=schema, 
    context_getter=get_graphql_context)
app.include_router(graphql_app, prefix="/graphql", tags=["graphql"])