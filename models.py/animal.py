"""Animal class to hold animal data, contains serializaiton and deserialization methods."""
import traits as traits

class Animal:
    """Class to hold animal data"""
    def __init__(self,
                 name: str,
                 tropic_level: traits.TrophicLevel,
                 habitat: traits.Habitat,
                 covering: traits.Covering,
                 locomotion: traits.Locomotion,
                 num_limbs: int):

        self.name = name
        self.tropic_level = tropic_level
        self.habitat = habitat
        self.locomotion = locomotion
        self.covering = covering
        self.num_limbs = num_limbs

