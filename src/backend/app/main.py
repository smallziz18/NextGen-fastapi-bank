from fastapi import FastAPI
app = FastAPI(
    title="NextGen Backend API",
    description="Next Gen Backend API",
    version="1.0",
)

@app.get("/")
def home():
    return {"message": "Welcome to Next Gen Backend API"}