import re
from typing import Optional


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
