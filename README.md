# PlantMind-AI

> **Enterprise Retrieval-Augmented Generation (RAG) Copilot for Process Industries**

PlantMind-AI is a modular, production-oriented Retrieval-Augmented Generation (RAG) system designed for engineering knowledge bases. It enables engineers to query technical documents using natural language while generating grounded, context-aware answers from local documentation.

Unlike generic "Chat with PDF" applications, PlantMind-AI is built with scalability, maintainability, and backend engineering best practices in mind.

---

## ✨ Features

-  Multi-Knowledge Base Architecture
-  FAISS Vector Search
-  Local LLM Inference with Ollama
-  BAAI/bge-small-en-v1.5 Embeddings
-  FastAPI REST Backend
-  Streamlit User Interface
-  Dynamic PDF Ingestion Pipeline
-  Conversation Memory
-  Swagger / OpenAPI Documentation
-  Dependency Injection Architecture
-  Centralized Validation Layer
-  Structured Logging
-  Config-Driven Design

---

# Project Architecture

```text
                    User
                      │
          ┌───────────┴───────────┐
          │                       │
      Streamlit UI          FastAPI API
          │                       │
          └───────────┬───────────┘
                      │
                PlantMind RAG
                      │
     ┌────────────────┼────────────────┐
     │                │                │
Retriever       Prompt Builder      Ollama
     │                                 │
     ▼                                 ▼
   FAISS                      Qwen2.5:3B
     │
     ▼
Knowledge Base
```

---

# 📂 Project Structure

```text
PlantMind-AI/
│
├── api/                    # FastAPI backend
├── chains/                 # RAG chains
├── config/                 # Configuration
├── ingestion/              # PDF ingestion pipeline
├── knowledge_manager/      # Knowledge base management
├── llm/                    # LLM wrapper
├── retrieval/              # Retrieval & RAG logic
├── tests/                  # Unit tests
├── ui/                     # Streamlit frontend
├── utils/                  # Logging & utilities
│
├── knowledge_bases/
│   └── heat_exchangers/
│       ├── raw/
│       └── faiss/
│
├── app.py
├── ingest.py
└── requirements.txt
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| LLM | Ollama (Qwen2.5:3B) |
| Embeddings | BAAI/bge-small-en-v1.5 |
| Vector Database | FAISS |
| Framework | LangChain |
| Documentation | Swagger / OpenAPI |

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/SykR23/PlantMind-AI.git
cd PlantMind-AI
```

---

## Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Ollama

Start Ollama

```bash
ollama serve
```

Download the model (first time only)

```bash
ollama pull qwen2.5:3b
```

---

# Ingest Documents

Place your PDFs inside

```text
knowledge_bases/<knowledge_base>/raw/
```

Run

```bash
python ingest.py
```

or use the FastAPI `/ingest` endpoint.

---

# Launch the FastAPI Server

```bash
uvicorn api.server:app --reload
```

Open Swagger

```
http://127.0.0.1:8000/docs
```

---

# Launch Streamlit

```bash
streamlit run app.py
```

---

# REST API

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/knowledge_bases` | List all available knowledge bases |
| POST | `/chat` | Ask questions to the selected knowledge base |
| POST | `/ingest` | Ingest a knowledge base |

---

# Current Capabilities

- Semantic document retrieval
- Context-aware question answering
- Multi-document support
- Dynamic knowledge base management
- Local LLM inference
- Engineering-focused responses
- REST API
- Interactive UI

---

# Roadmap

## Completed

- Multi Knowledge Base Support
- FastAPI Backend
- Streamlit Frontend
- Dependency Injection
- Validation Layer
- Structured Logging
- Swagger Documentation
- Config-Driven Architecture

## In Progress

- Evaluation Framework
- Automated Testing
- Docker Support
- CI/CD

## Planned

- Hybrid Search (Dense + BM25)
- Cross Encoder Reranking
- Authentication
- Multi-user Support
- Cloud Deployment

---

# 👨‍💻 Author

**Sayak Roy**

Chemical Engineering Undergraduate, NIT Durgapur

Interested in AI, NLP, Retrieval-Augmented Generation (RAG), Computer Vision, and Backend Engineering.

---

⭐ If you found this project useful, consider giving it a star!