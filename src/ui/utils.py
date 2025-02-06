import re
from typing import Optional

import streamlit as st


def get_post_title(post_title: str) -> str:
    if len(post_title) > 28:
        return f"{post_title[:25]}..."
    
    return post_title[:28]

def reset_post_view() -> None:
    if "view" in st.session_state:
        del st.session_state["view"]


def extract_title(response) -> Optional[str]:
    """Extracts the title from the post text based on the patterns provided."""
    regex_patterns = (
        r"^\*\*(.*?)\*\*\n",
        r"^# (.*?)\n",
        r"^## (.*?)\n",
        r"^### (.*?)\n",
        r"^Título: (.*?)\n",
        r"^\*\*Título: (.*?)\*\*\n",
    )
    
    for pattern in regex_patterns:
        match = re.search(pattern, response)
        
        if match is not None:
            return match.group(1).strip()
    
    return None
