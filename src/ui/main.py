import streamlit as st

from post_ai.main import run_via_streamlit
from ui import extract_title, session_state, sidebar, copyright, save_post

st.set_page_config(
    page_title="Post AI",
    page_icon=":memo:",
    layout="centered",
)

def main() -> None:
    title, groq_copyright = st.columns((3, 1))

    with title:
        st.title("🌟 Post AI 🌟")

    copyright(groq_copyright)

    Tema = st.text_input("Tema do artigo a ser desenvolvido")

    Tom = st.pills(
        "Tom (abordagem)",
        [
            "formal", "informal",
            "divertido", "jornalístico",
        ],
        selection_mode="single",
    )

    Aspectos = st.multiselect(
        "Aspecto (características)",
        [
            "interessante", "cativante",
            "factualmente correto", "sério",
            "embasado", "engraçado", "criativo",
        ],
        max_selections=4,
    )

    left_align, center_align, right_align = st.columns((1, 1, 1))

    post_container = st.container(border=True)

    session_state(post_container)

    with left_align:
        submit_button = st.button("Criar postagem")

    if submit_button:
        inputs = {
            "tema": Tema,
            "tom": Tom,
            "aspectos": ", ".join(Aspectos),
        }

        with right_align:
            with st.spinner("Gerando sua postagem..."):
                response = run_via_streamlit(inputs)

        title = extract_title(response) or Tema

        save_post({
            "title": title,
            "content": response
        })

        post_container.markdown(response)

        st.session_state["history"].append({"title": title, "response": response})
    
    sidebar()


if __name__ == "__main__":
    main()
