from model.dto.note_dto import NoteDTO

class NotesService:
    
    def get_user_notes(self, user_id: str) -> list[NoteDTO]:    
        return self._get_stub_notes(user_id)
    
    def _get_stub_notes(self, user_id: str) -> list[NoteDTO]:
        return [
            NoteDTO(
                id='some-id',
                user_id=user_id,
                content="This is a stub note",
                created_at="2023-10-01T12:00:00Z",
                tags=["stub", "example"]
            )
        ]
def get_notes_service() -> NotesService:
    return NotesService()        
