from pathlib import Path

from retrieval.faiss_manager import FAISSManager
from retrieval.retriever import PlantRetriever
from llm.prompt_builder import PromptBuilder

# ---------------------------------------------------
# Resolve project root
# ---------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

faiss_path = (
    PROJECT_ROOT
    / "knowledge_bases"
    / "heat_exchangers"
    / "faiss"
)

# ---------------------------------------------------
# Load Vector Store
# ---------------------------------------------------

faiss = FAISSManager()

faiss.load_vector_store(faiss_path)

# ---------------------------------------------------
# Retrieve Relevant Documents
# ---------------------------------------------------

retriever = PlantRetriever(faiss)

query = "How should a plate heat exchanger be cleaned?"

documents = retriever.retrieve(query)

# ---------------------------------------------------
# Build Prompt
# ---------------------------------------------------

builder = PromptBuilder()

prompt = builder.build_prompt(
    query=query,
    documents=documents,
)

# ---------------------------------------------------
# Display Prompt
# ---------------------------------------------------

print("=" * 100)
print(prompt)
print("=" * 100)