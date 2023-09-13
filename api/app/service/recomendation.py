from helper.file import FileHelper
from helper.text import TextHelper
from service.model import ModelService

class RecomendationService():
    def __init__(self,filename:str = 'all_movies.csv') -> None:
        self.df = FileHelper.get_dataframe(filename)

    def get_recomendation(self,movie_title):
        movie_index = self.df[self.df['title_pt'] == movie_title].index[0]
        tfidf_matrix = TextHelper.get_vectorized_matrix(self.df,'sinopse')
        movie_vector = tfidf_matrix[movie_index]
        distances, indices = ModelService.get_model_with_tfidf(tfidf_matrix).kneighbors(movie_vector)
        recommended_movies = [self.df.iloc[index]['title_pt'] for index in indices[0][1:]]
        return recommended_movies