from pydantic import BaseModel


class ChatRequest(BaseModel):
    query: str
    knowledge_base: str


class Source(BaseModel):
    source: str
    page: int | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]