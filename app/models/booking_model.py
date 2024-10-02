import uuid
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.database import Base
from datetime import datetime

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    trip_id = Column(UUID(as_uuid=True), ForeignKey('trips.id'), nullable=False)
    passenger_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    seats = Column(Integer, nullable=False, default=1)
    status = Column(String, default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    trip = relationship("Trip", back_populates="bookings")
    passenger = relationship("User", back_populates="bookings")
