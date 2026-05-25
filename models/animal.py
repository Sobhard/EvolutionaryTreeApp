"""Animal class to hold animal data, contains serialization and deserialization methods."""

from models import traits
import streamlit as st


class Animal:
    """Class to hold animal data"""

    def __init__(
        self,
        name: str,
        symmetry: traits.Symmetry,
        skeleton_type: traits.SkeletonType,
        wings: int,
        legs: int,
        arms: int,
        tentacles: int,
        body_segmentation: bool,
        covering: traits.Covering,
        respiration: traits.Respiration,
        warm_blooded: bool,
        lays_eggs: bool,
        metamorphosis: bool,
        habitat: traits.Habitat,
        region: traits.Region,
        user_generated: bool = True,
    ):

        self.id = id
        self.name = name
        self.symmetry = symmetry
        self.skeleton_type = skeleton_type
        self.wings = wings
        self.legs = legs
        self.arms = arms
        self.tentacles = tentacles
        self.body_segmentation = body_segmentation
        self.covering = covering
        self.respiration = respiration
        self.warm_blooded = warm_blooded
        self.lays_eggs = lays_eggs
        self.metamorphosis = metamorphosis
        self.habitat = habitat
        self.region = region
        self.user_generated = user_generated

    # -------------------------------SERIALIZATION METHODS-----------------------------
    def to_dict(self) -> dict:
        """Serializes the animal object into a dictionary with all the fields to send to Supabase."""
        return {
            "name": self.name,
            "symmetry": self.symmetry.value,
            "skeleton_type": self.skeleton_type.value,
            "wings": self.wings,
            "legs": self.legs,
            "arms": self.arms,
            "tentacles": self.tentacles,
            "body_segmentation": self.body_segmentation,
            "covering": self.covering.value,
            "respiration": self.respiration.value,
            "warm_blooded": self.warm_blooded,
            "lays_eggs": self.lays_eggs,
            "metamorphosis": self.metamorphosis,
            "habitat": self.habitat.value,
            "region": self.region.value,
            "user_generated": self.user_generated,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Creates an animal object from a dictionary fetched from the database."""
        return cls(
            name=data["name"],
            symmetry=traits.Symmetry(data["symmetry"]),
            skeleton_type=traits.SkeletonType(data["skeleton_type"]),
            wings=data.get("wings", 0),  # Using .get() with a default of 0 for safety
            legs=data.get("legs", 0),
            arms=data.get("arms", 0),
            tentacles=data.get("tentacles", 0),
            body_segmentation=data["body_segmentation"],
            covering=traits.Covering(data["covering"]),
            respiration=traits.Respiration(data["respiration"]),
            warm_blooded=data["warm_blooded"],
            lays_eggs=data["lays_eggs"],
            metamorphosis=data["metamorphosis"],
            habitat=traits.Habitat(data["habitat"]),
            region=traits.Region(data["region"]),
            user_generated=data.get("user_generated", True),
        )

    # -------------------------------DISPLAY METHODS-----------------------------------
    @st.dialog("Animal Details")
    def display_details(self):
        """Displays the details of the animal in a clean, sectioned dialog."""
        st.subheader(f"Name: {self.name}")

        st.write("### Morphology")
        st.write(f"**Symmetry:** {self.symmetry.value}")
        st.write(f"**Skeleton:** {self.skeleton_type.value}")
        st.write(f"**Body Covering:** {self.covering.value}")
        st.write(f"**Segmented Body:** {'Yes' if self.body_segmentation else 'No'}")

        st.write("### Appendages")
        st.write(
            f"**Legs:** {self.legs} | **Arms:** {self.arms} | **Wings:** {self.wings} | **Tentacles:** {self.tentacles}"
        )

        st.write("### Physiology & Lifecycle")
        st.write(f"**Respiration:** {self.respiration.value}")
        st.write(f"**Warm-blooded:** {'Yes' if self.warm_blooded else 'No'}")
        st.write(f"**Lays Eggs:** {'Yes' if self.lays_eggs else 'No'}")
        st.write(f"**Metamorphosis:** {'Yes' if self.metamorphosis else 'No'}")

        st.write("### Biogeography")
        st.write(f"**Habitat:** {self.habitat.value}")

    def write_animal_name_clickable(self):
        """Displays animal name as a clickable text that opens more details."""
        if st.button(f"{self.name}", type="tertiary"):
            self.display_details()
