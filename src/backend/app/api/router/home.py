from fastapi import APIRouter

from backend.app.logging import get_logger

router = APIRouter(
    prefix="/home",
    tags=["home"],
)
logger = get_logger()

@router.get("/")
def home():
    logger.info("home accessed")
    logger.warning("home accessed")
    logger.error("home accessed")
    logger.critical("home accessed")
    return {"message": "Welcome to Next Gen Backend API"}