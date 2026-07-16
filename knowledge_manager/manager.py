from pathlib import Path

from config.config import config


class KnowledgeBaseManager:

    def __init__(self):
        self.root = config.KNOWLEDGE_BASE_ROOT

    def list_knowledge_bases(self) -> list[str]:

        knowledge_bases = []

        for folder in sorted(self.root.iterdir()):
            if not folder.is_dir():
                continue

            if (folder / "raw").exists():
                knowledge_bases.append(folder.name)

        return knowledge_bases

    def get_metadata(self, knowledge_base: str):
        kb = self.root / knowledge_base

        raw = kb / "raw"
        faiss = kb / "faiss"

        pdfs = list(raw.glob("*.pdf"))

        return {
            "name": knowledge_base,
            "pdf_count": len(pdfs),
            "has_faiss": (
                (faiss / "index.faiss").exists()
                and
                (faiss / "index.pkl").exists()
            ),
            "raw_path": raw,
            "faiss_path": faiss
        }