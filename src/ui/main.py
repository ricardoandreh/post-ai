import streamlit as st

from post_ai.main import run_via_streamlit
from ui import extract_title, session_state, sidebar

st.set_page_config(
    page_title="Post AI",
    page_icon=":memo:",
    layout="centered",
)

def main() -> None:
    st.title("🌟 Post AI 🌟")

    Tema = st.text_input("Tema do artigo a ser desenvolvido")
    Tom = st.text_input("Qual a abordagem, informal, divertido, jornalístico etc")
    Aspectos = st.text_input("Características, interessante, cativante, factualmente correto etc")

    col1, _, col2 = st.columns((3, 6, 4))

    post_container = st.container(border=True)

    session_state(post_container)

    with col1:
        submit_button = st.button("Criar postagem")

    if submit_button:
        inputs = {
            "tema": Tema,
            "tom": Tom,
            "aspectos": Aspectos,
        }

        with col2:
            with st.spinner("Gerando sua postagem..."):
                response = run_via_streamlit(inputs)

        title = extract_title(response) or Tema

        post_container.markdown(response)

        st.session_state["history"].append({"title": title, "response": response})
    
    sidebar()


if __name__ == "__main__":
    main()
