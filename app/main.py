from fastapi import FastAPI
from routers.users import router as user_router
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/register")


@app.get('/')
def home():
    return {"message": "Welcome!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)



