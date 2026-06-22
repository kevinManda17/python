import fitz  # PyMuPDF
import sqlite3
import faiss
from sentence_transformers import SentenceTransformer
import torch

# Modèle d'embedding
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Connexion DB
conn = sqlite3.connect("documents.db")
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

# Exemple d'utilisation
if __name__ == "__main__":
    add_pdf_to_db("livre-python1.pdf")  # Remplace avec ton fichier PDF
    index, docs = create_faiss_index()
    results = search("mot clé de recherche", index, docs)
    print(results)
