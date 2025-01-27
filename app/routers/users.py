from app.security import create_access_token
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from app.schemas import UserData, User, ReviewUser
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
async def get_user(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "role_id": current_user.role_id}


@router.post('/review_profile')
async def review(user: UserData, data_review: ReviewUser, current_user: UserData = Depends(get_current_user)):
    pass_user = await get_current_by_username(user.username)
    if user.username != current_user.username or not verify_password(user.password, pass_user.hashed_password):
        HTTPException(status_code=400, detail='Чёт не то')
    return await AsyncCRUD.review_user(user.username, user.password, data_review.username, data_review.password)




