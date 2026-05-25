"""Provides functions to add and read animals from database"""

from postgrest import APIResponse
from supabase import create_client, Client
from models.animal import Animal
import streamlit as st


@st.cache_resource
def get_client() -> Client:
    """Returns supabase anon client"""
    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])


def add_animal(new_animal: Animal, supabase: Client) -> APIResponse:
    """Adds an animal to the database"""
    animal_data: dict = new_animal.to_dict()
    st.write(animal_data)
    return supabase.table("animals").insert(animal_data).execute()
