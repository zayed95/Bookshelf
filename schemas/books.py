from email.policy import default

from sqlmodel import Field, SQLModel, Relationship
from enum import Enum
from typing import Optional, List
from pydantic import EmailStr

class Genre(str, Enum):

    MYSTERY = "mystery"
    ROMANCE = "romance"
    NONFICTION = "nonfiction"
    HISTORY = "history"
    FANTASY = "fantasy"
    CLASSIC = "classic"
    POLITICS = "politics"

class AuthorBase(SQLModel):
    name: str = Field(..., max_length=32)
    email: EmailStr

class Author(AuthorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    books: List["Book"] = Relationship(back_populates="author")

class AuthorRead(AuthorBase):
    id: int

class AuthorCreate(AuthorBase):
    pass

class BookBase(SQLModel):

    title: str
    genre: Genre
    page_count: int = Field(..., ge=30)
    author_id: Optional[int] = Field(default=None, foreign_key="author.id")

class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    author: Optional[Author] = Relationship(back_populates="books")

class PartialUpdateBook(SQLModel):

    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[Genre] = None
    page_count: Optional[int] = None


class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int
