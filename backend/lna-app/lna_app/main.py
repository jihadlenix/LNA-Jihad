from fastapi import FastAPI

app = FastAPI(title="LNA App", description="this is the LNA App")

@app.get("/")
async def root():
    return {
        "message": "Nothing to see here! Click here to join the party -> http://localhost:8000/hello-world 🎉",
        "docs": "Check out the API docs at http://localhost:8000/docs"
    }

@app.get("/hello-world")
async def hello_world():
    return {"message": "Hello World"}
