import streamlit as st
import pandas as pd

# st.title("Bienvenue sur mon application Streamlit !")
# st.write("Ceci est une application interactive.")

# # Ajouter un bouton
# if st.button("Cliquez-moi"):
#     st.write("Vous avez cliqué sur le bouton !")

# # Ajouter un champ de saisie
# nom = st.text_input("Entrez votre nom :")
# st.write(f"Bonjour, {nom} 👋")

# # Ajouter un curseur
# age = st.slider("Sélectionnez votre âge :", 0, 100, 25)
# st.write(f"Votre âge est {age} ans.")



# # Création d'un DataFrame
# df = pd.DataFrame({
#     'Nom': ['Alice', 'Bob', 'Charlie'],
#     'Âge': [25, 30, 35],
#     'Score': [88, 92, 79]
# })

# st.write("📊 Voici un tableau de données :")
# st.dataframe(df)


import streamlit as st
import os
import openai

# Configuration de votre clé OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🤖 Chatbot IA avec Streamlit")

# Zone de saisie utilisateur
user_input = st.text_input("Posez une question au chatbot :")

if st.button("Envoyer"):
    if user_input:
        # Appel à l'API OpenAI (GPT-4)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write("💬 Réponse :", response["choices"][0]["message"]["content"])
    else:
        st.warning("Veuillez entrer un message !")
