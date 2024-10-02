from pydantic import BaseModel, condecimal, Field
from uuid import UUID
from datetime import datetime
from typing import List, Optional

class VehicleBase(BaseModel):
    make: str = Field(..., min_length=1, max_length=100)
    model: str = Field(..., min_length=1, max_length=100)
    year: int
    license_plate: str = Field(..., min_length=5, max_length=15)
    seat_count: int = Field(...)

class Vehicle(VehicleBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

class TripBase(BaseModel):
    origin: str = Field(..., min_length=1, max_length=100)
    destination: str = Field(..., min_length=1, max_length=100)
    departure_time: datetime
    price: condecimal(max_digits=10, decimal_places=2, ge=0)
    available_seats: condecimal(max_digits=2, decimal_places=0, ge=1, le=10)

class Trip(TripBase):
    id: UUID
    driver_id: UUID
    vehicle_id: UUID
    created_at: datetime
    updated_at: datetime

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str

class User(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    vehicles: List[Vehicle] = Field(default_factory=list)
    trips_driven: List[Trip] = Field(default_factory=list)
