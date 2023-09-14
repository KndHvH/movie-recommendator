import streamlit as st

from service.movies_api import MoviesApi

class MovieWidgets:
    
    @staticmethod
    def display_movie(movie):
        movie_data = MoviesApi.get_movie_info(movie)
        with st.expander(movie_data['title_pt'],expanded=True):
            st.image(movie_data['image'],use_column_width=True)

            c4,c2,c3 = st.columns((0.8,0.8,1))

            with c4: st.markdown(f"##### {movie_data['year']}📆")
            with c2: st.markdown(f"##### {movie_data['rating']}⭐")
            with c3: st.markdown(f"##### {movie_data['genre']}🎭")

            st.write(movie_data['sinopse'])
