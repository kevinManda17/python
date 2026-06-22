from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from config.settings import settings


class VectorStoreManager:
    def __init__(self, persist_dir: str | None = None):
        self.persist_dir = str(persist_dir or settings.VECTOR_STORE_DIR)
        Path(self.persist_dir).mkdir(parents=True, exist_ok=True)

        self.embeddings = SentenceTransformer(settings.EMBEDDING_MODEL)
        self.client = chromadb.PersistentClient(path=self.persist_dir)
        self.collection_name = "pdf_documents"
        self.collection = self.client.get_or_create_collection(self.collection_name)

    def create_from_text(self, text: str):
        text = (text or "").strip()
        if not text:
            return None

        self.clear_collection()
        chunks = self._split_text(text)
        embeddings = self.embeddings.encode(chunks).tolist()

        self.collection.upsert(
            embeddings=embeddings,
            documents=chunks,
            ids=[f"chunk_{i}" for i in range(len(chunks))],
        )
        return self.collection

    def clear_collection(self):
        try:
            self.client.delete_collection(self.collection_name)
        except Exception:
            pass
        self.collection = self.client.get_or_create_collection(self.collection_name)

    def query(self, question: str, n_results: int | None = None):
        if self.collection is None:
            return {"documents": []}

        question_embedding = self.embeddings.encode([question]).tolist()
        return self.collection.query(
            query_embeddings=question_embedding,
            n_results=n_results or settings.RETRIEVAL_TOP_K,
        )

    def _split_text(self, text: str) -> list[str]:
        chunk_size = max(200, settings.CHUNK_SIZE)
        overlap = min(settings.CHUNK_OVERLAP, chunk_size - 1)
        step = chunk_size - overlap

        chunks = []
        for start in range(0, len(text), step):
            chunk = text[start : start + chunk_size].strip()
            if chunk:
                chunks.append(chunk)
        return chunks
