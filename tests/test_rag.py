from pathlib import Path

from retrieval.faiss_manager import FAISSManager
from retrieval.retriever import PlantRetriever

from llm.model import PlantMindLLM
from llm.prompt_builder import PromptBuilder

from chains.rag_chain import PlantMindRAG

from utils.formatter import SourceFormatter

# -------------------------------------------------------
# Resolve Project Root
# -------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

FAISS_PATH = (
    PROJECT_ROOT
    / "knowledge_bases"
    / "heat_exchangers"
    / "faiss"
)

# -------------------------------------------------------
# Load Vector Store
# -------------------------------------------------------

faiss = FAISSManager()

faiss.load_vector_store(FAISS_PATH)

# -------------------------------------------------------
# Initialize Components
# -------------------------------------------------------

retriever = PlantRetriever(faiss)

llm = PlantMindLLM()

prompt_builder = PromptBuilder()

rag = PlantMindRAG(
    retriever=retriever,
    llm=llm,
    prompt_builder=prompt_builder,
)

# -------------------------------------------------------
# Ask Question
# -------------------------------------------------------

query = "How should a plate heat exchanger be cleaned?"

response = rag.run(query)

# -------------------------------------------------------
# Display Answer
# -------------------------------------------------------

print("\n")
print("=" * 100)
print("ANSWER")
print("=" * 100)

print(response["answer"])

print("\n")
print("=" * 100)
print("SOURCES")
print("=" * 100)

print(
    SourceFormatter.format_sources(
        response["documents"]
    )
)