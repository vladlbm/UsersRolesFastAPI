from app.security import create_access_token
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from app.schemas import UserData
from app.crud import AsyncCRUD
from app.security import hash_password, verify_password, verify_access_token
from app.dependencies import get_current_by_username, get_current_user

router = APIRouter()


@router.post('/register')
async def register(user: UserData):
    hashed_password = hash_password(user.password)
    await AsyncCRUD.create_user(user.username, hashed_password)


@router.post('/login')
async def login(user: UserData):
    data_user = await get_current_by_username(user.username)
    if not data_user or not verify_password(user.password, data_user.hashed_password):
        raise HTTPException(status_code=401, detail='Нету такого')
    token = create_access_token({"sub": data_user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get('/my_info')
async def get_user(current_user: UserData = Depends(get_current_user)):
    return {"username": current_user.username}





