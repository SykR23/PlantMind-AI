from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    APP_TITLE = "PlantMind AI"
    APP_DESCRIPTION = (
        "Enterprise RAG Copilot for Process Industries"
    )
    APP_ICON = "🌿"

    ROOT_DIR = Path(__file__).resolve().parent.parent
    KNOWLEDGE_BASE_ROOT = ROOT_DIR / "knowledge_bases"
    DEFAULT_KB = "heat_exchangers"

    LOG_DIR = ROOT_DIR / "logs"
    LOG_FILE = LOG_DIR / "plantmind.log"

    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")
    DEVICE = os.getenv("DEVICE", "cpu")
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
    LLM_MODEL = os.getenv("LLM_MODEL", "qwen2.5:3b")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    SEARCH_TYPE = os.getenv("SEARCH_TYPE", "similarity")
    TOP_K = int(os.getenv("TOP_K", "3"))
    FETCH_K = int(os.getenv("FETCH_K", "10"))

    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "500"))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "100"))

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