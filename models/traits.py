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
