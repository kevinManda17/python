chatbot-pdf/
├── requirements.txt
├── Dockerfile
├── .env.example
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── pdf_processor.py
│   │   ├── vector_store.py
│   │   └── chatbot.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── web/
│       ├── __init__.py
│       └── streamlit_app.py
├── data/
│   ├── pdfs/              # PDFs uploadés
│   ├── vector_store/      # Base vectorielle persistante
│   └── temp/              # Fichiers temporaires
├── tests/
│   ├── __init__.py
│   ├── test_pdf_processor.py
│   └── test_chatbot.py
└── docs/
    └── README.md