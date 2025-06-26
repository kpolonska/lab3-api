from datetime import datetime
from pydantic import BaseModel


class UserDTO(BaseModel):
    id: str
    full_name: str
    