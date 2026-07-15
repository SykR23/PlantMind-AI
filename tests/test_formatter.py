from utils.formatter import SourceFormatter
from pathlib import Path

from ingestion.loader import PDFLoader

from ingestion.cleaner import DocumentCleaner

from ingestion.metadata import MetadataManager

from ingestion.splitter import DocumentSplitter

from retrieval.faiss_manager import FAISSManager

PROJECT_ROOT = Path(__file__).resolve().parent.parent

pdf = (
    PROJECT_ROOT
    / "knowledge_bases"
    / "heat_exchangers"
    / "raw"
    / "EN_Manual.pdf"
)
loader = PDFLoader()

cleaner = DocumentCleaner()

metadata = MetadataManager()

documents = loader.load_pdf(pdf)

documents = cleaner.clean(documents)

splitter = DocumentSplitter()
documents = splitter.split(documents)

documents = metadata.enrich(
    documents,
    pdf,
    "heat_exchangers"
)

save_path = Path(
    PROJECT_ROOT/"knowledge_bases"/"heat_exchangers"/"faiss"
)

faiss_manager = FAISSManager()

faiss_manager.load_vector_store(save_path)

results = faiss_manager.similarity_search(
    query="plate",
    k=3,
)

print(
    SourceFormatter.format_sources(
        documents
    )
)