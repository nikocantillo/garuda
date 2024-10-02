# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from typing import Any
# from passlib.context import CryptContext
# from app.models import User as user_model
# from app.schemas import UserCreate, User
# from app.models.database import get_db

# router = APIRouter()

# pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# def get_password_hash(password):
#     return pwd_context.hash(password)

# @router.post("/users/", response_model=User, tags=['Users'])
# async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)) -> Any:
#     result = await db.execute(
#         select(user_model).filter(user_model.email == user.email)
#     )
#     db_user = result.scalar_one_or_none()
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     hashed_password = get_password_hash(user.password)
#     db_user = user_model(
#         username=user.username,
#         email=user.email,
#         hashed_password=hashed_password,
#         first_name=user.first_name,
#         last_name=user.last_name,
#         is_driver=user.is_driver,
#         birth_date=user.birth_date,
#         biography=user.biography,
#     )
#     db.add(db_user)
#     await db.commit()
#     await db.refresh(db_user)
#     return db_user


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Any
from passlib.context import CryptContext
from app.models import User as user_model
from app.schemas import UserCreate, User, UserResponse
from app.models.database import get_db

router = APIRouter()

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

@router.post("/users/", response_model=UserResponse, tags=['Users'])
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)) -> Any:
    result = await db.execute(select(user_model).filter(user_model.email == user.email))
    db_user = result.scalar_one_or_none()
    
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    
    db_user = user_model(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
        is_driver=user.is_driver,
        birth_date=user.birth_date,
        biography=user.biography,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)  
    return db_user

#