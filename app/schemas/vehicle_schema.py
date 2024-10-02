from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime
from .shared_schemas import Trip

class VehicleBase(BaseModel):
    make: str = Field(..., min_length=1, max_length=100)
    model: str = Field(..., min_length=1, max_length=100)
    year: int
    color: Optional[str] = Field(None, max_length=50)
    license_plate: str = Field(..., min_length=5, max_length=15)
    seat_count: int = Field(...)

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(VehicleBase):
    make: Optional[str] = Field(None, min_length=1, max_length=100)
    model: Optional[str] = Field(None, min_length=1, max_length=100)

class Vehicle(VehicleBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime
    trips: List[Trip] = Field(default_factory=list)

    class Config:
        from_attributes = True







