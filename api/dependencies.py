from rag.build import build_rag

RAG_CACHE = {}


def get_rag(knowledge_base: str):

    if knowledge_base not in RAG_CACHE:
        RAG_CACHE[knowledge_base] = build_rag(knowledge_base)

    return RAG_CACHE[knowledge_base]


def clear_rag(knowledge_base: str):
    RAG_CACHE.pop(knowledge_base, None)


def clear_all():
    RAG_CACHE.clear()