from typing import List

import streamlit as st

from ui import sidebar, copyright, form

st.set_page_config(
    page_title="Post AI",
    page_icon=":memo:",
    layout="centered",
)

def main() -> None:
    title, groq_copyright = st.columns((3, 1))

    with title:
        st.title("🌟 Post AI 🌟")

    with groq_copyright:
        copyright()

    form()

    sidebar()


if __name__ == "__main__":
    main()
