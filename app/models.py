from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import Mapped, MappedColumn, DeclarativeBase


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__= 'users'

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    username: Mapped[str]
    hashed_password: Mapped[str]
    role_id: Mapped[int] = MappedColumn(ForeignKey("user_role.id"), default=3)

    __table_args__ = (
        ForeignKeyConstraint(["role_id"], ["user_role.id"], ondelete="CASCADE"),
    )


class UserRoleModel(Base):
    __tablename__ = 'user_role'

    id: Mapped[int] = MappedColumn(primary_key=True)
    role: Mapped[str]

