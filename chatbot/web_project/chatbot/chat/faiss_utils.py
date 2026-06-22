import os
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Dossiers
DATA_DIR = "data/"
INDEX_DIR = "faiss_index/"

# Fonction pour créer un index FAISS
def create_faiss_index():
    documents = []
    for file_name in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, file_name)
        if os.path.isfile(file_path):
            loader = TextLoader(file_path)
            documents.extend(loader.load())

    # Générer les embeddings et créer l'index
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(INDEX_DIR)
    return vectorstore

# Fonction pour charger un index FAISS existant
def load_faiss_index():
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    return FAISS.load_local(INDEX_DIR, embeddings)
