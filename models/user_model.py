from typing import Optional
from pydantic import BaseModel, Field
import utils


class UserBase(BaseModel):
    email: str

class UserLogin(UserBase):
    password: str

class UserRegister(UserBase):
    id: Optional[str] = None
    password: str

class UserOut(UserBase):
    id: str
    created_at: str
    game_level: str
    