import sqlite3
from tkinter import filedialog, messagebox
import os
from PyPDF2 import PdfReader  # Assurez-vous que PyPDF2 est installé : `pip install PyPDF2`

# --- Gestion de la base de données ---
DB_NAME = "documents.db"

def init_db():
    """
    Initialise la base de données SQLite avec une table pour les documents.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            text TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(name, text):
    """
    Sauvegarde un document dans la base de données.
    :param name: Nom du fichier PDF.
    :param text: Texte extrait du PDF.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO documents (name, text) VALUES (?, ?)", (name, text))
        conn.commit()
        conn.close()
        print(f"Document '{name}' sauvegardé avec succès dans la base de données.")
    except sqlite3.Error as e:
        print(f"Erreur lors de la sauvegarde dans la base de données : {e}")
        raise e

def get_all_documents():
    """
    Récupère tous les documents enregistrés dans la base de données.
    :return: Liste des documents (id, name, text).
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM documents")
    documents = cursor.fetchall()
    conn.close()
    return documents

def import_pdf():
    """
    Permet à l'utilisateur de sélectionner un fichier PDF, extrait son texte et l'enregistre dans la base de données.
    """
    try:
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if not file_path:
            return  # L'utilisateur a annulé la sélection

        # Extraire le texte du fichier PDF
        text = extract_text_from_pdf(file_path)
        if not text.strip():
            messagebox.showinfo("Information", "Le fichier PDF est vide ou non lisible.")
            return

        # Extraire le nom du fichier
        file_name = os.path.basename(file_path)

        # Sauvegarder dans la base de données
        save_to_db(file_name, text)
        messagebox.showinfo("Succès", f"Le fichier '{file_name}' a été importé et sauvegardé.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue lors de l'importation du PDF :\n{e}")

def extract_text_from_pdf(file_path):
    """
    Extrait le texte d'un fichier PDF.
    :param file_path: Chemin du fichier PDF.
    :return: Texte extrait.
    """
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Erreur lors de l'extraction du texte du PDF : {e}")
        raise e

def show_documents():
    """
    Affiche la liste des documents enregistrés dans la base de données.
    """
    try:
        documents = get_all_documents()
        if not documents:
            messagebox.showinfo("Information", "Aucun document enregistré.")
            return

        # Affichage des documents dans la console (ou une autre interface selon le besoin)
        print("Documents enregistrés :")
        for doc in documents:
            print(f"ID : {doc[0]}, Nom : {doc[1]}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la récupération des documents : {e}")

# --- Exemple d'utilisation ---
if __name__ == "__main__":
    import tkinter as tk

    # Initialisation de la base de données
    init_db()

    # Interface simple pour tester les fonctionnalités
    def run_ui():
        root = tk.Tk()
        root.title("Gestion des Documents PDF")
        root.geometry("400x300")

        # Bouton pour importer un PDF
        import_button = tk.Button(root, text="Importer un PDF", command=import_pdf, width=30)
        import_button.pack(pady=10)

        # Bouton pour afficher tous les documents
        show_button = tk.Button(root, text="Afficher les Documents", command=show_documents, width=30)
        show_button.pack(pady=10)

        # Bouton pour quitter
        quit_button = tk.Button(root, text="Quitter", command=root.quit, width=30)
        quit_button.pack(pady=10)

        root.mainloop()

    run_ui()
