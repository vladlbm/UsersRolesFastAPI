from fastapi import FastAPI
from routers.users import router as user_router
from routers.roles import routers_role as role_router
import uvicorn

app = FastAPI()


app.include_router(user_router)
app.include_router(role_router)


@app.get('/')
def home():
    return {"message": "Welcome!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)



