from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Fast API Backend is running!"}
