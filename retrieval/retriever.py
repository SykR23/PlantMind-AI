from retrieval.faiss_manager import FAISSManager
from  config.config import config

class PlantRetriever:
    def __init__(self, faiss_manager: FAISSManager):
        self.faiss_manager = faiss_manager

    def retrieve(self, query: str):
        if config.SEARCH_TYPE == "similarity":
            return self.faiss_manager.similarity_search(
                query=query,
                k=config.TOP_K
            )
        elif config.SEARCH_TYPE == "mmr":
            return self.faiss_manager.mmr_search(query=query)

        raise ValueError(
            f"Unknown search type: {config.SEARCH_TYPE}"
        )