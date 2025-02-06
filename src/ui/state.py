from pathlib import Path
import pickle
from typing import List, Optional, Dict, Any

POSTS_FOLDER = Path(__file__).parent / "posts"
POSTS_FOLDER.mkdir(exist_ok=True)

def save_post(post: Dict[str, Any]) -> bool:
    """Salva uma postagem em um arquivo Pickle."""
    if not post or "title" not in post or "content" not in post:
        return False
    
    file_path = POSTS_FOLDER / post["title"]
    
    try:
        with open(file_path, "wb") as f:
            pickle.dump(post, f)
        
        return True
    except Exception as e:
        print(f"Erro ao salvar post: {str(e)}")
        
        return False

def get_one_post(post_title: str) -> Optional[Dict[str, str]]:
    """Recupera uma postagem específica pelo título."""
    file_path = POSTS_FOLDER / post_title
    
    if not file_path.exists():
        return None
    
    try:
        with open(file_path, "rb") as f:
            post = pickle.load(f)

            if "title" not in post or "content" not in post:
                return None
            
            return post
    except Exception as e:
        print(f"Erro ao recuperar post: {str(e)}")
        return None

def get_all_posts() -> List[Dict[str, str]]:
    """Recupera todas as postagens salvas."""
    posts = []
    
    for file in POSTS_FOLDER.glob("*"):
        try:
            with open(file, "rb") as f:
                post = pickle.load(f)
                
                if "title" in post and "content" in post:
                    posts.append(post)
        except Exception as e:
            continue
    
    return posts

def delete_post(post_title: str) -> Optional[bool]:
    """Remove uma postagem pelo título."""
    file_path = POSTS_FOLDER / post_title
    
    if not file_path.exists():
        return None
    
    try:
        file_path.unlink(missing_ok=False)

        return True
    except Exception as e:
        print(f"Erro ao remover post {post_title}: {str(e)}")
        return False

def delete_all_posts() -> Optional[bool]:
    """Remove todas as postagens salvas no diretório 'posts'."""
    if not POSTS_FOLDER.exists():
        return None
    
    for file in POSTS_FOLDER.iterdir():
        if file.is_file() and file.name != ".gitkeep":
            try:
                file.unlink()
            except Exception as e:
                print(f"Erro ao remover arquivo {file}: {str(e)}")
    
    return True
