from fastapi import APIRouter, Depends, HTTPException
from app.schemas import CreateUser, BaseModel, ReviewUserForModer
from app.dependencies import require_role
from app.security import hash_password
from app.models import UserModel
from app.crud import AsyncCRUD
import time

routers_role = APIRouter()


@routers_role.post('/create_user')
async def create(user: CreateUser, role: UserModel = Depends(require_role("admin"))):
    await AsyncCRUD.create_user_for_admin(user.username, user.password, user.role_id)
    return {"message": 'Пользяк успешно создан'}


@routers_role.post('/delete_user')
async def delete(user_id: int, role: str = Depends(require_role("admin"))):
    return await AsyncCRUD.delete_user(user_id)


@routers_role.post('/review_user')
async def review_user(user_id: int, data: ReviewUserForModer, role: str = Depends(require_role("moderator"))):
    return await AsyncCRUD.review_user_for_moder(user_id, data.username, data.password, data.role_id)
