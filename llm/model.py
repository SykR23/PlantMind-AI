from config.config import config

from llm.ollama import OllamaLLM
from llm.groq import GroqLLM


class PlantMindLLM:

    def __init__(self):

        provider = config.LLM_PROVIDER.lower()

        if provider == "ollama":
            self.llm = OllamaLLM()

        elif provider == "groq":
            self.llm = GroqLLM()

        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")

    def generate(self, prompt: str) -> str:
        return self.llm.generate(prompt)