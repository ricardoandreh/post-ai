from typing import List

import streamlit as st


def display_inputs() -> None:
    st.text_input(
        "Tema do artigo a ser desenvolvido",
        key="theme",
    )

    tone_column, language_column = st.columns((1, 1))

    with tone_column:
        st.pills(
            "Tom (abordagem)",
            (
                "formal", "informal",
                "divertido", "jornalístico",
            ),
            selection_mode="single",
            key="tone",
        )

    with language_column:
        st.selectbox(
            "Idioma base a ser realizado",
            (
                "Português Brasileiro", "Inglês", "Espanhol"
            ),
            placeholder="Escolha um idioma",
            key="language",
        )

    st.multiselect(
        "Aspecto (características)",
        (
            "interessante", "cativante",
            "factualmente correto", "sério",
            "embasado", "engraçado", "criativo",
        ),
        max_selections=4,
        placeholder="Selecione no máximo 4 aspectos",
        key="aspects",
    )
