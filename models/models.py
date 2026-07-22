from sqlalchemy import Column, Integer, String, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from enum import Enum

Base = declarative_base()

class Genre(str, Enum):
    MYSTERY = "mystery"
    ROMANCE = "romance"
    NONFICTION = "nonfiction"
    HISTORY = "history"
    FANTASY = "fantasy"
    CLASSIC = "classic"
    POLITICS = "politics"

class Author(Base):
    __tablename__ = "author"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), nullable=False)
    email = Column(String, nullable=False)
    
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "book"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(SQLEnum(Genre), nullable=False)
    page_count = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=True)
    
    author = relationship("Author", back_populates="books")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)