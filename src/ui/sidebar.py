import streamlit as st

from ui.state import get_all_posts, delete_post, delete_all_posts
from ui.utils import truncate_post_title


@st.fragment
def sidebar() -> None:
    st.header("📜 Histórico")

    if st.button(
        "🗞️ Nova postagem",
        use_container_width=True,
    ):
        del st.session_state["view"]

        st.rerun()
    
    st.markdown("")

    all_posts = get_all_posts()
    
    if all_posts:
        for idx, post in enumerate(all_posts):
            post_title_column, delete_post_column = st.columns((4, 1))
            
            with post_title_column:
                if st.button(
                    truncate_post_title(post["title"]),
                    use_container_width=True,
                    key=f"view_{idx}",
                ):
                    st.session_state["view"] = post["title"]

                    st.rerun()

            with delete_post_column:
                if st.button("🗑️", key=f"delete_{idx}"):
                    delete_post(post["title"])

                    st.rerun()
    else:
        st.write("Nenhum histórico registrado ainda.")
    
    st.divider()

    if st.button(
        "Limpar Todo Histórico",
        use_container_width=True,
        key="clean_history",
    ):
        delete_all_posts()
        
        st.rerun(scope="fragment")
