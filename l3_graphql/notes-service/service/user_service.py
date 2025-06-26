from model.dto.user_dto import UserDTO

class UserService:
    
    def get_user(self, user_id: str) -> list[UserDTO]:    
        return UserDTO(
            id=user_id,
            full_name="Markiyan"
        )
    
    
def get_user_service() -> UserService:
    return UserService()        
