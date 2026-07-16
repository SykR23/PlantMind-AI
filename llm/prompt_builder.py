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
            history: list[dict]
    ) -> str:
        """
        Build a grounded prompt using the retrieved documents.
        """
        history_text = ""

        recent_history = history[-8:]

        for message in recent_history:

            role = message["role"].capitalize()

            content = message["content"]

            history_text += (
                f"{role}: {content}\n\n"
            )

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
        
    ====================CONVERSATION HISTORY====================

    {history_text}

    ====================RETRIEVED CONTEXT=======================

    {context}

    =============================================================

    CURRENT QUESTION:

    {query}
    
    ======================INSTRUCTIONS==========================

   1. Answer ONLY using the retrieved context. 
   2. Use the conversation history only to understand references
      such as "it", "that", "previous step", etc.
   3. If the answer is not contained in the retrieved context,
      reply exactly:

   "I couldn't find enough information in the supplied documents."

    ===========================================================

    FINAL ANSWER:
    """

        return prompt