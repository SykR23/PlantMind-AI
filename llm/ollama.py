from langchain_ollama import ChatOllama

from config.config import config


class OllamaLLM:
    def __init__(self):
        self.llm = ChatOllama(
            model=config.LLM_MODEL,
            temperature=config.TEMPERATURE
        )

    def generate(self, prompt: str) -> str:
        print("=" * 80)
        print("PROMPT LENGTH: ", len(prompt))
        print("=" * 80)

        response = self.llm.invoke(prompt)
        return response.content