"""Entry point for the evolutionary tree app."""

import streamlit as st
from pages.form import create_animal_form

st.session_state.setdefault("animals", [])
st.session_state.setdefault("popup_open", False)

st.title("Evolutionary Tree App")
st.write(
    "Welcome to the Evolutionary Tree App! Use the form below to create new animals."
)
st.button(
    "Create New Animal", on_click=lambda: st.session_state.update({"popup_open": True})
)

if st.session_state.popup_open:
    create_animal_form()

st.write("Current Animals in the Evolutionary Tree:")
for animal in st.session_state.animals:
    animal.write_animal_name_clickable()
