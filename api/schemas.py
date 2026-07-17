from pydantic import BaseModel


class ChatRequest(BaseModel):
    query: str
    knowledge_base: str = "heat_exchangers"


class ChatResponse(BaseModel):
    answer: str
    sources: list[dict]


class IngestRequest(BaseModel):
    knowledge_base: str


class HealthResponse(BaseModel):
    status: str
    version: str


class KnowledgeBaseResponse(BaseModel):
    knowledge_base: list[str]


class IngestResponse(BaseModel):
    status: str
    knowledge_base: str
    message: str