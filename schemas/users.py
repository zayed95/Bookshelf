from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

class User(UserBase):
    id: int
    hashed_password: str

    class Config:
            from_attributes = True