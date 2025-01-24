from sqlalchemy import insert, select, update

from dependencies import async_engine
from schemas import UserCreate
from dependencies import async_session
from models import UserModel

class AsyncCRUD:

    @staticmethod
    async def create_user(username: str, hashed_password: str):
        async with async_session() as session:
            async with session.begin():
                query = (
                    insert(UserModel).values({"username": username, "hashed_password": hashed_password})
                )
                await session.execute(query)
                await session.commit()








































