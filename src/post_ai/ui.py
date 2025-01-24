import streamlit as st
from post_ai.main import run_via_streamlit

def main():
    st.set_page_config(
        page_title="Post IA", 
        page_icon=":memo:", 
        layout="centered",
    )

    st.title("🌟 Post AI 🌟")

    Tema = st.text_input("Tema do artigo a ser desenvolvido")
    Tom = st.text_input("Qual a abordagem, informal, divertido, jornalístico etc")
    Aspectos = st.text_input("Características, interessante, cativante, factualmente correto etc")

    if st.button("Criar postagem"):
        inputs = {
            "tema": Tema,
            "tom": Tom,
            "aspectos": Aspectos,
        }

        with st.spinner("Gerando sua postagem..."):
            st.markdown(run_via_streamlit(inputs))


if __name__ == "__main__":
    main()
