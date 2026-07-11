from pydantic import BaseModel, Field, field_validator
from enum import Enum

class Genre(str, Enum):

    HORROR = "horror"
    MYSTERY = "mystery"
    ROMANCE = "romance"
    NONFICTION = "nonfiction"
    HISTORY = "history"
    SCIFI = "science-fiction"
    FANTASY = "fantasy"
    FICTION = "fiction"
    CLASSIC = "classic"
    POLITICS = "politics"
    ROMCOM = "rom-com"

class Book(BaseModel):

    title: str
    author: str = Field(..., max_length=32)
    genre: list[Genre]
    page_count: int = Field(..., ge=30)
    ISBN: str = Field(None, min_length=16, max_length=32)

    @field_validator("ISBN")
    def verify_isbn(cls, v):
        if isinstance(v, str):
            return v.upper()
        return ValueError("ISBN should be of string format")