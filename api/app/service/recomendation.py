from app.helper.file import FileHelper
from app.helper.text import TextHelper
from app.service.model import ModelService


class RecomendationService:
    def __init__(self, filename: str = "all_movies.csv") -> None:
        self.df = FileHelper.get_dataframe(filename)

    def get_recomendation(self, movie_title: str, blacklist: list = [])
        blacklist.append(movie_title)
        movie_index = self.df[self.df["title_pt"] == movie_title].index[0]
        #todo PAU
        tfidf_matrix = TextHelper.get_vectorized_matrix(self.df, "sinopse")
        movie_vector = tfidf_matrix[movie_index]
        distances, indices = ModelService.get_model_with_tfidf(tfidf_matrix).kneighbors(movie_vector)
        paired = list(zip(indices[0].tolist(), distances[0]))
        sorted_paired = sorted(paired, key=lambda x: x[1])
        recommended_movies = [
            self.df.iloc[pair[0]]["title_pt"]
            for pair in sorted_paired
            if self.df.iloc[pair[0]]["title_pt"] not in blacklist
        ][:10]

        return recommended_movies
