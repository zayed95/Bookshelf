from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exc, select
from models.models import User
from schemas.users import UserCreate, UserRead
from db.db import get_session
from db.password import get_password_hash
from typing import Optional

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, session: AsyncSession = Depends(get_session)):

    hashed_password = get_password_hash(user_in.password)
    db_user = User(email=user_in.email, hashed_password=hashed_password)
    session.add(db_user)

    try:
        await session.commit()
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this email already exists!"
        )
    
    await session.refresh(db_user)
    return db_user