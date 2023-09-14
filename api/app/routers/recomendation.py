from app.helper.file import FileHelper
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.service.recomendation import RecomendationService
from app.models.models import MovieRecommendation, MovieInfoRequest


router = APIRouter()


@router.post("/recommend")
def recomend(data: MovieRecommendation):
    movie_title = data.movie
    blacklist = data.blacklist

    recomendation_service = RecomendationService()
    recomendation = recomendation_service.get_recommendation(
        movie_title=movie_title, blacklist=blacklist
    )
    return recomendation


@router.post("/info")
def info(request: MovieInfoRequest):
    df = FileHelper.get_dataframe("all_movies.csv")
    movie_info = df[df["title_pt"] == request.title]
    return movie_info.iloc[0].to_dict()


@router.get("/movie")
def get_movie():
    recomendation_service = RecomendationService()
    return recomendation_service.get_random_movie()
