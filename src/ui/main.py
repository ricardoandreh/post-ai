from typing import List

import streamlit as st

from ui import sidebar, copyright, form


def main() -> None:
    title, groq_copyright = st.columns((3, 1))

    with title:
        st.title("🌟 Post AI 🌟")

    with groq_copyright:
        copyright()

    with st.form("post-ai-form", border=False):
        form()

    with st.sidebar:
        sidebar()


if __name__ == "__main__":
    st.set_page_config(
        page_title="Post AI",
        page_icon=":memo:",
        layout="centered",
    )
    
    main()
