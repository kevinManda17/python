# Chatbot PDF avec OpenAI

Application Streamlit pour poser des questions librement ou interroger le contenu d'un PDF.

## Lancer en local

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
streamlit run src/main.py
```

Par defaut, l'application fonctionne en mode local pour les reponses sur PDF:

```env
LLM_PROVIDER=local
```

Pour activer OpenAI, ajoute ensuite ta cle OpenAI dans `.env` et change le fournisseur:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
```

Sans `LLM_PROVIDER=openai`, aucune requete n'est envoyee a OpenAI.

## Variables utiles

```env
LLM_MODEL=gpt-5.4-mini
LLM_PROVIDER=local
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
TTS_MODEL=gpt-4o-mini-tts
TTS_VOICE=alloy
RETRIEVAL_TOP_K=4
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

## Hebergement

Ne pousse jamais `.env` sur GitHub. Sur Streamlit Cloud, Render, Railway ou Docker, ajoute `OPENAI_API_KEY` dans les secrets ou variables d'environnement de la plateforme.

Commande Docker:

```powershell
docker build -t chatbot-pdf .
docker run --env-file .env -p 8501:8501 chatbot-pdf
```

## Notes de securite

Si une ancienne cle a deja ete presente dans l'historique Git, il faut la revoquer depuis la plateforme OpenAI et en creer une nouvelle.
