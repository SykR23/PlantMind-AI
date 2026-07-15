from langchain_core.documents import Document
from config.config import config


class PromptBuilder:
    """
    Builds grounded prompts for PlantMind.
    """
    def build_prompt(
            self,
            query: str,
            documents: list[Document],
    ) -> str:
        """
        Build a grounded prompt using the retrieved documents.
        """
        context = ""

        for document in documents:
            metadata = document.metadata

            context += f"""
    ============================================================
    SOURCE          : {metadata.get("document_name", "Unknown")}
    KNOWLEDGE BASE  : {metadata.get("knowledge_base", "Unknown")}
    PAGE            : {metadata.get("page", 0) + 1}
    CHUNK ID        : {metadata.get("chunk_id", "Unknown")}
    ============================================================

    CONTENT:

    {document.page_content.strip()}
    ============================================================
    """

        prompt = f"""{config.SYSTEM_PROMPT}
    ========================= CONTEXT =========================

    {context}

    ===========================================================

    USER QUESTION:

    {query}

    ===========================================================

    FINAL ANSWER:
    """

        return prompt