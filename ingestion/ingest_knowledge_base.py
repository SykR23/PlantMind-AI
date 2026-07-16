from config.config import config

from ingestion.loader import PDFLoader
from ingestion.metadata import MetadataManager
from ingestion.splitter import RecursiveCharacterTextSplitter

from retrieval.faiss_manager import FAISSManager


class IngestionPipeline:

    def __init__(self):
        self.loader = PDFLoader()
        self.metadata = MetadataManager()
        self.splitter = RecursiveCharacterTextSplitter()
        self.faiss = FAISSManager()

    def ingest(self, knowledge_base: str):

        raw_dir = config.get_raw_document_path(knowledge_base)
        faiss_dir = config.get_faiss_path(knowledge_base)

        documents = []

        # Process each PDF individually
        for pdf_path in sorted(raw_dir.glob("*.pdf")):

            print(f"Loading: {pdf_path.name}")

            pdf_documents = self.loader.load_pdf(pdf_path)

            pdf_documents = self.metadata.enrich(
                documents=pdf_documents,
                pdf_path=pdf_path,
                knowledge_base=knowledge_base,
            )

            documents.extend(pdf_documents)

        chunks = self.splitter.split_documents(documents)

        self.faiss.build_vector_store(chunks)

        self.faiss.save_vector_store(faiss_dir)

        print("\nKnowledge Base Ready!")