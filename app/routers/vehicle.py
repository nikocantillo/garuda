from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.database import get_db
from app.models.user_model import User as user_model
from app.models.vehicle_model import Vehicle as vehicle_model
from app.schemas.vehicle_schema import VehicleCreate, Vehicle
from typing import Any

router = APIRouter()

@router.post("/vehicles/", response_model=Vehicle, tags=['Vehicles'])
async def create_vehicle(vehicle: VehicleCreate, db: AsyncSession = Depends(get_db)) -> Any:
    # Verificar si el usuario existe de forma asíncrona
    result = await db.execute(select(user_model).filter(user_model.id == vehicle.user_id))
    db_user = result.scalar_one_or_none()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Crear el nuevo vehículo
    db_vehicle = vehicle_model(
        make=vehicle.make,
        model=vehicle.model,
        color=vehicle.color,
        license_plate=vehicle.license_plate,
        seat_count=vehicle.seat_count,
        user_id=vehicle.user_id,
    )
    
    # Agregar el vehículo a la base de datos de manera asíncrona
    db.add(db_vehicle)
    
    # Hacer commit asíncrono
    await db.commit()

    # Refrescar el estado del vehículo desde la base de datos
    await db.refresh(db_vehicle)

    return db_vehicle
