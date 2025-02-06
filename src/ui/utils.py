import re
from typing import Optional

import streamlit as st


def truncate_post_title(post_title: str) -> str:
    """Formats the title to display at sidebar."""
    if len(post_title) > 28:
        return f"{post_title[:23]}..."
    
    return post_title[:28]

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
