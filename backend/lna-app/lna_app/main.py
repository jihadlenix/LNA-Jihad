from fastapi import FastAPI
from contextlib import asynccontextmanager
from lna_app.api import news
from lna_app.db.session import init_database


app = FastAPI(title="Simple LNA API")

@app.get("/")
async def root():
    return {"message": "Hi"}

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for FastAPI application.

    Handles startup and shutdown events:
    - Startup: Initialize database and Beanie ODM
    - Shutdown: Any cleanup if needed
    """
    # Startup
    await init_database()
    yield
    # Shutdown (if we need cleanup later)


app = FastAPI(
    title="LNA API",
    lifespan=lifespan,
)

app.include_router(news.router, prefix="/news")