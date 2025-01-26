import streamlit as st


def session_state(post_container) -> None:
    if "history" not in st.session_state:
        st.session_state["history"] = []
    
    if "view" in st.session_state:
        selected_idx = st.session_state["view"]

        if 0 <= selected_idx < len(st.session_state["history"]):
            selected_post = st.session_state["history"][selected_idx]
            post_container.markdown(selected_post["response"])
        else:
            st.warning("O item selecionado não está mais disponível.")
            del st.session_state["view"]
