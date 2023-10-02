from widget.movie import MovieWidgets
from service.movies_api import MoviesApi
import streamlit as st
from cache.session_state import init_session_state

st.set_page_config(layout="wide")

st.title("Movie Recomendator🎬")

st.image(
    "https://static.amazon.jobs/teams/53/images/IMDb_Header_Page.jpg?1501027252",
    use_column_width="always",
)

tab1, tab2 = st.tabs(["Tinder Like Recomendation 🔥","Search Recomendation 🔎"])
init_session_state()

with tab1:
    _, c1, _ = st.columns((1, 0.8, 1))
    _, _, c2, c3, _, _ = st.columns(6)

    if st.session_state.recomendations is None:
        st.session_state.recomendations = MoviesApi.get_recomendation(st.session_state.current_movie, st.session_state.blacklist)
    
    with c1:
        MovieWidgets.display_movie(st.session_state.current_movie)

    with c3:
        if st.button("👍", use_container_width=True):
            st.session_state.blacklist.append(st.session_state.current_movie)
            st.session_state.current_movie = st.session_state.recomendations[0]
            st.session_state.recomendations = None
            st.experimental_rerun()
    with c2:
        if st.button("👎", use_container_width=True):
            st.session_state.blacklist.append(st.session_state.current_movie)
            st.session_state.current_movie = st.session_state.recomendations[-1]
            st.session_state.recomendations = None
            st.experimental_rerun()


with tab2:
    _, c1, _,= st.columns(3)
    with c1:
        my_expander = st.expander("Selecione um filme 🎬", expanded=True)
        if st.session_state.movies[0] != '': st.session_state.movies.insert(0,'')
        selected_movie_name = my_expander.selectbox("", st.session_state.movies)

    if my_expander.button("Recomendar Similares"):
        st.write("#")
        if selected_movie_name != '':
            recomendations = MoviesApi.get_recomendation(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            cols = [col1, col2, col3, col4, col5]
            for i in range(0, 5):
                with cols[i]:
                    MovieWidgets.display_movie(recomendations[i])
