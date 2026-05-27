"""Entry point for the evolutionary tree app."""

import streamlit as st
from components.form import create_animal_form
from components.database import fetch_animals
from components.util import initialize_session

initialize_session()

st.title("Evolutionary Tree App")
st.write(
    "Welcome to the Evolutionary Tree App! Use the form below to create new animals."
)
st.button(
    "Create New Animal",
    type="primary",
    on_click=lambda: st.session_state.update({"popup_open": True}),
)
st.button(
    "Fetch New Animals", on_click=lambda: fetch_animals(st.session_state.database)
)

if st.session_state.popup_open:
    fetch_animals(st.session_state.database)
    create_animal_form()

st.write("Current Animals in the Evolutionary Tree:")
for animal in st.session_state.animals:
    animal.write_animal_name_clickable()
