# app.py

from pathlib import Path

from ingestion.loader import PDFLoader

from ingestion.cleaner import DocumentCleaner

from ingestion.metadata import MetadataManager

from ingestion.splitter import DocumentSplitter

from retrieval.faiss_manager import FAISSManager

pdf = Path(
    "knowledge_bases/heat_exchangers/raw/EN_Manual.pdf"
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
    "knowledge_bases/heat_exchangers/faiss"
)

faiss_manager = FAISSManager()

faiss_manager.load_vector_store(save_path)

results = faiss_manager.similarity_search(
    query="plate",
    k=3,
)

for i, document in enumerate(results):

    print(f"\nResult {i+1}")

    print(document.metadata)

    print()

    print(document.page_content)

    print("=" * 100)