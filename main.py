from fastapi import FastAPI
from routers.books import router as book_router
from routers.authors import router as author_router
from routers.users import router as user_router
from db.db import init_db


app = FastAPI()

app.include_router(book_router)
app.include_router(author_router)
app.include_router(user_router)

@app.on_event("startup")
async def on_startup():
    await init_db()