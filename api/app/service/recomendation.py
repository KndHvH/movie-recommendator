from helper.file import FileHelper

class RecomendationService():
    def __init__(self,filename:str) -> None:
        self.df = FileHelper.get_dataframe(filename)

    def get_recomendation(self,movie_title):
        movie_index = self.df[self.df['title_en'] == movie_title].index[0]
