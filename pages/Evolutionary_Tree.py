import streamlit as st
from streamlit_echarts import st_echarts
from components.database import fetch_animals
from components.util import initialize_session
from components.tree import get_graph

initialize_session()

st.title("Evolutionary Tree")
st.write("As you add animals, they will be sorted into an evolutionary tree")

st.button(
    "Fetch New Animals", on_click=lambda: fetch_animals(st.session_state.database)
)

graph = get_graph(15, 5)

echarts_options = {
    "series": [
        {
            "type": "graph",
            "layout": "force",
            "roam": True,
            "symbol": "diamond",
            "force": {
                "repulsion": 100,
                # ECharts automatically scales the visual distance based on the "value"
                # key in your links list. If you want to bound the shortest and longest
                # branches to specific pixel lengths later, you can add: "edgeLength":
            },
            "label": {"show": True, "position": "top"},
            "edgeLabel": {"show": False},
            "lineStyle": {
                "width": 2,
                "type": "solid",
                # Can add color here
            },
            "data": graph["data"],
            "links": graph["links"],
            "draggable": True,
        }
    ]
}
st_echarts(options=echarts_options, height="400px", theme="light")
