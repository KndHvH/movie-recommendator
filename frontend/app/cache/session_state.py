import streamlit as st

def init_session_state():
    if 'current_movie' not in st.session_state:
        st.session_state.current_movie = None
    if 'blacklist' not in st.session_state:
        st.session_state.blacklist = []
    if 'recomendations' not in st.session_state:
        st.session_state.recomendations = None