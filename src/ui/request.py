import streamlit as st

from post_ai.main import run_via_streamlit

from ui.state import save_post
from ui.utils import extract_title


def generate_post(align_column) -> None:
    inputs = {
        "tema": st.session_state.theme,
        "tom": st.session_state.tone,
        "idioma": st.session_state.language,
        "aspectos": ", ".join(st.session_state.aspects),
    }

    with align_column:
        with st.spinner("Gerando sua postagem..."):
            response = run_via_streamlit(inputs)

    title = extract_title(response) or st.session_state.theme

    st.session_state["view"] = title

    save_post({
        "title": title,
        "content": response,
    })
