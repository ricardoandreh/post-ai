import streamlit as st
from ui.serializers import get_one_post

def session_state(post_container) -> None:
    if "history" not in st.session_state:
        st.session_state.history = []
    
    if "view" in st.session_state:
        post_title = st.session_state["view"]

        if (post := get_one_post(post_title)) is not False:
            post_container.markdown(post["content"])
        else:
            del st.session_state["view"]
            
            st.warning("O item selecionado não está mais disponível.")
