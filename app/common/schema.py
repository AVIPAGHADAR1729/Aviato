from typing import Optional

from pydantic.v1 import BaseModel, Field, EmailStr, validator


class UserBase(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)


class UserCreateEmail(UserBase):
    email: Optional[EmailStr] = None
    password: str = Field(..., min_length=8)
    company_name: Optional[str] = None

    @validator("company_name", always=True)
    def set_default_company(cls, v):
        return v or ""


class UserCreateMobileDOB(UserBase):
    mobile: Optional[str] = Field(..., pattern="^\+?[1-9]\d{1,14}$")
    date_of_birth: Optional[str] = None


class UserCreateMobileHashtag(UserBase):
    mobile: Optional[str] = Field(..., pattern="^\+?[1-9]\d{1,14}$")
    hashtag: Optional[str] = None


class UserUpdate(UserCreateEmail, UserCreateMobileDOB, UserCreateMobileHashtag):
    pass


class UserGet(BaseModel):
    user_ids: Optional[list[str]] = None


class UserDelete(BaseModel):
    user_id: str
