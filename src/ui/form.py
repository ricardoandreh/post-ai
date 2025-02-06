import streamlit as st

from post_ai.main import run_via_streamlit

from ui.inputs import display_inputs
from ui.state import save_post
from ui.utils import extract_title
from ui.view import post_view


def generate_post(right_align) -> None:
    inputs = {
        "tema": st.session_state.tema,
        "tom": st.session_state.tom,
        "idioma": st.session_state.idioma,
        "aspectos": ", ".join(st.session_state.aspectos),
    }

    with right_align:
        with st.spinner("Gerando sua postagem..."):
            response = run_via_streamlit(inputs)

    title = extract_title(response) or Tema

    st.session_state["view"] = title

    save_post({
        "title": title,
        "content": response,
    })

def form() -> None:
    display_inputs()

    left_align, _, right_align = st.columns((1, 1, 1))

    post_view()         

    with left_align:
        submitted = st.form_submit_button(
            "Criar postagem", 
            on_click=generate_post,
            args=(right_align,),
        )
