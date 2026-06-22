import re

def clean_text(text):
    """Nettoyage simple du texte utilisateur ou modèle."""
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text
