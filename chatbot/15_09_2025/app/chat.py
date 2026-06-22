from app.model import model, tokenizer
import torch
import json
import os

HISTORY_FILE = "data/history.json"

# Charger l'historique existant ou créer vide
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)
else:
    history = []

def add_to_history(user_input, bot_response):
    history.append({"user": user_input, "bot": bot_response})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def generate_chat_response(user_input, max_tokens=200):
    # Concaténer l'historique pour le contexte
    prompt = ""
    for turn in history[-5:]:  # on garde les 5 derniers échanges pour mémoire
        prompt += f"User: {turn['user']}\nAssistant: {turn['bot']}\n"
    prompt += f"User: {user_input}\nAssistant:"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=max_tokens)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Extraire seulement la réponse
    response = response[len(prompt):].strip()

    # Sauvegarder dans l'historique
    add_to_history(user_input, response)
    return response
