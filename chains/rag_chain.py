from retrieval.retriever import PlantRetriever

from llm.model import PlantMindLLM
from llm.prompt_builder import PromptBuilder

from utils.logger import PlantMindLogger
logger = PlantMindLogger.get_logger()


class PlantMindRAG:

    def __init__(self,retriever: PlantRetriever,
                 llm: PlantMindLLM, prompt_builder: PromptBuilder):
        self.retriever = retriever
        self.llm = llm
        self.prompt_builder = prompt_builder

    def run(
            self,
            query: str,
    ):

        logger.info("Starting RAG Pipeline...")

        try:

            documents = self.retriever.retrieve(query)

            logger.info(
                f"Retrieved {len(documents)} document(s)."
            )

            prompt = self.prompt_builder.build_prompt(
                query=query,
                documents=documents,
            )

            answer = self.llm.generate(prompt)

            logger.info("Answer generated successfully.")

            return {

                "query": query,

                "answer": answer,

                "documents": documents,

            }

        except Exception as e:

            logger.error(str(e))

            return {

                "query": query,

                "answer": f"Error: {e}",

                "documents": [],

            }