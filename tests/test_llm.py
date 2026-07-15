from llm.model import PlantMindLLM

model = PlantMindLLM()

response = model.generate(
    "Explain a plate heat exchanger in two sentences."
)

print(response)