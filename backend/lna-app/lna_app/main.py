from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .api.news import router as news_router  # Ensure this path is correct

app = FastAPI(title="Simple LNA API")

# Correcting CORS settings to be included in the same FastAPI app instance
origins = [
    "http://localhost:5173",  # Local frontend address
    "https://lnafrontend.vercel.app", # Deployed frontend address]
     "http://127.0.0.1:5173" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news_router, prefix="/news")  # Include your router with the prefix

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
