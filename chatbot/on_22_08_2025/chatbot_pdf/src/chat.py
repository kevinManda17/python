import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory  # vient bien de langchain.memory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import OpenAIEmbeddings

# Charger les variables d'environnement
load_dotenv()

def start_chat(db_path="vectorstore"):
    # Vérifier la clé OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("⚠️ ERREUR : OPENAI_API_KEY non trouvé dans .env !")

    # Charger la base vectorielle
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(
        db_path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )

    # Définir modèle GPT
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    # Mémoire de conversation
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Construire la chaîne RAG
    qa = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=db.as_retriever(),
        memory=memory
    )

    print("🤖 Chatbot prêt ! Tapez 'exit' pour quitter.\n")

    while True:
        query = input("Vous: ")
        if query.lower() in ["exit", "quit"]:
            break
        result = qa({"question": query})
        print("Bot:", result["answer"])

if __name__ == "__main__":
    start_chat()
