from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import news

app = FastAPI(title="LNA API")

@app.get("/")
async def root():
    return {"message": "Hi"}

# Remove or comment out the lifespan setup that includes database initialization
# This makes the application initialization simpler and independent of the database

app.include_router(news.router, prefix="/news")

# Adjust the CORS middleware to match your actual frontend deployment URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lnaapp-fjgqecfra5hsaff0.uaenorth-01.azurewebsites.net"], # Change to your deployed frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
