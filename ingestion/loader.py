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

        knowledge_base = pdf_path.parent.parent.name

        relative_path = (Path("knowledge_bases") / knowledge_base / "raw" / pdf_path.name)

        for document in documents:
            document.metadata["document_name"] = pdf_path.name
            document.metadata["knowledge_base"] = knowledge_base
            document.metadata["relative_path"] = str(relative_path)

        return documents

    def load_directory(self, directory: Path) -> list[Document]:
        documents = []
        pdf_files = sorted(directory.glob("*.pdf"))

        if len(pdf_files) == 0:
            raise FileNotFoundError(
                f"No PDF files found in {directory}"
            )

        for pdf in pdf_files:
            print(f"Loading: {pdf.name}")

            documents.extend(self.load_pdf(pdf))

        return documents