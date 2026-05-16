"""Form for creating new animals in the evolutionary tree app."""

import streamlit as st
from models import traits, animal


def create_animal_form():
    """
    Creates a form for users to input animal data.
    """
    st.title("Create a New Animal")

    name: str = st.text_input("Animal Name")

    trophic_level: traits.TrophicLevel = st.selectbox(
        "Trophic Level",
        list(traits.TrophicLevel),
        format_func=lambda level: level.value,
    )

    habitat = st.selectbox(
        "Habitat", list(traits.Habitat), format_func=lambda habitat: habitat.value
    )

    covering = st.selectbox(
        "Covering", list(traits.Covering), format_func=lambda covering: covering.value
    )

    locomotion = st.selectbox(
        "Locomotion",
        list(traits.Locomotion),
        format_func=lambda locomotion: locomotion.value,
    )

    num_limbs = st.number_input("Number of Limbs", min_value=0, step=1)

    if st.button("Create Animal"):
        new_animal = animal.Animal(
            name=name,
            tropic_level=trophic_level,
            habitat=habitat,
            covering=covering,
            locomotion=locomotion,
            num_limbs=num_limbs,
        )
        st.success(f"Created animal: {new_animal}")
