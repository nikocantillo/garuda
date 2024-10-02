from typing import Union
from app.routers import user, vehicle
from fastapi import FastAPI

app = FastAPI()


app.include_router(user.router)
app.include_router(vehicle.router)