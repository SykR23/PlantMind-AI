class QueryRewriter:
    """
        Converts conversational follow-up questions into
        standalone questions before retrieval.
        """

    def rewrite(self, query: str, history: list[dict]) -> str:
        if len(history) == 0:
            return query

        if len(query.split()) > 5:
            return query

        last_user = ""

        for message in reversed(history[:-1]):
            if message["role"] == "user":
                last_user = message["content"]
                break

        if not last_user:
            return query

        return f"{last_user} {query}"