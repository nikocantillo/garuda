# from pydantic import BaseModel
# from uuid import UUID


# class BookingBase(BaseModel):
#     status: str

# class BookingCreate(BookingBase):
#     pass

# class Booking(BookingBase):
#     id: UUID
#     trip_id: UUID
#     passenger_id: UUID

#     class Config:
#         from_attributes = True


from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime
from .shared_schemas import Trip, User

class BookingBase(BaseModel):
    seats: str = Field(..., pattern=r'^\d+$')
    status: Optional[str] = Field('pending', max_length=20)

class BookingCreate(BookingBase):
    trip_id: UUID

class BookingUpdate(BaseModel):
    seats: str = Field(..., pattern=r'^\d+$')
    status: Optional[str] = Field(None, max_length=20)

class Booking(BookingBase):
    id: UUID
    trip_id: UUID
    passenger_id: UUID
    created_at: datetime
    updated_at: datetime
    trip: Optional[Trip] = None
    passenger: Optional[User] = None

    class Config:
        from_attributes = True




