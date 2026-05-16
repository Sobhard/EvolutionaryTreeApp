"""Animal class to hold animal data, contains serializaiton and deserialization methods."""

from models import traits
import streamlit as st


class Animal:
    """Class to hold animal data"""

    def __init__(
        self,
        name: str,
        tropic_level: traits.TrophicLevel,
        habitat: traits.Habitat,
        covering: traits.Covering,
        locomotion: traits.Locomotion,
        num_limbs: int,
    ):

        self.name = name
        self.tropic_level = tropic_level
        self.habitat = habitat
        self.locomotion = locomotion
        self.covering = covering
        self.num_limbs = num_limbs

    @st.dialog("Animal Details")
    def display_details(self):
        """Displays the details of the animal in a dialog."""
        st.write(f"Name: {self.name}")
        st.write(f"Trophic Level: {self.tropic_level.value}")
        st.write(f"Habitat: {self.habitat.value}")
        st.write(f"Covering: {self.covering.value}")
        st.write(f"Locomotion: {self.locomotion.value}")
        st.write(f"Number of Limbs: {self.num_limbs}")

    def write_animal_name_clickable(self):
        """Displays animal name as a clickable text that opens more details"""
        if st.button(f"{self.name}", type="tertiary"):
            self.display_details()
