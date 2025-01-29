import streamlit as st
from ui.state import get_one_post

def post_view(post_container) -> None:
    if "view" in st.session_state:
        post_title = st.session_state["view"]

        if (post := get_one_post(post_title)) is not None:
            post and post_container.markdown(post["content"])
        else:
            del st.session_state["view"]
            
            st.warning("O item selecionado não está mais disponível.")
