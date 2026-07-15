from pathlib import Path

from retrieval.faiss_manager import FAISSManager
from retrieval.retriever import PlantRetriever

from config.config import config

save_path = config.FAISS_DIRS["heat_exchangers"]
faiss = FAISSManager()

faiss.load_vector_store(save_path)


retriever = PlantRetriever(faiss)


results = retriever.retrieve(

    "plate heat exchanger maintenance"

)


for i, document in enumerate(results):

    print("=" * 80)

    print(f"Result {i+1}")

    print(document.metadata)

    print()

    print(document.page_content)