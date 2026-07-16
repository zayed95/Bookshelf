#from pydantic import BaseModel, Field, ConfigDict
from email.policy import default

from sqlmodel import Field, Session, SQLModel
from enum import Enum
from typing import Optional

class Genre(str, Enum):

    MYSTERY = "mystery"
    ROMANCE = "romance"
    NONFICTION = "nonfiction"
    HISTORY = "history"
    FANTASY = "fantasy"
    CLASSIC = "classic"
    POLITICS = "politics"

class BookBase(SQLModel):

    title: str
    author: str = Field(..., max_length=32)
    genre: Genre
    page_count: int = Field(..., ge=30)

class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 

class PartialUpdateBook(SQLModel):

    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[Genre] = None
    page_count: Optional[int] = None


class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int
