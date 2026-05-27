"""Util functions for streamlit app"""

import streamlit as st
from components.database import get_client, fetch_animals


def initialize_session():
    """
    Initializes database connections and fetches initial data.
    """
    if "app_initialized" not in st.session_state:

        with st.spinner("Excavating fossil records... (Fetching from database)"):

            st.session_state.database = get_client()

            st.session_state.setdefault("animals", [])
            st.session_state.setdefault("popup_open", False)

            fetch_animals(st.session_state.database)

            st.session_state.app_initialized = True
