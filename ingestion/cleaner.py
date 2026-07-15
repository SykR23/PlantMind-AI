import re

from langchain_core.documents import Document


class DocumentCleaner:
    """
        Cleans and normalizes extracted PDF text.
        """
    def clean(

        self,

        documents: list[Document],

    ) -> list[Document]:

        cleaned_documents = []

        for document in documents:

            text = document.page_content

            text = re.sub(

                r"\n+",

                "\n",

                text,

            )

            text = re.sub(

                r"\s+",

                " ",

                text,

            )

            document.page_content = text.strip()

            cleaned_documents.append(

                document

            )

        return cleaned_documents