"""Displays evolutionary tree page"""

import streamlit as st
from streamlit_echarts import st_echarts
from components.util import *
from components.tree import get_graph

initialize_session()

st.title("Evolutionary Tree")
st.write("""
         As you add animals, they will be sorted into an evolutionary tree
         - The **length** of each branch or line represents the evolutionary distance between the two creatures
         - **Hover** over branches to see the exact weight
         - **Click** on a diamond to see more information about the animal
         """)

col1, col2 = st.columns(2)

with col1:
    st.button(
        "Create New Animal",
        type="primary",
        on_click=lambda: st.session_state.update({"popup_open": True}),
        width="stretch",
    )
    if st.button(
        "Back to Home Page",
        type="secondary",
        width="stretch",
    ):
        st.switch_page("Home_Page.py")


with col2:
    st.button(
        "Fetch New Animals", type="secondary", on_click=lambda: fetch_button_callback()
    )

graph = get_graph(25, 18)

echarts_options = {
    "backgroundColor": "#c1ceb3",
    "tooltip": {},
    "legend": [
        {
            "data": ["Extant Species", "Ancestral Node"],
            "top": "bottom",
            "icon": "diamond",  # Forces legend icons to match your tree node shape
        }
    ],
    "series": [
        {
            "type": "graph",
            "layout": "force",
            "roam": True,
            "symbol": "diamond",
            "force": {
                "repulsion": 400,
                "edgeLength": [20, 80],
            },
            "label": {"show": True, "position": "top"},
            "edgeLabel": {"show": False},
            "lineStyle": {
                "width": 3,
                "curviness": 0.3,
                "type": "solid",
                "color": "#5B3E00",
            },
            "data": graph["data"],
            "links": graph["links"],
            "draggable": True,
        }
    ],
}

with st.spinner("Decoding DNA sequences, Deciphering phylogenetics", show_time=True):
    st_echarts(options=echarts_options, height="500px")
