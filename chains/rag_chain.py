from retrieval.retriever import PlantRetriever

from llm.model import PlantMindLLM
from llm.prompt_builder import PromptBuilder

from chains.query_rewriter import QueryRewriter

from utils.logger import PlantMindLogger
logger = PlantMindLogger.get_logger()


class PlantMindRAG:

    def __init__(self,retriever: PlantRetriever,
                 llm: PlantMindLLM, prompt_builder: PromptBuilder):
        self.retriever = retriever
        self.llm = llm
        self.prompt_builder = prompt_builder
        self.query_rewriter = QueryRewriter()

    def run(self, query: str, history: list[dict]):
        logger.info("=" * 60)
        logger.info("STARTING RAG PIPELINE")
        logger.info("=" * 60)\

        try:
            retrieval_query = self.query_rewriter.rewrite(
                query=query,
                history=history,
            )
            logger.info("QUERY REWRITING")
            logger.info(f"Original Query : {query}")
            logger.info(f"Retrieval Query: {retrieval_query}")

            print("\n")
            print("=" * 80)
            print("QUERY REWRITING")
            print("=" * 80)
            print(f"Original Query : {query}")

            print(f"Retrieval Query: {retrieval_query}")
            print("=" * 80)

            documents = self.retriever.retrieve(retrieval_query)

            logger.info(f"Retrieved {len(documents)} documents")

            print("\n")
            print("="*80)
            print("Retrieved Documents")
            print("="*80)

            for i, doc in enumerate(documents, start=1):

                print(f"\nDocument {i}")

                print(doc.metadata)

                print()

                print(doc.page_content[:500])

                print("\n" + "=" * 80)

            prompt = self.prompt_builder.build_prompt(
                query,
                documents,
                history
            )

            answer = self.llm.generate(prompt)

            logger.info("Answer generated successfully")
            logger.info("RAG pipeline completed successfully")

            return {
                "query": query,
                "retrieval_query": retrieval_query,
                "answer": answer,
                "documents": documents
            }

        except Exception:

            logger.exception("Error while executing pipeline")

            raise