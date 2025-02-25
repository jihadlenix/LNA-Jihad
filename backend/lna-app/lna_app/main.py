from fastapi import FastAPI

app = FastAPI(title="Simple LNA API")

@app.get("/")
async def root():
    return {"message": "Hi"}
