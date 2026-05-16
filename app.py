"""Entry point for the evolutionary tree app."""

import streamlit as st
from pages.form import create_animal_form


def main():
    """Creates form for now"""
    st.title("Evolutionary Tree App")
    st.write(
        "Welcome to the Evolutionary Tree App! Use the form below to create new animals."
    )
    create_animal_form()


if __name__ == "__main__":
    main()
