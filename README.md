# PlantMind-AI

> **An AI-powered Retrieval-Augmented Generation (RAG) copilot for process industries.**

PlantMind-AI is a modular engineering assistant that enables engineers to query technical manuals and domain-specific documentation using natural language. It combines semantic search with Large Language Models (LLMs) to provide grounded, context-aware answers instead of hallucinated responses.

🔗 **Live Demo:** https://plantmind-ai-ewjxqd3ubd9pg2bqbh3uac.streamlit.app/

---

## ✨ Features

-  Dynamic PDF ingestion pipeline
-  Retrieval-Augmented Generation (RAG)
-  FAISS vector search
-  HuggingFace BGE embeddings
-  Groq LLM integration
-  Provider-agnostic LLM architecture (Groq / Ollama)
-  Multi-knowledge-base architecture
-  Source-aware responses
-  Streamlit deployment
-  Configuration-driven design

---

# Demo

<img src="assets/demo.gif" width="100%">

*(Replace with screenshots or GIF later.)*

---

# Architecture

```
                        User Query
                             │
                             ▼
                     Streamlit Frontend
                             │
                             ▼
                      PlantMind RAG
                             │
          ┌──────────────────┴─────────────────┐
          ▼                                    ▼
   HuggingFace Embeddings                 FAISS Retriever
          │                                    │
          └──────────────┬─────────────────────┘
                         ▼
                  Relevant Chunks
                         │
                         ▼
                  Prompt Construction
                         │
                         ▼
                  Groq / Ollama LLM
                         │
                         ▼
                     Final Answer
```

---

# Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| LLM | Groq, Ollama |
| Framework | LangChain |
| Embeddings | HuggingFace BAAI/bge-small-en-v1.5 |
| Vector Database | FAISS |
| Frontend | Streamlit |
| Backend | FastAPI |
| Deployment | Streamlit Community Cloud |
| Document Processing | PyPDF |

---

# Project Structure

```
PlantMind-AI/
│
├── app.py
├── config/
├──chains/
├── ingestion/
├── retrieval/
├── rag/
├── llm/
├── prompts/
├── knowledge_bases/
│   ├── heat_exchangers/
│   ├── pumps/
│   ├── process_control/
│   └── safety/
├── ui/
├── utils/
├── requirements.txt
└── README.md
```

---

# Current Workflow

```
PDF Documents
      │
      ▼
Document Loader
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
FAISS Index
      │
      ▼
User Query
      │
      ▼
Semantic Retrieval
      │
      ▼
LLM
      │
      ▼
Grounded Response
```

---

# Supported Knowledge Bases

- ✅ Heat Exchangers
- 🚧 Pumps
- 🚧 Process Control
- 🚧 Industrial Safety

---

# Installation

Clone the repository

```bash
git clone https://github.com/SykR23/PlantMind-AI.git
cd PlantMind-AI
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env`

```env
GROQ_API_KEY=YOUR_API_KEY

LLM_PROVIDER=groq
LLM_MODEL=llama-3.3-70b-versatile

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5

DEVICE=cpu

TEMPERATURE=0.2
```

---

# Running

```bash
streamlit run app.py
```

---

# Example Questions

- What are refrigerants?
- How do I clean a brazed plate heat exchanger?
- What is the purpose of a gasket?
- Explain fouling in plate heat exchangers.
- Which heat exchanger should be selected for food applications?

---

# Roadmap

## Completed

- [x] Modular RAG pipeline
- [x] PDF ingestion
- [x] FAISS indexing
- [x] HuggingFace embeddings
- [x] Groq integration
- [x] Ollama integration
- [x] Streamlit deployment
- [x] Source attribution

## In Progress

- [ ] FastAPI backend
- [ ] Railway deployment
- [ ] Multi-KB selector
- [ ] Response streaming
- [ ] Docker support

## Planned

- [ ] React frontend
- [ ] Hybrid Search (BM25 + FAISS)
- [ ] Cross-Encoder reranking
- [ ] Conversation memory
- [ ] Authentication
- [ ] Admin dashboard

---

# Why PlantMind-AI?

Traditional chatbots often hallucinate technical information.

PlantMind-AI retrieves relevant information directly from engineering manuals before generating responses, ensuring answers remain grounded in authoritative documentation.

The project demonstrates a production-oriented RAG architecture with modular components, configurable LLM providers, and scalable knowledge base support.

---

# Author

**Sayak Roy**

Chemical Engineering Undergraduate  
National Institute of Technology Durgapur
