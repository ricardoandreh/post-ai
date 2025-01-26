import streamlit as st


def sidebar() -> None:
  with st.sidebar:
        st.header("📜 Histórico")
        
        if st.session_state["history"]:
            for idx, post in enumerate(st.session_state["history"]):
                col1, col2 = st.columns((8, 2))
                
                with col1:
                    if st.button(f"{post["title"]}", key=f"view_{idx}"):
                        st.session_state["view"] = idx

                with col2:
                    if st.button("🗑️", key=f"delete_{idx}"):
                        del st.session_state["history"][idx]
                        st.rerun()

        else:
            st.write("Nenhum histórico registrado ainda.")
        
        st.divider()

        if st.button("Limpar Todo Histórico", key="clean_history"):
            st.session_state["history"] = []
            if "view" in st.session_state:
                del st.session_state["view"]
            st.info("Histórico limpo!", icon="🧹")
