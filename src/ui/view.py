import streamlit as st
from ui.state import get_one_post


def post_view() -> None:
    post_container = st.container(border=True)

    if "view" in st.session_state:
        post_title = st.session_state["view"]

        if (post := get_one_post(post_title)) is not None:
            post_container.markdown(post["content"])

            return None

        del st.session_state["view"]
        
        st.warning("O item selecionado não está mais disponível.")
