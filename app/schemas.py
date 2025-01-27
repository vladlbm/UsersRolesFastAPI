from pydantic import BaseModel

class UserData(BaseModel):
    username: str
    password: str


class CreateUser(BaseModel):
    username: str
    password: str
    role_id: int


class ReviewUserForModer(BaseModel):
    username: str
    password: str
    role_id: int


class ReviewUser(BaseModel):
    username: str
    password: str


class User(BaseModel):
    username: str
    password: str
    role_id: int