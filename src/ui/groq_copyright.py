import streamlit as st


def copyright() -> None:
    st.html("""           
        <footer style="width: 8vw; margin-top: 20px;">
            <a href="https://groq.com" target="_blank" rel="noopener noreferrer">
                <img
                    src="https://groq.com/wp-content/uploads/2024/03/PBG-mark1-color.svg"
                    alt="Powered by Groq for fast inference."
                />
            </a>
        </footer>""")
