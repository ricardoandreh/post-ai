from typing import List, Tuple

import streamlit as st


def get_inputs() -> Tuple[str, str, str, str]:
    Tema: str = st.text_input("Tema do artigo a ser desenvolvido")

    tone_column, language_column = st.columns((1, 1))

    with tone_column:
        Tom: str = st.pills(
            "Tom (abordagem)",
            (
                "formal", "informal",
                "divertido", "jornalístico",
            ),
            selection_mode="single",
        )

    with language_column:
        Idioma: str = st.selectbox(
            "Idioma base a ser realizado",
            (
                "Português Brasileiro", "Inglês", "Espanhol"
            ),
            placeholder="Escolha um idioma"
        )

    Aspectos: List[str] = st.multiselect(
        "Aspecto (características)",
        (
            "interessante", "cativante",
            "factualmente correto", "sério",
            "embasado", "engraçado", "criativo",
        ),
        max_selections=4,
        placeholder="Selecione no máximo 4 aspectos",
    )

    return (Tema, Tom, Idioma, ", ".join(Aspectos))
