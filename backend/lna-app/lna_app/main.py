from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import news
import os

app = FastAPI(title="LNA API")

@app.get("/")
async def root():
    return {"message": "Hi"}

# Register API routes
app.include_router(news.router, prefix="/news")

# Allow frontend requests from the Azure frontend deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lnaapp-fjgqecfra5hsaff0.uaenorth-01.azurewebsites.net"],  # Your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Ensure Azure assigns the correct port
    uvicorn.run(app, host="0.0.0.0", port=port, reload=True)
