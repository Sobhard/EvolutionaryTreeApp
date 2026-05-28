"""Util functions for streamlit app"""

from pathlib import Path

import streamlit as st
import re
from components.database import get_client, fetch_animals


def initialize_session():
    """
    Initializes database connections and fetches initial data.
    """
    if "app_initialized" not in st.session_state:

        with st.spinner("Excavating fossil records... (Fetching from database)"):

            st.session_state.database = get_client()
            st.session_state.setdefault("animals", [])

            fetch_animals(st.session_state.database)

            st.session_state.app_initialized = True


def fetch_button_callback():
    """Lambda for the fetch button, fetches and writes whether it was successful or not"""
    fetched = fetch_animals(st.session_state.database)

    if fetched:
        st.caption("Fetched New Animals (Success)")

    else:
        st.caption("No new animals to fetch. You're up to date!")


def switch_to_page(page_name: str):
    """
    Switches to page

    Input: Name of python file to Switch to
    """
    st.switch_page(Path("pages") / page_name)


regex_list = [
    r"^[a@][s\$][s\$]$",
    r"[a@][s\$][s\$]h[o0][l1][e3][s\$]?",
    r"b[a@][s\$][t\+][a@]rd",
    r"b[e3][a@][s\$][t\+][i1][a@]?[l1]([i1][t\+]y)?",
    r"b[e3][a@][s\$][t\+][i1][l1][i1][t\+]y",
    r"b[e3][s\$][t\+][i1][a@][l1]([i1][t\+]y)?",
    r"b[i1][t\+]ch[s\$]?",
    r"b[i1][t\+]ch[e3]r[s\$]?",
    r"b[i1][t\+]ch[e3][s\$]",
    r"b[i1][t\+]ch[i1]ng?",
    r"b[l1][o0]wj[o0]b[s\$]?",
    r"c[l1][i1][t\+]",
    r"^(c|k|ck|q)[o0](c|k|ck|q)[s\$]?$",
    r"(c|k|ck|q)[o0](c|k|ck|q)[s\$]u",
    r"(c|k|ck|q)[o0](c|k|ck|q)[s\$]u(c|k|ck|q)[e3]d",
    r"(c|k|ck|q)[o0](c|k|ck|q)[s\$]u(c|k|ck|q)[e3]r",
    r"(c|k|ck|q)[o0](c|k|ck|q)[s\$]u(c|k|ck|q)[i1]ng",
    r"(c|k|ck|q)[o0](c|k|ck|q)[s\$]u(c|k|ck|q)[s\$]",
    r"^cum[s\$]?$",
    r"cumm??[e3]r",
    r"cumm?[i1]ngcock",
    r"(c|k|ck|q)um[s\$]h[o0][t\+]",
    r"(c|k|ck|q)un[i1][l1][i1]ngu[s\$]",
    r"(c|k|ck|q)un[i1][l1][l1][i1]ngu[s\$]",
    r"(c|k|ck|q)unn[i1][l1][i1]ngu[s\$]",
    r"(c|k|ck|q)un[t\+][s\$]?",
    r"(c|k|ck|q)un[t\+][l1][i1](c|k|ck|q)",
    r"(c|k|ck|q)un[t\+][l1][i1](c|k|ck|q)[e3]r",
    r"(c|k|ck|q)un[t\+][l1][i1](c|k|ck|q)[i1]ng",
    r"cyb[e3]r(ph|f)u(c|k|ck|q)",
    r"d[a@]mn",
    r"d[i1]ck",
    r"d[i1][l1]d[o0]",
    r"d[i1][l1]d[o0][s\$]",
    r"d[i1]n(c|k|ck|q)",
    r"d[i1]n(c|k|ck|q)[s\$]",
    r"[e3]j[a@]cu[l1]",
    r"(ph|f)[a@]g[s\$]?",
    r"(ph|f)[a@]gg[i1]ng",
    r"(ph|f)[a@]gg?[o0][t\+][s\$]?",
    r"(ph|f)[a@]gg[s\$]",
    r"(ph|f)[e3][l1][l1]?[a@][t\+][i1][o0]",
    r"(ph|f)u(c|k|ck|q)",
    r"(ph|f)u(c|k|ck|q)[s\$]?",
    r"g[a@]ngb[a@]ng[s\$]?",
    r"g[a@]ngb[a@]ng[e3]d",
    r"g[a@]y",
    r"h[o0]m?m[o0]",
    r"h[o0]rny",
    r"j[a@](c|k|ck|q)\-?[o0](ph|f)(ph|f)?",
    r"j[e3]rk\-?[o0](ph|f)(ph|f)?",
    r"j[i1][s\$z][s\$z]?m?",
    r"[ck][o0]ndum[s\$]?",
    r"mast(e|ur)b(8|ait|ate)",
    r"n+[i1]+[gq]+[e3]*r+[s\$]*",
    r"[o0]rg[a@][s\$][i1]m[s\$]?",
    r"[o0]rg[a@][s\$]m[s\$]?",
    r"p[e3]nn?[i1][s\$]",
    r"p[i1][s\$][s\$]",
    r"p[i1][s\$][s\$][o0](ph|f)(ph|f)",
    r"p[o0]rn",
    r"p[o0]rn[o0][s\$]?",
    r"p[o0]rn[o0]gr[a@]phy",
    r"pr[i1]ck[s\$]?",
    r"pu[s\$][s\$][i1][e3][s\$]",
    r"pu[s\$][s\$]y[s\$]?",
    r"[s\$][e3]x",
    r"[s\$]h[i1][t\+][s\$]?",
    r"[s\$][l1]u[t\+][s\$]?",
    r"[s\$]mu[t\+][s\$]?",
    r"[s\$]punk[s\$]?",
    r"[t\+]w[a@][t\+][s\$]?",
]
combined_pattern = f"({'|'.join(regex_list)})"
compiled_regex = re.compile(combined_pattern, re.IGNORECASE)


def contains_bad_word(text: str) -> bool:
    """
    Checks if the given text contains any of the bad words defined in the compiled regex.
    """
    if compiled_regex.search(text):
        return True
    return False
