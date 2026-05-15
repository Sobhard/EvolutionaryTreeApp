"""Traits for animals"""
from enum import Enum

class TrophicLevel(Enum):
    """Trophic levels for characters."""
    PRODUCER = "Producer"
    PRIMARY_CONSUMER = "Primary Consumer"
    SECONDARY_CONSUMER = "Secondary Consumer"
    TERTIARY_CONSUMER = "Tertiary Consumer"
    DECOMPOSER = "Decomposer"

class Habitat(Enum):
    """Habitats for Animals"""
    TROPICAL_RAIFOREST = "Tropical Rainforest"
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

class COVERING(Enum):
    """Covering types for Animals."""
    FUR = "Fur"
    FEATHERS = "Feathers"
    SCALES = "Scales"
    SKIN = "Skin"
    EXOSKELETON = "Exoskeleton"

class LOCOMOTION(Enum):
    """Locomotion types for Animals."""
    WALKING = "Walking"
    FLYING = "Flying"
    SWIMMING = "Swimming"
    CLIMBING = "Climbing"
    JUMPING = "Jumping"
