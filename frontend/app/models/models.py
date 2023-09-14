from pydantic import BaseModel

class MovieRecommendation(BaseModel):
    movie: str
    blacklist: list = []
