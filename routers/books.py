from sqlmodel import select
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Book, Genre
from schemas.books import PartialUpdateBook, BookCreate, BookRead
from db.db import get_session
from typing import Optional

router = APIRouter(
    prefix="/books",
    tags=["books"]
    )

async def get_book_or_404(book_id: int, 
                          session: AsyncSession = Depends(get_session)) -> Book:
    book = await session.get(Book, book_id)
    
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Book not found")
    return book   
    

@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def create_book(book_create: BookCreate,
                    session: AsyncSession = Depends(get_session)) -> Book:

    db_book = Book(**book_create.model_dump())
    session.add(db_book)
    await session.commit()
    await session.refresh(db_book)
    return db_book



@router.get("/", response_model=list[BookRead])
async def get_all_books(genre: Optional[Genre] = None, author_id: Optional[int] = None, 
                        session: AsyncSession = Depends(get_session)) -> list[BookRead]:
    
    books = await session.execute(select(Book))

    if genre:
        books = await session.execute(select(Book).where(Book.genre == genre))

    if author_id:
        books = await session.execute(select(Book).where(Book.author_id == author_id))
    
    books = books.scalars().all()

    if not books or len(books) == 0:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "No books on the bookshelf"}
        )

    return books

 

@router.get("/{book_id}", response_model=BookRead)
async def get_book(book: Book = Depends(get_book_or_404)) -> Book:
    return book


    
@router.patch("/{book_id}", response_model=BookRead)
async def partial_update_book(book_update: PartialUpdateBook,
                            book: Book = Depends(get_book_or_404), 
                            session: AsyncSession = Depends(get_session)):

    book_data = book_update.model_dump(exclude_unset=True)
    book.sqlmodel_update(book_data)
    
    await session.commit()
    await session.refresh(book)

    return book


@router.delete("/{book_id}")
async def delete_book(book_db: Book = Depends(get_book_or_404), 
                            session: AsyncSession = Depends(get_session)):

    await session.delete(book_db)
    await session.commit()
    
    return JSONResponse(
        content={"message": "book deleted successflly"}
    )