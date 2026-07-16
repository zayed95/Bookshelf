import contextlib
from fastapi import FastAPI
from routers.books import router
from db import init_db


app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def on_startup():
    await init_db()