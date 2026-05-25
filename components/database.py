"""Provides functions to add and read animals from database"""

from supabase import create_client, Client
from models.animal import Animal
import streamlit as st


def get_client() -> Client:
    """Returns supabase anon client"""
    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])


def add_animal(new_animal: Animal, supabase: Client):
    """Adds an animal to the database"""
    animal_data = new_animal.to_dict()
    st.write(animal_data)
    return supabase.table("animals").insert(animal_data).execute()
