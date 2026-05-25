"""Form for creating new animals in the evolutionary tree app."""

import streamlit as st
from models import traits, animal
from components.database import add_animal


@st.dialog("Create a New Animal")
def create_animal_form():
    """Creates a form for users to input animal data safely inside a dialog."""

    with st.form("new_animal_submission_form", clear_on_submit=False):
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
            "Covering",
            list(traits.Covering),
            format_func=lambda covering: covering.value,
        )

        locomotion = st.selectbox(
            "Locomotion",
            list(traits.Locomotion),
            format_func=lambda locomotion: locomotion.value,
        )

        num_limbs = st.number_input("Number of Limbs", min_value=0, step=1)
        submitted = st.form_submit_button("Create Animal")

        if submitted:
            if not name.strip():
                st.error("Please enter a valid name for the animal.")
                return

            taken_names: list[str] = [a.name for a in st.session_state.animals]

            if name in taken_names:
                st.error(
                    "Animal name is already in use, please choose a different name"
                )
                return

            new_animal = animal.Animal(
                name=name,
                trophic_level=trophic_level,
                habitat=habitat,
                covering=covering,
                locomotion=locomotion,
                num_limbs=num_limbs,
                user_generated=True,
            )

            try:
                db_client = st.session_state.get("database")
                if db_client is None:
                    st.error("Database client not found in session state.")
                    return

                add_animal(new_animal, db_client)

                st.session_state.popup_open = False
                st.rerun()

            except Exception as e:
                st.error(f"Failed to submit to database: {e}")
