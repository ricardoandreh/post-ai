import streamlit as st

from post_ai.main import run_via_streamlit

from ui.inputs import get_inputs
from ui.state import save_post
from ui.utils import extract_title
from ui.view import post_view


def form() -> None:
    with st.form("post-ai-form", border=False):
        Tema, Tom, Idioma, Aspectos = get_inputs()

        left_align, _, right_align = st.columns((1, 1, 1))

        post_container = st.container(border=True)

        post_view(post_container)

        with left_align:
            submitted = st.form_submit_button("Criar postagem")

        if submitted:
            inputs = {
                "tema": Tema,
                "tom": Tom,
                "aspectos": Aspectos,
                "idioma": Idioma
            }

            with right_align:
                with st.spinner("Gerando sua postagem..."):
                    response = run_via_streamlit(inputs)

            title = extract_title(response) or Tema

            post_container.markdown(response)

            save_post({
                "title": title,
                "content": response,
            })
