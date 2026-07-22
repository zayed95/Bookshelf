from sqlmodel import select
from fastapi import APIRouter, status, Depends, HTTPException
from models.models import Author
from schemas.authors import AuthorRead, AuthorCreate
from db.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
    )

@router.post("/", response_model=AuthorRead, status_code=status.HTTP_201_CREATED)
async def create_author(author_create: AuthorCreate,
                    session: AsyncSession = Depends(get_session)) -> Author:

    db_author = Author(**author_create.model_dump())
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