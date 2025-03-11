from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI(title="Simple LNA API")

origins = [
    "https://localhost:5173",  # If using HTTPS locally
    "http://localhost:5173",  # If still using HTTP locally
    "https://lnafrontend.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .api.news import router as news_router

app.include_router(news_router, prefix="/news")

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
