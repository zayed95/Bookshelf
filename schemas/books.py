from pydantic import BaseModel, Field
from typing import Optional
from models.models import Genre

class BookBase(BaseModel):
    title: str
    genre: Genre
    page_count: int = Field(..., ge=30)
    author_id: Optional[int] = None

class Book(BookBase):
    pass

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int
    #author: str

    class Config:
        from_attributes = True

class PartialUpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None 
    genre: Optional[Genre] = None
    page_count: Optional[int] = None