import random
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from schemas.books import Book, Genre, PartialUpdateBook
from db import db

router = APIRouter(
    prefix="/books",
    tags=["books"]
    )

@router.post("/")
async def create_book(book: Book):

    id = int(random.random() * 100)

    if id in db.books.keys():
        return {"message": "book already exists"}
    
    db.books[id] = book

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": "book added succesfully!",
            "id": id
        }
    )


@router.get("/")
async def get_all_books(genre: Genre | None = None):

    if genre:
        return [book for book in db.books.values() if genre in book.genre]
    
    books = [book for book in db.books.values()]

    if not books or len(books) == 0:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "No books on the bookshelf"}
        )
    
    return books
    

@router.get("/{book_id}")
async def get_book(book_id: int):

    book = db.books.get(book_id)
    
    if not book:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "This book does not exist."}
        )
    
    return book


@router.put("/{book_id}")
async def update_book(book_update: Book, book_id: int):

    try:

        db.books[book_id] = book_update
        return {"message": "Book has been updated"}
    
    except:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "This book does not exist"}
        )
    
@router.patch("/{book_id}")
async def partial_update_book(book_update: PartialUpdateBook, book_id: int):

    book = db.books.get(book_id)
    
    if not book:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "This book does not exist."}
        )
    
    book_dict = book_update.dict(exclude_unset=True)
    updated_book = book.copy(update=book_dict)

    db.books[book_id] = updated_book

    return updated_book


@router.delete("/{book_id}")
async def delete_book(book_id: int):
    try: 
        db.books.pop(book_id, None)
        return JSONResponse(
           # status_code=status.HTTP_204_NO_CONTENT,
            content={"message": "book deleted successflly"}
        )
    
    except:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "This book does not exist."}
        )