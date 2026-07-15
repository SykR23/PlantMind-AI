from pathlib import Path

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from ingestion.embedder import DocumentEmbedder

from config.config import config


class FAISSManager:
    """
        Builds, saves, loads and queries the FAISS vector store.
        """
    def __init__(self):
        self.embedder = DocumentEmbedder()
        self.vector_store = None

    def build_vector_store(self, documents: list[Document]):
        self.vector_store = FAISS.from_documents(
            documents,
            self.embedder.embedding_model,
        )
        return self.vector_store

    def save_vector_store(self, save_path=True):
        self.vector_store.save_local(str(save_path))

    def load_vector_store(self, load_path=Path,):
        self.vector_store = FAISS.load_local(
            str(load_path),
            self.embedder.embedding_model,
            allow_dangerous_deserialization=True,
        )
        return self.vector_store

    def similarity_search(self, query: str, k: int):
        return self.vector_store.similarity_search(query, k=k)

    def similarity_search_with_score(self, query: str, k: int):
        return self.vector_store.similarity_search_with_score(query, k=k)

    def mmr_search(self, query: str):
        return self.vector_store.max_marginal_relevance_search(
            query=query,
            k=config.TOP_K,
            fetch_k=config.FETCH_K
        )