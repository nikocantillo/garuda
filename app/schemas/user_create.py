from typing import Optional, List
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from .shared_schemas import Vehicle, Trip

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    first_name: Optional[str] = Field(None, max_length=100)
    last_name: Optional[str] = Field(None, max_length=100)
    birth_date: Optional[datetime] = None
    is_driver: bool = False
    biography: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8)
    first_name: Optional[str] = Field(None, max_length=100)
    last_name: Optional[str] = Field(None, max_length=100)
    birth_date: Optional[datetime] = None
    is_driver: Optional[bool] = None
    biography: Optional[str] = None

class User(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    vehicles: List[Vehicle] = Field(default_factory=list)
    trips_driven: List[Trip] = Field(default_factory=list)

    class Config:
        from_attributes = True

class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    vehicles: List[Vehicle] = Field(default_factory=list)
    trips_driven: List[Trip] = Field(default_factory=list)

    class Config:
        from_attributes = True
