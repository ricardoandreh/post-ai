import streamlit as st

from ui.inputs import display_inputs
from ui.request import generate_post
from ui.view import post_view


def form() -> None:
    display_inputs()

    left_align, _, right_align = st.columns((1, 1, 1))

    post_view()         

    with left_align:
        st.form_submit_button(
            "Criar postagem", 
            on_click=generate_post,
            args=(right_align,),
        )
