import gradio as gr
from model import setup_qa_system

def process_pdf_and_answer(question, pdf_file):
    # Sauvegarder le PDF uploadé
    pdf_path = f"data/uploaded.pdf"
    with open(pdf_path, "wb") as f:
        f.write(pdf_file.read())
    
    # Initialiser le système QA
    qa_system = setup_qa_system(pdf_path)
    
    # Obtenir la réponse
    response = qa_system.run(question)
    return response

# Interface Gradio
interface = gr.Interface(
    fn=process_pdf_and_answer,
    inputs=[
        gr.Textbox(label="Votre question"),
        gr.File(label="Uploader un PDF", type="binary")
    ],
    outputs=gr.Textbox(label="Réponse de l'IA"),
    title="🦜 IA Générative pour PDF"
)

if __name__ == "__main__":
    interface.launch(server_port=7860, share=True)