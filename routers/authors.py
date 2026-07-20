from sqlmodel import select
from fastapi import APIRouter, status, Depends, HTTPException
from schemas.books import Author, AuthorRead, AuthorCreate
from db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
    )

@router.post("/", response_model=AuthorRead, status_code=status.HTTP_201_CREATED)
async def create_author(author_create: AuthorCreate,
                    session: AsyncSession = Depends(get_session)) -> Author:

    db_author = Author.model_validate(author_create)
    session.add(db_author)
    await session.commit()
    await session.refresh(db_author)
    return db_author

@router.get("/", response_model=list[AuthorRead])
async def get_authors(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Author))
    authors = result.scalars().all()

    if not authors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Author not found"
        )
    
    return authors