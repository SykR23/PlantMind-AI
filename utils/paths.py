from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CONFIG = PROJECT_ROOT / "config"

KNOWLEDGE_BASES = PROJECT_ROOT / "knowledge_bases"

LOGS = PROJECT_ROOT / "logs"

TESTS = PROJECT_ROOT / "tests"

UI = PROJECT_ROOT / "ui"

DATA = PROJECT_ROOT / "data"

DEFAULT_KB = "heat_exchangers"


def get_kb_path(kb_name: str) -> Path:
    """
    Returns the path to a knowledge base.
    """

    return KNOWLEDGE_BASES / kb_name


def get_raw_path(kb_name: str) -> Path:
    """
    Returns the raw PDF directory.
    """

    return get_kb_path(kb_name) / "raw"


def get_faiss_path(kb_name: str) -> Path:
    """
    Returns the FAISS directory.
    """

    return get_kb_path(kb_name) / "faiss"


def get_pdf_path(
    kb_name: str,
    filename: str,
) -> Path:
    """
    Returns the full path to a PDF.
    """

    return get_raw_path(kb_name) / filename