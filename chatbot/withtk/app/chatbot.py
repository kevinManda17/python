import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Charger la clé API OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def create_chatbot(vector_store):
    """
    Crée un chatbot basé sur GPT et un index vectoriel.
    """
    if not api_key:
        raise ValueError("La clé API OpenAI n'a pas été trouvée. Vérifiez votre fichier .env.")
    
    # Initialisation du modèle LLM
    llm = OpenAI(model_name="gpt-4", temperature=0, openai_api_key=api_key)
    
    # Création du récupérateur à partir de l'index vectoriel
    retriever = vector_store.as_retriever()
    
    # Création de la chaîne de questions-réponses
    qa_chain = RetrievalQA(llm=llm, retriever=retriever)
    
    return qa_chain

def ask_question(chatbot, question):
    """
    Pose une question au chatbot et retourne la réponse.

    Args:
        chatbot: La chaîne QA créée par `create_chatbot`.
        question: La question posée par l'utilisateur.

    Returns:
        La réponse générée par le chatbot.
    """
    try:
        # Utilisation du chatbot pour répondre à la question
        answer = chatbot.run(question)
        return answer
    except Exception as e:
        return f"Erreur lors de la génération de la réponse : {e}"
