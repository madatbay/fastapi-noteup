from fastapi import FastAPI

from app.routers import user

app = FastAPI(
    title="noteUP",
    version="0.1.0"
)

app.include_router(user.router)
