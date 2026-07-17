from retrieval.faiss_manager import FAISSManager
from retrieval.retriever import PlantRetriever

from llm.model import PlantMindLLM
from llm.prompt_builder import PromptBuilder

from chains.rag_chain import PlantMindRAG

from config.config import config
from utils.logger import logger


class DependencyContainer:

    def __init__(self):

        self.llm = PlantMindLLM()
        self.prompt_builder = PromptBuilder()
        self.retrievers = {}

    def get_rag(self, knowledge_base: str):

        if knowledge_base not in self.retrievers:

            logger.info(
                f"Loading retriever for knowledge base '{knowledge_base}'."
            )

            faiss = FAISSManager()

            faiss.load_vector_store(
                config.get_faiss_path(knowledge_base)
            )

            self.retrievers[knowledge_base] = PlantRetriever(faiss)

        else:
            logger.info(
                f"Using cached retriever for knowledge base '{knowledge_base}'."
            )

        retriever = self.retrievers[knowledge_base]

        return PlantMindRAG(
            retriever,
            self.llm,
            self.prompt_builder
        )

    def clear_retriever(self, knowledge_base: str):
        self.retrievers.pop(knowledge_base, None)


container = DependencyContainer()