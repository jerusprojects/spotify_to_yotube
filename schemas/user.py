from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    user_id: int = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    hashed_password: str = Field(..., min_length=8, max_length=64)


class User(UserBase):
    name: str = Field(..., min_length=1, max_length=20)
    yt_account: int = Field(...)


class UserRegister(User):
    hashed_password: str = Field(..., min_length=8, max_length=64)
