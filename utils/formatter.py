from langchain_core.documents import Document


class SourceFormatter:
    """
        Utility class for formatting retrieved document sources.
        """

    @staticmethod
    def format_sources(
            documents: list[Document]
    ) -> str:

        formatted = []

        for i, document in enumerate(documents, start=1):
            metadata = document.metadata
            formatted.append(
                f"""Source {i}

            Document       : {metadata.get("document_name", "Unknown")}
            Knowledge Base : {metadata.get("knowledge_base", "Unknown")}
            Page           : {metadata.get("page", 0) + 1}
            Chunk ID       : {metadata.get("chunk_id", "Unknown")}

            ------------------------------------------------------------"""
            )
            return "\n\n".join(formatted)