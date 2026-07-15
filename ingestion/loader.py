from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class PDFLoader:
    """
        Loads PDF documents into LangChain Document objects.
        """
    def __init__(self):
        pass

    def load_pdf(
            self,
            pdf_path: Path,
    ) -> list[Document]:
        loader = PyPDFLoader(
            str(pdf_path)
        )
        documents = loader.load()
        return documents