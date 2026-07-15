from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.config import config


class DocumentSplitter:
    """
        Splits documents into overlapping chunks.
        """
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP,
        )

    def split(
            self,
            documents: list[Document],
    ) -> list[Document]:
        chunks = self.splitter.split_documents(documents)
        return chunks