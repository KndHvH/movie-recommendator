import random

from app.helper.file import FileHelper
from app.helper.text import TextHelper
from app.service.model import ModelService


class RecomendationService:
    def __init__(self, filename: str = "all_movies.csv") -> None:
        self.df = FileHelper.get_dataframe(filename)
        self.tfidf_matrix = TextHelper.get_vectorized_matrix(self.df, "sinopse")

    def _get_movie_index(self, movie_title: str) -> int:
        return self.df[self.df["title_pt"] == movie_title].index[0]

    def _get_movie_vector(self, movie_index: int):
        return self.tfidf_matrix[movie_index]

    def _get_kneighbors(self, movie_vector):
        return ModelService.get_model_with_tfidf(self.tfidf_matrix).kneighbors(
            movie_vector
        )

    def get_recommendation(self, movie_title: str, blacklist: list = None) -> list:
        if blacklist is None:
            blacklist = []
        blacklist.append(movie_title)

        movie_index = self._get_movie_index(movie_title)
        movie_vector = self._get_movie_vector(movie_index)
        distances, indices = self._get_kneighbors(movie_vector)

        paired = list(zip(indices[0].tolist(), distances[0]))
        sorted_paired = sorted(paired, key=lambda x: x[1])
        recommended_movies = [
            self.df.iloc[pair[0]]["title_pt"]
            for pair in sorted_paired
            if self.df.iloc[pair[0]]["title_pt"] not in blacklist
        ]

        return recommended_movies

    def get_random_movie(self):
        return random.choice(self.df["title_pt"].tolist())
