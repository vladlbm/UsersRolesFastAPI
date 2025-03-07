from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import select
from fastapi import HTTPException, Depends
from app.security import verify_access_token
from models import UserModel
from config import settings
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from crud import AsyncCRUD
import asyncio
import time

o2auth_scheme = OAuth2PasswordBearer(tokenUrl="login")


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True
)

async_session = async_sessionmaker(async_engine)


async def get_current_by_username(username: str):
    async with async_session() as session:
        query = (select(UserModel).where(UserModel.username == username))
        result = await session.execute(query)
        data_user = result.scalar_one_or_none()
        return data_user


async def get_current_user(token: str):
    payload = verify_access_token(token)
    username = payload.get('sub')
    if username is None:
        raise HTTPException(status_code=401, detail='Инвалид ваш токен короче')
    user = await get_current_by_username(username)
    if user is None:
        raise HTTPException(status_code=401, detail="Тоже инвалид, не знаю")
    return user


def require_role(role: str):
    async def dependency(current_user: UserModel = Depends(get_current_user)):
        role_id = await AsyncCRUD.get_role_id(role)
        if role_id != current_user.role_id:
            raise HTTPException(status_code=403, detail="Нету прав")
        return current_user
    return dependency




