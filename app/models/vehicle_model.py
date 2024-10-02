import uuid
from sqlalchemy import Column, String, Integer, ForeignKey,DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.database import Base
from datetime import datetime

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    make = Column(String, nullable=False)          # Marca del vehículo
    model = Column(String, nullable=False)         # Modelo del vehículo
    year = Column(Integer, nullable=False)         # Año del vehículo
    color = Column(String, nullable=True)           # Color del vehículo
    license_plate = Column(String, unique=True, nullable=False)  # Matrícula única
    seat_count = Column(Integer, nullable=False)    # Número de asientos
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="vehicles")  # Relación con Usuario
    trips = relationship("Trip", back_populates="vehicle")   # Relación con Trips
