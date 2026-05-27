"""Util functions for streamlit app"""

from pathlib import Path

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

            fetch_animals(st.session_state.database)

            st.session_state.app_initialized = True


def fetch_button_callback():
    """Lambda for the fetch button, fetches and writes whether it was successful or not"""
    fetched = fetch_animals(st.session_state.database)

    if fetched:
        st.caption("Fetched New Animals (Success)")

    else:
        st.caption("No new animals to fetch. You're up to date!")


def switch_to_page(page_name: str):
    """
    Switches to page

    Input: Name of python file to Switch to
    """
    st.switch_page(Path("Pages") / page_name)
