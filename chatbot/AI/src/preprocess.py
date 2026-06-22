import spacy
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Charger le modèle NLP
nlp = spacy.load("fr_core_news_sm")  # Modèle français

def clean_and_chunk_text(text, chunk_size=500):
    # Nettoyage
    text = text.replace("\n", " ").replace("\t", " ").strip()
    
    # Découpage en chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=50
    )
    chunks = text_splitter.split_text(text)
    
    return chunks

def generate_embeddings(chunks):
    # Modèle d'embedding (ex: all-mpnet-base-v2 pour l'anglais, ou paraphrase-multilingual-mpnet-base-v2 pour le multilingue)
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    embeddings = model.encode(chunks)
    return embeddings