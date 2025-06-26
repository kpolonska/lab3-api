from fastapi import Request, APIRouter, Depends
from model.dto.note_dto import NoteDTO
from model.dto.user_dto import UserDTO
from service.notes_service import NotesService, get_notes_service
from service.user_service import UserService, get_user_service

router = APIRouter(prefix="/api", tags=["notes"])

@router.get("/user/{user_id}/notes")
def get_user(user_id: str, service: NotesService = Depends(get_notes_service))-> list[NoteDTO]:
    
    return service.get_user_notes(user_id)

@router.get("/user/{user_id}")
def get_user_info(user_id: str, service: UserService = Depends(get_user_service))-> UserDTO:
    
    return service.get_user(user_id)