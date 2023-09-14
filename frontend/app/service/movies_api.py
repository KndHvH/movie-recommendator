import requests
import json
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

class MoviesApi:
    @staticmethod
    def get_recomendation(movie:str, blacklist:list=[]):
        data = {
                "movie": movie,
                "blacklist": blacklist
            }
        response = requests.post(f'{os.getenv("API_URL")}/recommend',json=data)
        data = response.json()
        return data
    
    @staticmethod
    def get_movie_info(movie:str):
        data = {"title": movie}
        response = requests.post(f'{os.getenv("API_URL")}/info', json=data)
        data = response.json()
        return data
    
    @staticmethod
    def get_random_movie():
        response = requests.get(f'{os.getenv("API_URL")}/movie')
        data = response.json()
        return data
    