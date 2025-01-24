from fastapi import FastAPI, APIRouter
from app.schemas import UserCreate
from app.crud import AsyncCRUD
from app.security import hash_password, verify_password

router = APIRouter()


@router.post('/register')
async def register(user: UserCreate):
    hashed_password = hash_password(user.password)
    await AsyncCRUD.create_user(user.username, hashed_password)