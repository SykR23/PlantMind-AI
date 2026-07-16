import streamlit as st
from config.config import config
from knowledge_manager.manager import KnowledgeBaseManager


class Sidebar:

    @staticmethod
    def render():
        with st.sidebar:
            st.title("🌿 PlantMind AI")
            st.sidebar.caption("RAG Copilot")
            st.sidebar.divider()

            manager = KnowledgeBaseManager()

            metadata = [
                manager.get_metadata(kb) for kb in manager.list_knowledge_bases()
            ]

            options = {
                f"{m['name']} ({m['pdf_count']} PDFs)": m['name']
                for m in metadata
            }

            selected = st.sidebar.selectbox(
                "Knowledge Base",
                list(options.keys())
            )

            knowledge_base = options[selected]

            st.sidebar.divider()

            st.sidebar.markdown("### Model")

            st.sidebar.info(config.LLM_MODEL)

            st.sidebar.markdown("### Retrieval")

            st.sidebar.write(f"Search : {config.SEARCH_TYPE}")

            st.sidebar.write(f"Top K : {config.TOP_K}")

            st.sidebar.divider()

            st.sidebar.markdown("### About")

            st.sidebar.caption(
                "Built with LangChain, FAISS, Ollama and Streamlit."
            )

            st.sidebar.caption("Version 1.0")
            return knowledge_base