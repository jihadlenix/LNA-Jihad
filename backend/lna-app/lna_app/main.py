from fastapi import FastAPI

from lna_app.api import news

app: FastAPI = FastAPI()

app.include_router(news.router, prefix="/news")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
