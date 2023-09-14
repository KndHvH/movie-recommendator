from widget.movie import MovieWidgets
import streamlit as st

st.image('https://static.amazon.jobs/teams/53/images/IMDb_Header_Page.jpg?1501027252')
st.title('Movie Recomendator🎬')

MovieWidgets.display_main_movie()