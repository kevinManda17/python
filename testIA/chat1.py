import os
import fitz  # PyMuPDF pour extraire le texte des PDFs
import sqlite3
import faiss
import openai
from sentence_transformers import SentenceTransformer
import torch

# Configuration de l'API OpenAI (Remplace avec ta clé API si besoin)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Modèle d'embedding
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Connexion DB
conn = sqlite3.connect("documents.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS documents (id INTEGER PRIMARY KEY, text TEXT)")
conn.commit()

# Fonction pour extraire le texte d'un PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return " ".join([page.get_text() for page in doc])

# Ajouter un PDF à la base de données
def add_pdf_to_db(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    cur.execute("INSERT INTO documents (text) VALUES (?)", (text,))
    conn.commit()

# Indexation avec FAISS
def create_faiss_index():
    cur.execute("SELECT text FROM documents")
    docs = [row[0] for row in cur.fetchall()]
    embeddings = model.encode(docs, convert_to_tensor=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings.cpu().numpy())
    return index, docs

# Recherche dans la base
def search(query, index, docs, top_k=3):
    query_embedding = model.encode([query], convert_to_tensor=True).cpu().numpy()
    D, I = index.search(query_embedding, top_k)
    return [docs[i] for i in I[0]]

# Génération de réponse avec OpenAI
def generate_response(query, context):
    prompt = f"""
    Voici un extrait de document :
    {context}
    
    Question : {query}
    Réponse :
    """
    
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Tu es un assistant intelligent qui répond en se basant sur les documents."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Programme principal
if __name__ == "__main__":
    # Ajouter des PDFs (remplace par tes fichiers)
    add_pdf_to_db("livre-python1.pdf")
    
    # Créer l'index
    index, docs = create_faiss_index()
    
    while True:
        query = input("Pose une question (ou tape 'exit' pour quitter) : ")
        if query.lower() == 'exit':
            break
        results = search(query, index, docs)
        answer = generate_response(query, "\n".join(results))
        print("Réponse :", answer)
