import streamlit as st

from utils.formatter import SourceFormatter


class ChatUI:

    @staticmethod
    def display_history():

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if message["role"] == "assistant":
                    if message.get("documents"):
                        with st.expander("Sources"):
                            st.text(
                                SourceFormatter.format_sources(
                                    message["documents"]
                                )
                            )

    @staticmethod
    def display_sources(documents):
        with st.expander("Sources"):
            for i, document in enumerate(documents, start=1):
                meta = document.metadata
                st.markdown(
                    f"""
                ### 📄 Source {i}

                **Document:** `{meta.get("document_name", "Unknown")}`

                **Knowledge Base:** `{meta.get("knowledge_base", "Unknown")}`

                **Page:** `{meta.get("page", 0)+ 1}`

                **Chunk ID:** `{meta.get("chunk_id", "Unknown")}`
                """
                )

                st.divider()