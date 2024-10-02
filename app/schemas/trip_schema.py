from typing import Optional, List
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, condecimal, Field
from .shared_schemas import User, Vehicle

class TripBase(BaseModel):
    origin: str = Field(..., min_length=1, max_length=100)
    destination: str = Field(..., min_length=1, max_length=100)
    departure_time: datetime
    price: condecimal(max_digits=10, decimal_places=2, ge=0)
    available_seats: condecimal(max_digits=2, decimal_places=0, ge=1, le=10)

class TripCreate(TripBase):
    vehicle_id: UUID

class TripUpdate(BaseModel):
    origin: Optional[str] = Field(None, min_length=1, max_length=100)
    destination: Optional[str] = Field(None, min_length=1, max_length=100)
    departure_time: Optional[datetime] = None
    price: Optional[condecimal(max_digits=10, decimal_places=2, ge=0)] = None
    available_seats: Optional[condecimal(max_digits=2, decimal_places=0, ge=1, le=10)] = None
    vehicle_id: Optional[UUID] = None

class Trip(TripBase):
    id: UUID
    driver_id: UUID
    vehicle_id: UUID
    created_at: datetime
    updated_at: datetime
    driver: Optional[User] = None
    vehicle: Optional[Vehicle] = None
    bookings: List['Booking'] = Field(default_factory=list)

    class Config:
        from_attributes = True
