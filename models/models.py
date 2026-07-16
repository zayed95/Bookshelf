import sqlalchemy as sa
from sqlalchemy import  Integer, String, Column
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

# Base = declarative_base()

# class Book(Base):
#     __tablename__ = "books"

#     #id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     id = Column('id', Integer, primary_key=True, autoincrement=True)
#     #title: Mapped[str] = mapped_column(String(255), nullable=False)
#     title = Column('title', String(255), nullable=False)
#     #genre: Mapped[str] = mapped_column(String(255), nullable=False)
#     genre = Column('genre', String(255), nullable=False)
#     #page_count: Mapped[int] = mapped_column(Integer, nullable=False)
#     page_count = Column('page_count', Integer)

#     metadata_ = Column('metadata', sa.JSON)