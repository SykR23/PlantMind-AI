import os

from fastapi import HTTPException

from config.config import config
from knowledge_manager.manager import KnowledgeBaseManager

from utils.logger import logger

manager = KnowledgeBaseManager()


def validate_knowledge_base(knowledge_base: str):
    if knowledge_base not in manager.list_knowledge_bases():
        raise HTTPException(
            status_code=404,
            detail=f"Knowledge base '{knowledge_base}' not found."
        )


def validate_query(query: str):

    if not query.strip():
        logger.warning("Received an empty query")
        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty"
        )


def validate_vector_store(knowledge_base: str):

    faiss_path = config.get_faiss_path(knowledge_base)

    if not os.path.exists(faiss_path):
        raise HTTPException(
            status_code=404,
            detail=f"Knowledge base '{knowledge_base}' has not been ingested yet."
        )


def validate_raw_folder(knowledge_base: str):

    raw_path = config.get_raw_document_path(knowledge_base)

    if not os.path.exists(raw_path):
        raise HTTPException(
            status_code=404,
            detail=f"Raw document folder for '{knowledge_base}' not found."
        )


def validate_pdf_files(knowledge_base: str):

    raw_path = config.get_raw_document_path(knowledge_base)

    pdf_files = [
        file for file in os.listdir(raw_path)
        if file.lower().endswith(".pdf")
    ]

    if not pdf_files:
        raise HTTPException(
            status_code=400,
            detail=f"No PDF files found in '{knowledge_base}'."
        )