"""Entry point for the evolutionary tree app."""

import streamlit as st
from components.form import create_animal_form
from components.database import fetch_animals
from components.util import *

initialize_session()

st.title("Evolutionary Tree App")
st.write("""
    Welcome to the Evolutionary Tree App! 
    - Press the **Create New Animal** button to create your own animal!
    - Navigate to the sidebar to view the evolutionary tree or press the **View Tree** button
    - Press the **Fetch New Animals** button to fetch new animals that other users have added.
    """)
col1, col2 = st.columns(2)

with col1:
    st.button(
        "Create New Animal",
        type="primary",
        on_click=lambda: st.session_state.update({"popup_open": True}),
        width="stretch",
    )
    if st.button(
        "View Evolutionary Tree",
        type="secondary",
        width="stretch",
    ):
        switch_to_page("Evolutionary_Tree.py")


with col2:
    st.button(
        "Fetch New Animals", type="secondary", on_click=lambda: fetch_button_callback()
    )

if st.session_state.popup_open:
    fetch_animals(st.session_state.database)
    create_animal_form()

st.divider()

st.write("Current Animals in the Evolutionary Tree:")
for animal in st.session_state.animals:
    animal.write_animal_name_clickable()
