import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from flask import Flask, render_template, request, redirect, session
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# Définir la clé API OpenAI ici (en dur)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Assurer que la clé API est bien dans les variables d'environnement
if not OPENAI_API_KEY:
    raise RuntimeError("La variable OPENAI_API_KEY doit être définie.")

# Initialisation de Flask
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Pour la gestion de la session

# Fonctions de traitement des documents et de l'IA
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# Routes Flask
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_documents():
    # Récupérer les fichiers PDF téléchargés
    pdf_docs = request.files.getlist('pdf_docs')
    
    # Extraire le texte des fichiers PDF
    raw_text = get_pdf_text(pdf_docs)
    
    # Diviser le texte en morceaux
    text_chunks = get_text_chunks(raw_text)
    
    # Créer le VectorStore avec les embeddings
    vectorstore = get_vectorstore(text_chunks)
    
    # Créer la chaîne de conversation avec la mémoire et le retriever
    conversation_chain = get_conversation_chain(vectorstore)
    
    # Stocker la chaîne de conversation dans la session
    session['conversation_chain'] = conversation_chain
    return redirect('/chat')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    # Récupérer la chaîne de conversation de la session
    conversation_chain = session.get('conversation_chain', None)
    
    if not conversation_chain:
        return redirect('/')
    
    chat_history = []
    if request.method == 'POST':
        user_question = request.form['user_question']
        
        # Utiliser la chaîne de conversation pour obtenir une réponse
        response = conversation_chain({'question': user_question})
        
        # Mettre à jour l'historique de chat dans la session
        chat_history = response['chat_history']
        session['chat_history'] = chat_history

    return render_template('chat.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
