from service.movies_api import MoviesApi
import streamlit as st

def init_session_state():
    if 'current_movie' not in st.session_state:
        st.session_state.current_movie = MoviesApi.get_random_movie()
    if 'blacklist' not in st.session_state:
        st.session_state.blacklist = []
    if 'recomendations' not in st.session_state:
        st.session_state.recomendations = None
    if 'movies' not in st.session_state:
        st.session_state.movies = MoviesApi.get_all_movies()