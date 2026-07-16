from pathlib import Path


class Config:

    ROOT_DIR = Path(__file__).resolve().parent.parent

    DEFAULT_KB = "heat_exchangers"

    KNOWLEDGE_BASE_ROOT = ROOT_DIR / "knowledge_bases"

    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 100

    EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
    DEVICE = "cpu"

    SEARCH_TYPE = "similarity"
    TOP_K = 3
    FETCH_K = 10

    LLM_MODEL = "qwen2.5:3b"
    TEMPERATURE = 0.2

    NO_CONTEXT_RESPONSE = (
        "I couldn't find enough information in the supplied documents."
    )

    SYSTEM_PROMPT = """
You are PlantMind AI.

You are an expert Chemical and Mechanical Engineering assistant.

Use ONLY the supplied context.

Do NOT use outside knowledge.

If the supplied context does not contain enough information,
reply EXACTLY:

"I couldn't find enough information in the supplied documents."

If multiple context chunks contribute to the answer,
combine them naturally into one response.

For procedures or instructions,
present the answer as numbered steps.

Keep the answer concise, technically accurate and professional.
"""

    APP_TITLE = "PlantMind AI"

    APP_DESCRIPTION = (
        "Enterprise RAG Copilot for Process Industries"
    )

    APP_ICON = "🌿"

    LOG_DIR = ROOT_DIR / "logs"
    LOG_FILE = LOG_DIR / "plantmind.log"

    @classmethod
    def get_kb_path(cls, kb_name: str) -> Path:
        return cls.KNOWLEDGE_BASE_ROOT / kb_name

    @classmethod
    def get_raw_document_path(cls, kb_name: str) -> Path:
        return (
            cls.KNOWLEDGE_BASE_ROOT
            / kb_name
            / "raw"
        )

    @classmethod
    def get_faiss_path(cls, kb_name: str) -> Path:
        return (
            cls.KNOWLEDGE_BASE_ROOT
            / kb_name
            / "faiss"
        )

    @classmethod
    def get_pdf_path(
        cls,
        kb_name: str,
        filename: str,
    ) -> Path:
        return (
            cls.get_raw_document_path(kb_name)
            / filename
        )


config = Config()