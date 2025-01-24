from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, MappedColumn
from dependencies import Base

class UserModel(Base):
    __table__= 'users'

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    username: Mapped[str]
    hashed_password: Mapped[str]
    role_id: Mapped[int] = MappedColumn(ForeignKey("user_role.c.id"), default=3, on_delete='CASCADE')


class UserRoleModel(Base):
    __table__ = 'user_role'

    id: Mapped[int] = MappedColumn(primary_key=True)
    role: Mapped[str]
