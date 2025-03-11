from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .api.news import router as news_router  # Adjust this import path based on your project structure

app = FastAPI(title="Simple LNA API")

app.include_router(news_router, prefix="/news")  # Add a prefix if desired, or leave it empty

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lnafrontend.vercel.app"],  # This is for development only; specify your frontend's host for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hi"}
