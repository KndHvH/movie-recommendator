import requests
import json
import os

class MoviesApi:
    @staticmethod
    def get_recomendation(movie:str, blacklist:list=[]):
        data = {
                "movie": movie,
                "blacklist": blacklist
            }
        response = requests.post(f'{os.getenv("URL")}/recommend',data=data)
        data = response.json()
        return data
    
    @staticmethod
    def get_movie_info(movie:str):
        data = {"title": movie}
        response = requests.post(f'{os.getenv("URL")}/info')
        data = response.json()
        return data
    
    @staticmethod
    def get_random_movie():
        response = requests.get(f'{os.getenv("URL")}/movie')
        data = response.json()
        return data
    