from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from .books import BookRead  

class AuthorBase(BaseModel):
    name: str = Field(..., max_length=32)
    email: EmailStr

class Author(AuthorBase):
    pass

class AuthorCreate(AuthorBase):
    pass

class AuthorRead(AuthorBase):
    id: int
    #books: Optional[list["BookRead"]] = []

    class Config:
        from_attributes = True