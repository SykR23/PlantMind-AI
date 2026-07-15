from pathlib import Path


class Config:

    ROOT_DIR = Path(__file__).resolve().parent.parent

    DEFAULT_KB = "heat_exchangers"

    KNOWLEDGE_BASES = {
        "heat_exchangers": ROOT_DIR / "knowledge_bases" / "heat_exchangers",
        "pumps": ROOT_DIR / "knowledge_bases" / "pumps",
        "process_control": ROOT_DIR / "knowledge_bases" / "process_control",
        "safety": ROOT_DIR / "knowledge_bases" / "safety",
    }

    FAISS_DIRS = {
        name: path / "faiss"
        for name, path in KNOWLEDGE_BASES.items()
    }

    RAW_DOCUMENT_DIRS = {
        name: path / "raw"
        for name, path in KNOWLEDGE_BASES.items()
    }
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 100

    EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
    DEVICE = "cpu"

    SEARCH_TYPE = "mmr"
    TOP_K = 5
    FETCH_K = 10

    LLM_MODEL = "qwen2.5:3b"
    TEMPERATURE = 0.2
    NO_CONTEXT_RESPONSE = (
        "I couldn't find enough information in the supplied documents."
    )

    APP_TITLE = "PlantMind AI"
    APP_DESCRIPTION = (
        "Enterprise RAG Copilot for Process Industries"
    )
    APP_ICON = "🌿"

    LOG_DIR = ROOT_DIR / "logs"
    LOG_FILE = LOG_DIR / "plantmind.log"

    SYSTEM_PROMPT = """
You are PlantMind AI.

You are an expert Chemical and Mechanical Engineering assistant.

Use ONLY the supplied context.

Do NOT use outside knowledge.

If the context is insufficient, reply exactly:

"I couldn't find enough information in the supplied documents."

When explaining procedures:

- Use numbered steps.
- Be concise.
- Use technical terminology.
- Merge information from multiple context chunks naturally.
"""


config = Config()