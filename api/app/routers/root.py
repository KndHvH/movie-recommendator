from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.models.models import MovieRecommendation


router = APIRouter()


@router.get("/")
def recomend():
    return RedirectResponse(url="/docs")