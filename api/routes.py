from fastapi import APIRouter, HTTPException

from api.schemas import ChatRequest, ChatResponse, IngestRequest, IngestResponse, HealthResponse, KnowledgeBaseResponse

from utils.logger import logger

from api.dependencies import container

from api.validators import (validate_knowledge_base,
                            validate_query,
                            validate_vector_store,
                            validate_raw_folder,
                            validate_pdf_files)

from knowledge_manager.manager import KnowledgeBaseManager

from ingestion.ingest_knowledge_base import IngestionPipeline

router = APIRouter()

manager = KnowledgeBaseManager()

pipeline = IngestionPipeline()


# Health Route
@router.get("/health", response_model=HealthResponse,
            tags=["System"],
            summary="Health Check",
            description="Returns the current health status and API version.")
def health():

    return HealthResponse(status="ok", version="1.0.0")


# Knowledge Base Route
@router.get("/knowledge_bases",
            response_model=KnowledgeBaseResponse,
            tags=["Knowledge Bases"],
            summary="List Knowledge Bases",
            description="Returns all available knowledge bases discovered by PlantMind")
def knowledge_bases():
    return KnowledgeBaseResponse(
        knowledge_bases=manager.list_knowledge_bases()
    )


# Chat Route
@router.post(
    "/chat",
    response_model=ChatResponse,
    tags=["Chat"],
    summary="Ask a Question",
    description="Retrieves relevant documents from the selected knowledge base and generates an answer using the PlantMind RAG pipeline."
)
def chat(request: ChatRequest):
    validate_knowledge_base(request.knowledge_base)
    validate_query(request.query)
    validate_vector_store(request.knowledge_base)
    try:
        rag = container.get_rag(request.knowledge_base)
        response = rag.run(
            query=request.query,
            history=[]
        )

        sources = []

        for doc in response["documents"]:
            meta = doc.metadata

            sources.append(
                {
                    "document": meta.get("document_name"),
                    "page": meta.get("page"),
                    "chunk_id": meta.get("chunk_id")
                }
            )

        return ChatResponse(
            answer=response["answer"],
            sources=sources
        )

    except Exception as e:

        logger.exception("Error while processing chat requests")

        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while processing the request."
        )


@router.post("/ingest",
             response_model=IngestResponse,
             tags=["Knowledge Bases"],
             summary="Ingest Knowledge Base",
             description="Processes all PDFs inside a knowledge base, generates embeddings, and creates or updates the FAISS index."
             )
def ingest(request: IngestRequest):
    logger.info(
        f"Starting ingestion for '{request.knowledge_base}'."
    )

    validate_knowledge_base(request.knowledge_base)
    validate_raw_folder(request.knowledge_base)
    validate_pdf_files(request.knowledge_base)

    try:
        pipeline.ingest(request.knowledge_base)

        container.clear_retriever(request.knowledge_base)

        return IngestResponse(
            status="success",
            knowledge_base=request.knowledge_base,
            message="Knowledge base ingested successfully."
        )

    except Exception as e:

        logger.exception("Knowledge base ingestion failed.")

        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while ingesting the knowledge base."
        )