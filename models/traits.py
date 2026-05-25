"""Traits for animals"""

from enum import Enum


class Symmetry(Enum):
    """Symmetry types for animals."""

    BILATERAL = "Bilateral"
    RADIAL = "Radial"
    ASYMMETRICAL = "Asymmetrical"


class SkeletonType(Enum):
    """Skeleton types for animals."""

    ENDOSKELETON = "Endoskeleton"
    EXOSKELETON = "Exoskeleton"
    HYDROSTATIC = "Hydrostatic"
    NONE = "None"


class Covering(Enum):
    """Covering types for animals."""

    HAIR_FUR = "Hair/Fur"
    FEATHERS = "Feathers"
    SCALES = "Scales"
    CHITIN = "Chitin"
    SMOOTH_SKIN = "Smooth/Permeable Skin"
    MUCUS = "Mucus"


class Respiration(Enum):
    """Respiration systems for animals."""

    LUNGS = "Lungs"
    GILLS = "Gills"
    DIFFUSION = "Skin/Diffusion"
    SPIRACLES = "Spiracles/Trachea"


class Habitat(Enum):
    """Habitats for animals."""

    TROPICAL_RAINFOREST = "Tropical Rainforest"
    TEMPERATE_FOREST = "Temperate Forest"
    TUNDRA = "Tundra"
    POLAR = "Polar"
    LAKE = "Lake"
    RIVER = "River"
    OCEAN = "Ocean"
    REEF = "Reef"
    DESERT = "Desert"
    GRASSLAND = "Grassland"
    TAIGA = "Taiga"


class Region(Enum):
    """
    World regions that correspond to ancient tectonic bodies
    """

    NORTH_AMERICA = "North America"
    EURASIA = "Europe & Northern Asia"
    SOUTH_AMERICA = "South America"
    AFRICA = "Africa"
    AUSTRALIA_ANTARCTICA = "Australia & Antarctica"
    CENTRAL_AMERICA_CARIBBEAN = "Central America & Caribbean"
    MEDITERRANEAN_TETHYS = "Mediterranean & Middle East"
    INDIAN_SUBCONTINENT = "Indian Subcontinent"
    MADAGASCAR = "Madagascar"
    OCEAN = "Ocean"

    @property
    def ancient_continent(self) -> str:
        """Maps the modern region back to its high-level Cretaceous paleogeographic origin."""
        if self in (Region.NORTH_AMERICA, Region.EURASIA):
            return "Laurasia"

        elif self in (
            Region.SOUTH_AMERICA,
            Region.AFRICA,
            Region.AUSTRALIA_ANTARCTICA,
            Region.MADAGASCAR,
        ):
            return "Gondwana"

        elif self == Region.INDIAN_SUBCONTINENT:
            return "Gondwana Island"

        elif self in (Region.CENTRAL_AMERICA_CARIBBEAN, Region.MEDITERRANEAN_TETHYS):
            return "Tethys/Tectonic Bridge"

        else:
            return "Panthalassa Ocean"
