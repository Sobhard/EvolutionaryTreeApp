"""Provides functions to add and read animals from database"""

from postgrest import APIResponse, CountMethod
from supabase import create_client, Client
from models.animal import Animal
import streamlit as st

ANIMALS_TABLE: str = "animals"


@st.cache_resource
def get_client() -> Client:
    """Returns supabase anon client"""
    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])


def add_animal(new_animal: Animal, db: Client) -> APIResponse:
    """Adds an animal to the database"""
    animal_data: dict = new_animal.to_dict()
    st.write(animal_data)
    return db.table(ANIMALS_TABLE).insert(animal_data).execute()


def session_state_from_response(query_response: APIResponse):
    """Takes an API response and parses it, adding the new objects to the session state"""
    for animal_dict in query_response.model_dump()["data"]:
        st.session_state.animals.append(Animal.from_dict(animal_dict))


def fetch_animals(db: Client):
    """Checks if there is new animals to fetch,
    if yes, adds those new animals to the session state"""

    num_local_animals: int = len(st.session_state.animals)

    if num_local_animals == 0:
        try:
            response: APIResponse = db.table(ANIMALS_TABLE).select("*").execute()
            session_state_from_response(response)

        except Exception as e:
            st.error(f"Failed to load animals {e}")

    # Getting number of rows, if we already have all the rows, return
    try:
        response: APIResponse = (
            db.table(ANIMALS_TABLE)
            .select("*", count=CountMethod.exact, head=False)
            .execute()
        )
        num_rows = response.count

    except Exception as e:
        st.error(f"Failed to get count {e}")

    if num_rows is None:
        return

    if num_local_animals >= num_rows:
        return

    local_animal_names: list[str] = [a.name for a in st.session_state.animals]

    try:
        response = (
            db.table(ANIMALS_TABLE)
            .select("*")
            .not_.in_("name", local_animal_names)
            .execute()
        )

        session_state_from_response(response)

    except Exception as e:
        st.error(f"Failed to update animals list {e}")
