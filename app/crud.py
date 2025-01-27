from fastapi import HTTPException
from sqlalchemy import insert, select, update, delete

from app.schemas import ReviewUser
from schemas import UserData
from models import UserModel, UserRoleModel
import dependencies
from security import hash_password

class AsyncCRUD:

    @staticmethod
    async def create_user(username: str, hashed_password: str):
        async with dependencies.async_session() as session:
            async with session.begin():
                query = (
                    insert(UserModel).values({"username": username, "hashed_password": hashed_password})
                )
                await session.execute(query)
                await session.commit()


    @staticmethod
    async def delete_user(user_id: int):
        async with dependencies.async_session() as session:
            async with session.begin():
                query = (
                    select(UserModel).filter(UserModel.id == user_id)
                )
                result = await session.execute(query)
                user = result.scalar_one_or_none()
                if user is None:
                    raise HTTPException(status_code=404, detail='С таким айди нету пользака')

                await session.delete(user)
            return {"message": "Пользак успешно удалён"}


    @staticmethod
    async def review_user_for_moder(user_id: int, username: str, password: str, role_id: int):
        async with dependencies.async_session() as session:
            async with session.begin():
                hashed_password = hash_password(password)
                query = (
                    update(UserModel).values({"username": username, "hashed_password": hashed_password, "role_id": role_id}).filter(UserModel.id == user_id)
                )
                await session.execute(query)
                await session.commit()


    @staticmethod
    async def review_user(username, password, review_username, review_password):
        async with dependencies.async_session() as session:
            async with session.begin():
                hashed_password = hash_password(review_password)
                query = (
                    update(UserModel).values({"username": review_username, "hashed_password": hashed_password})
                    .filter(UserModel.username == username, UserModel.hashed_password == hash_password(password))
                )
                await session.execute(query)
                await session.commit()


    @staticmethod
    async def create_user_for_admin(username: str, password: str, role_id: int):
        async with dependencies.async_session() as session:
            async with session.begin():
                hashed_password = hash_password(password)
                query = (
                    insert(UserModel).values({"username": username, "hashed_password": hashed_password, "role_id": role_id})
                )
                await session.execute(query)
                await session.commit()


    @staticmethod
    async def get_role_id(role: str):
        async with dependencies.async_session() as session:
            query = (
                select(UserRoleModel.id).filter(UserRoleModel.role == role)
            )
            result = await session.execute(query)
            role_id = result.scalar_one_or_none()
            return role_id









































