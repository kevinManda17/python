from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os

# Initialisation
os.environ["OPENAI_API_KEY"] = "sk-..."  # Clé API OpenAI

def setup_qa_system(pdf_path):
    # Étape 1: Extraire et prétraiter le texte
    raw_text = extract_text_from_pdf(pdf_path)
    chunks = clean_and_chunk_text(raw_text)
    
    # Étape 2: Générer les embeddings
    embeddings = generate_embeddings(chunks)
    
    # Étape 3: Créer la base de vecteurs
    vector_db = FAISS.from_texts(chunks, embeddings)
    
    # Étape 4: Initialiser le LLM
    llm = OpenAI(model_name="gpt-4", temperature=0.3)
    
    # Étape 5: Chaîne QA
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever(search_kwargs={"k": 3}),
    )
    
    return qa

# Exemple d'utilisation
if __name__ == "__main__":
    qa_system = setup_qa_system("data/sample.pdf")
    response = qa_system.run("Quelles sont les conclusions de ce document ?")
    print(response)