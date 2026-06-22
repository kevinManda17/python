import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from app.pdf_processor import extract_text_from_pdf
from app.database import save_to_db, get_all_documents
from app.embeddings import create_embeddings
from app.chatbot import create_chatbot, ask_question


def run_ui():
    # --- Initialisation globale ---
    vector_store = None
    chatbot = None

    # --- Actions des boutons ---
    def upload_pdf():
        try:
            file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
            if file_path:
                text = extract_text_from_pdf(file_path)
                save_to_db(file_path.split('/')[-1], text)
                status_label.config(text="PDF chargé et sauvegardé avec succès !", foreground="green")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement du PDF :\n{e}")

    def initialize_chatbot():
        try:
            documents = get_all_documents()
            if not documents:
                messagebox.showinfo("Information", "Aucun document dans la base de données. Chargez un PDF d'abord.")
                return

            texts = [doc[2] for doc in documents]
            nonlocal vector_store
            vector_store = create_embeddings(texts)
            nonlocal chatbot
            chatbot = create_chatbot(vector_store)
            status_label.config(text="Chatbot initialisé avec succès !", foreground="green")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'initialisation du chatbot :\n{e}")

    def ask_bot():
        try:
            question = question_entry.get()
            if not question.strip():
                messagebox.showinfo("Information", "Veuillez saisir une question.")
                return

            if chatbot:
                answer = ask_question(chatbot, question)
                output_text.delete("1.0", tk.END)
                output_text.insert(tk.END, answer)
                status_label.config(text="Réponse générée avec succès !", foreground="green")
            else:
                status_label.config(text="Le chatbot n'est pas encore initialisé.", foreground="red")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la génération de la réponse :\n{e}")

    def show_documents():
        try:
            documents = get_all_documents()
            if not documents:
                messagebox.showinfo("Information", "Aucun document disponible dans la base de données.")
                return

            # Affiche une nouvelle fenêtre avec la liste des documents
            doc_window = tk.Toplevel(root)
            doc_window.title("Documents enregistrés")
            doc_window.geometry("500x400")
            doc_window.resizable(False, False)

            listbox = tk.Listbox(doc_window, font=("Arial", 12), width=70, height=20)
            listbox.pack(pady=10, padx=10)
            for doc in documents:
                listbox.insert(tk.END, f"ID : {doc[0]} | Nom : {doc[1]}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'affichage des documents :\n{e}")

    def clear_texts():
        question_entry.delete(0, tk.END)
        output_text.delete("1.0", tk.END)
        status_label.config(text="Champs nettoyés.")

    # --- Interface principale ---
    root = tk.Tk()
    root.title("Chatbot PDF - Menu Latéral")
    root.geometry("800x600")

    # Menu latéral
    side_menu = tk.Frame(root, bg="#2c3e50", width=200, height=600)
    side_menu.pack(side="left", fill="y")

    side_menu_title = tk.Label(
        side_menu, text="Navigation", bg="#2c3e50", fg="white", font=("Arial", 16, "bold")
    )
    side_menu_title.pack(pady=20)

    menu_buttons = [
        ("Charger un PDF", upload_pdf),
        ("Initialiser le Chatbot", initialize_chatbot),
        ("Afficher les Documents", show_documents),
        ("Quitter", root.quit),
    ]

    for label, command in menu_buttons:
        btn = tk.Button(
            side_menu,
            text=label,
            command=command,
            bg="#34495e",
            fg="white",
            font=("Arial", 12),
            relief="flat",
            cursor="hand2",
            width=18,
        )
        btn.pack(pady=10)

    # Section principale
    main_frame = tk.Frame(root, bg="white", padx=20, pady=20)
    main_frame.pack(side="right", fill="both", expand=True)

    # Titre principal
    title_label = tk.Label(main_frame, text="LexIA ", font=("Arial", 20, "bold"), bg="white")
    title_label.pack()

    # Section pour poser une question
    question_frame = tk.Frame(main_frame, bg="white", pady=10)
    question_frame.pack(fill="x")

    question_label = tk.Label(question_frame, text="Posez une question :", font=("Arial", 14), bg="white")
    question_label.pack(anchor="w")

    question_entry = ttk.Entry(question_frame, width=70)
    question_entry.pack(pady=5)

    ask_button = ttk.Button(question_frame, text="Poser la Question", command=ask_bot)
    ask_button.pack(pady=5, side="left")

    clear_button = ttk.Button(question_frame, text="Nettoyer les Champs", command=clear_texts)
    clear_button.pack(pady=5, side="left", padx=10)

    # Section pour afficher la réponse
    output_frame = tk.Frame(main_frame, bg="white", pady=10)
    output_frame.pack(fill="both", expand=True)

    output_label = tk.Label(output_frame, text="Réponse générée :", font=("Arial", 14), bg="white")
    output_label.pack(anchor="w")

    output_text = tk.Text(output_frame, wrap="word", font=("Arial", 12), height=10)
    output_text.pack(fill="both", expand=True, padx=10, pady=5)

    # Barre d'état
    status_label = tk.Label(root, text="", font=("Arial", 10), fg="blue", bg="#ecf0f1", anchor="w")
    status_label.pack(side="bottom", fill="x")

    # Lancer la boucle principale
    root.mainloop()
