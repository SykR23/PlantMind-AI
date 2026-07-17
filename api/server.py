from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="PlantMind API",
    description="""
    A modular Retrieval-Augmented Generation (RAG) backend for engineering knowledge bases.

Features:
- Multi knowledge base support
- Local Ollama LLM inference
- FAISS vector retrieval
- Dynamic PDF ingestion
- REST API for chat and ingestion
    """,
    version="1.0.0"
)

app.include_router(router)
