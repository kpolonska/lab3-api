import strawberry
from strawberry.types import Info

from typing import List, Optional
from datetime import datetime

@strawberry.type
class NoteType:
    id: str
    user_id: str
    content: str
    created_at: str
    tags: List[str]
    @strawberry.field
    def user(self, info: Info) -> Optional['UserType']:
        user_service = info.context['user_service']
        user = user_service.get_user(self.user_id)
        if user:
            return UserType(
                id=user.id,
                full_name=user.full_name
            )
        return None

@strawberry.type
class UserType:
    id: str
    full_name: str

    @strawberry.field
    def notes(self, info: Info) -> List[NoteType]:
        notes_service = info.context['notes_service']
        notes = notes_service.get_user_notes(self.id)
        return [
            NoteType(
                id = n.id,
                user_id=n.user_id,
                content=n.content,
                created_at=n.created_at.isoformat() if hasattr(n.created_at, "isoformat") else str(n.created_at),
                tags=n.tags
            ) for n in notes #todo extract to mapper class
        ]

@strawberry.type
class Query:
    @strawberry.field
    def user(self, info: Info, user_id: str) -> UserType:
        user_service = info.context['user_service']
        user = user_service.get_user(user_id)
        return UserType(
            id=user.id,
            full_name=user.full_name
            )
    
    @strawberry.field
    def notes(self, info: Info, user_id: str) -> list[NoteType]:
        notes_service = info.context['notes_service']
        notes = notes_service.get_user_notes(user_id)
        return [
            NoteType(
                id=n.id,
                user_id=n.user_id,
                content=n.content,
                created_at=n.created_at,
                tags=n.tags
            ) for n in notes #todo extract to mapper class
        ]
        
        

schema = strawberry.Schema(query=Query)
