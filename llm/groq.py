from langchain_groq import ChatGroq

from config.config import config


class GroqLLM:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=config.GROQ_API_KEY,
            model=config.LLM_MODEL,
            temperature=config.TEMPERATURE
        )

    def generate(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content