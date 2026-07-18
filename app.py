import streamlit as st

from config.config import config

from ui.sidebar import Sidebar
from ui.chat import ChatUI
from ui.session import SessionManager
from ui.styles import Styles
from ui.home import Home

from retrieval.faiss_manager import FAISSManager
from retrieval.retriever import PlantRetriever

from llm.model import PlantMindLLM
from llm.prompt_builder import PromptBuilder

from chains.rag_chain import PlantMindRAG


@st.cache_resource
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


# Page Configuration
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon=config.APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize UI
Styles.load()

SessionManager.initialize()

# Sidebar
knowledge_base = Sidebar.render()

# Build Backend
rag = build_rag(knowledge_base)

# Display Previous Messages
if len(st.session_state.messages) == 0:
    Home.render()
else:
    ChatUI.display_history()

# Chat Input
query = st.chat_input(
    "Ask a question.."
)
if query:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query,
        }
    )
    with st.chat_message("user"):
        st.markdown(query)

    with st.spinner("🌿 PlantMind is searching the knowledge base..."):
        response = rag.run(query=query, history=st.session_state.messages)

    print("\n" + "=" * 80)
    print("RAG RESPONSE")
    print("=" * 80)
    print(type(response))
    print(response)
    print(response.keys() if isinstance(response, dict) else "Not a dict")
    print("=" * 80)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response["answer"],
            "documents": response["documents"]
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response["answer"])
        ChatUI.display_sources(response["documents"])

    with st.container():
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Knowledge Base",
            knowledge_base.replace("_", " ").title()
        )

        col2.metric(
            "Retrieved Docs",
            len(response["documents"])
        )

        col3.metric(
            "Model",
            config.LLM_MODEL
        )