from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_superuser: Optional[bool] = None


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


# Properties shared by schemas stored in DB
class UserInDBBase(UserBase):
    class Config:
        orm_mode = True


# Properties properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
