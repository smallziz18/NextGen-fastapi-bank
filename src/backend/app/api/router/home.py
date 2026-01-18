from fastapi import APIRouter

router = APIRouter(
    prefix="/home",
    tags=["home"],
)

@router.get("/")
def home():
    return {"message": "Welcome to Next Gen Backend API"}