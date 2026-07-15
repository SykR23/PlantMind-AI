from langchain_ollama import ChatOllama

from config.config import config


class PlantMindLLM:
    def __init__(self):
        self.llm = ChatOllama(
            model = config.LLM_MODEL,
            temperature = config.TEMPERATURE
        )

    def generate(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content