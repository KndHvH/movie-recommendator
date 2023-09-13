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
    def post_files(movie:str):
        data = {"title": movie}
        response = requests.post(f'{os.getenv("URL")}/info')
        data = response.json()
        return data
    