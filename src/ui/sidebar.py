import streamlit as st
from ui.serializers import get_all_posts, delete_post, delete_all_posts

def get_post_title(post_title) -> str:
    if len(post_title) > 28:
        return f"{post_title[:25]}..."
    
    return f"{post_title[:28]}"

def sidebar() -> None:
    with st.sidebar:
        st.header("📜 Histórico")

        all_posts = get_all_posts()
        
        if all_posts:
            for idx, post in enumerate(all_posts):
                col1, col2 = st.columns((4, 1))
                
                with col1:
                    if st.button(get_post_title(post["title"]), key=f"view_{idx}"):
                        st.session_state["view"] = post["title"]

                        st.rerun()

                with col2:
                    if st.button("🗑️", key=f"delete_{idx}"):
                        delete_post(post["title"])

                        st.rerun()

        else:
            st.write("Nenhum histórico registrado ainda.")
        
        st.divider()

        if st.button("Limpar Todo Histórico", key="clean_history"):
            st.session_state.history = []
            delete_all_posts()

            if "view" in st.session_state:
                del st.session_state["view"]
            
            st.info("Histórico limpo!", icon="🧹")
