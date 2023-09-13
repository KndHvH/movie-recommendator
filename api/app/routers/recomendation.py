from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.service.recomendation import RecomendationService
from app.models.models import MovieRecommendation


router = APIRouter()


@router.post('/recommend')
def recommend():
    def recomend(data: MovieRecommendation):
        movie_title = data.movie
        blacklist = data.blacklist

        recomendation = RecomendationService()


        return RedirectResponse(url="/docs")