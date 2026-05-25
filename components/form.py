"""Form for creating new animals in the evolutionary tree app."""

import streamlit as st
from models import traits, animal
from components.database import add_animal


@st.dialog("Create a New Animal")
def create_animal_form():
    """Creates a form for users to input animal data safely inside a dialog."""

    with st.form("new_animal_submission_form", clear_on_submit=False):

        st.subheader("Basic Info")
        name: str = st.text_input("Animal Name")

        st.subheader("Morphology")
        symmetry = st.selectbox(
            "Symmetry", list(traits.Symmetry), format_func=lambda sym: sym.value
        )
        skeleton_type = st.selectbox(
            "Skeleton Type",
            list(traits.SkeletonType),
            format_func=lambda skel: skel.value,
        )
        covering = st.selectbox(
            "Covering", list(traits.Covering), format_func=lambda cov: cov.value
        )
        body_segmentation = st.checkbox("Has Segmented Body?")

        st.subheader("Appendages")
        # Putting appendages in a single row to save vertical space
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            legs = st.number_input("Legs", min_value=0, step=1)
        with col2:
            arms = st.number_input("Arms", min_value=0, step=1)
        with col3:
            wings = st.number_input("Wings", min_value=0, step=1)
        with col4:
            tentacles = st.number_input("Tentacles", min_value=0, step=1)

        st.subheader("Physiology & Lifecycle")
        respiration = st.selectbox(
            "Respiration", list(traits.Respiration), format_func=lambda res: res.value
        )
        warm_blooded = st.checkbox("Is Warm-blooded?")
        lays_eggs = st.checkbox("Lays Eggs?")
        metamorphosis = st.checkbox("Undergoes Metamorphosis?")

        st.subheader("Biogeography")
        habitat = st.selectbox(
            "Habitat", list(traits.Habitat), format_func=lambda hab: hab.value
        )

        lat_col, lon_col = st.columns(2)
        with lat_col:
            latitude = st.number_input(
                "Latitude", min_value=-90.0, max_value=90.0, value=0.0, step=0.1
            )
        with lon_col:
            longitude = st.number_input(
                "Longitude", min_value=-180.0, max_value=180.0, value=0.0, step=0.1
            )

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

            # Instantiate the updated Animal class
            new_animal = animal.Animal(
                name=name.strip(),
                symmetry=symmetry,
                skeleton_type=skeleton_type,
                wings=wings,
                legs=legs,
                arms=arms,
                tentacles=tentacles,
                body_segmentation=body_segmentation,
                covering=covering,
                respiration=respiration,
                warm_blooded=warm_blooded,
                lays_eggs=lays_eggs,
                metamorphosis=metamorphosis,
                latitude=latitude,
                longitude=longitude,
                habitat=habitat,
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
