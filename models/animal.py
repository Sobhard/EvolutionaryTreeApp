"""Animal class to hold animal data, contains serializaiton and deserialization methods."""

from models import traits
import streamlit as st


class Animal:
    """Class to hold animal data"""

    def __init__(
        self,
        name: str,
        trophic_level: traits.TrophicLevel,
        habitat: traits.Habitat,
        covering: traits.Covering,
        locomotion: traits.Locomotion,
        num_limbs: int,
        user_generated: bool,
    ):

        self.name = name
        self.trophic_level = trophic_level
        self.habitat = habitat
        self.locomotion = locomotion
        self.covering = covering
        self.num_limbs = num_limbs
        self.user_generated = user_generated

    # -------------------------------SERIALIZATION METHODS-----------------------------
    def to_dict(self) -> dict:
        """Serializes the animal object into a dictionary with all the fields"""
        return {
            "name": self.name,
            "trophic_level": self.trophic_level.value,
            "habitat": self.habitat.value,
            "locomotion": self.locomotion.value,
            "covering": self.covering.value,
            "num_limbs": self.num_limbs,
            "user_generated": self.user_generated,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Creates an animal object from dict fetched from database"""
        return cls(
            name=data["name"],
            trophic_level=traits.TrophicLevel(data["trophic_level"]),
            habitat=traits.Habitat(data["habitat"]),
            covering=traits.Covering(data["covering"]),
            locomotion=traits.Locomotion(data["locomotion"]),
            num_limbs=data["num_limbs"],
            user_generated=data["user_generated"],
        )

    # -------------------------------DISPLAY METHODS-----------------------------------
    @st.dialog("Animal Details")
    def display_details(self):
        """Displays the details of the animal in a dialog."""
        st.write(f"Name: {self.name}")
        st.write(f"Trophic Level: {self.trophic_level.value}")
        st.write(f"Habitat: {self.habitat.value}")
        st.write(f"Covering: {self.covering.value}")
        st.write(f"Locomotion: {self.locomotion.value}")
        st.write(f"Number of Limbs: {self.num_limbs}")

    def write_animal_name_clickable(self):
        """Displays animal name as a clickable text that opens more details"""
        if st.button(f"{self.name}", type="tertiary"):
            self.display_details()
