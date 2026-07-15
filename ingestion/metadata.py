from pathlib import Path

from langchain_core.documents import Document


class MetadataManager:
    def enrich(self, documents: list[Document], pdf_path: Path,
               knowledge_base: str,) -> list[Document]:
        page_counter = {}

        for document in documents:
            page = document.metadata.get("page", 0)
            page_counter.setdefault(page, 0)

            chunk_number = page_counter[page]
            chunk_id = (
                f"{pdf_path.stem}"
                f"_p{page + 1}"
                f"_c{chunk_number}"
            )
            document.metadata.update(
                {
                    "document_name": pdf_path.name,
                    "knowledge_base": knowledge_base,
                    "chunk_id": chunk_id,
                    "relative_path": str(pdf_path),
                }
            )
            page_counter[page] += 1

        return documents