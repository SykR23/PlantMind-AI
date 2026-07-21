from config.config import config

from retrieval.faiss_manager import FAISSManager
from retrieval.retriever import PlantRetriever

from llm.model import PlantMindLLM
from llm.prompt_builder import PromptBuilder

from chains.rag_chain import PlantMindRAG



def build_rag(kb_name: str):
    faiss = FAISSManager()

    faiss.load_vector_store(config.get_faiss_path(kb_name))

    retriever = PlantRetriever(faiss)

    llm = PlantMindLLM()

    builder = PromptBuilder()

    return PlantMindRAG(
        retriever,
        llm,
        builder
    )
