from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_embeddings(texts):
    """Crée un index vectoriel pour les textes donnés."""
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(texts, embeddings)
    return vector_store

def query_embeddings(vector_store, query):
    """Interroge le vector store avec une question."""
    retriever = vector_store.as_retriever()
    return retriever.get_relevant_documents(query)
