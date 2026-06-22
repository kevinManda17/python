from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from .faiss_utils import load_faiss_index
import os 


# Charger l'index FAISS
vectorstore = load_faiss_index()

# Configurer LangChain avec OpenAI
llm = OpenAI(model="text-davinci-003", openai_api_key=os.getenv("OPENAI_API_KEY"))
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

class AskQuestionView(APIView):
    def post(self, request):
        question = request.data.get("question", "")
        if not question:
            return Response({"error": "Aucune question fournie."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            response = qa_chain.run(question)
            return Response({"response": response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
