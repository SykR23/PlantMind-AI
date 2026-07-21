from langchain_core.documents import Document

from langchain_huggingface import HuggingFaceEmbeddings

from config.config import config


class DocumentEmbedder:
    """
        Generates vector embeddings using BGE Small.
        """
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL,
                                                     model_kwargs={"device": config.DEVICE, },
                                                     encode_kwargs={"normalize_embeddings": True, },)

    def embed_documents(self,
                        documents: list[Document],
                        ) -> list[list[float]]:
        texts = [
            document.page_content
            for document in documents
        ]
        embeddings = self.embedding_model.embed_documents(
            texts
        )
        return embeddings

    def embed_query(self, query: str,) -> list[float]:
        embedding = self.embedding_model.embed_query(
            query
        )
        return embedding