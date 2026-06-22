import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Charger variables d'environnement
load_dotenv()

def ingest_pdf(file_path: str, db_path: str = "vectorstore"):
    # Charger PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Découper en chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(documents)

    # Créer les embeddings
    embeddings = OpenAIEmbeddings()

    # Construire la base vectorielle
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(db_path)

    print(f"✅ Ingestion terminée pour {file_path}. Base sauvegardée dans {db_path}")

if __name__ == "__main__":
    ingest_pdf("data/management.pdf")
