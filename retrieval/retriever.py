from retrieval.faiss_manager import FAISSManager


class PlantRetriever:
    def __init__(self, faiss_manager: FAISSManager):
        self.faiss_manager = faiss_manager

    def retrieve(self, query: str):
        return self.faiss_manager.mmr_search(query=query)

