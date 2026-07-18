from config.config import config


class PlantMindLLM:

    def __init__(self):

        provider = config.LLM_PROVIDER.lower()

        if provider == "ollama":
            from llm.ollama import OllamaLLM
            self.llm = OllamaLLM()

        elif provider == "groq":
            from llm.groq import GroqLLM
            self.llm = GroqLLM()

        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")

    def generate(self, prompt: str) -> str:
        return self.llm.generate(prompt)