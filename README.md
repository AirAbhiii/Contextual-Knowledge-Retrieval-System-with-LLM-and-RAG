# Contextual Knowledge Retrieval System with LLM and RAG

An intelligent, end-to-end Retrieval-Augmented Generation (RAG) system powered by an agentic AI architecture. This system features dynamic query routing, intelligent document retrieval, and advanced LLM capabilities to provide accurate, context-aware answers.

## 🌟 Overview

The **Contextual Knowledge Retrieval System** intelligently adapts its retrieval strategy based on the query type. It can utilize indexed documents, general knowledge, or real-time web search to generate comprehensive and relevant responses.

Built with a modular architecture using **LangGraph** for workflow orchestration, **FastAPI** for the backend, and **Streamlit** for a modern user interface.

## 🚀 Key Features

*   **Intelligent Query Routing**: Automatically classifies queries into Index (Document-based), General Knowledge, or Web Search.
*   **Advanced RAG Pipeline**: Optimized document chunking, embedding, and vector search.
*   **Agentic AI Architecture**: Multi-agent system using the ReAct framework for reasoning and action.
*   **Vector Search**: Powered by **Qdrant** (with FAISS fallback).
*   **State Management**: Persistent chat history and session tracking using **MongoDB**.
*   **Modern UI**: Interactive Streamlit dashboard for chatting and document uploads.

## 🛠️ Technology Stack

*   **LLM Framework**: LangChain & LangGraph
*   **Backend**: FastAPI
*   **Frontend**: Streamlit
*   **Vector DB**: Qdrant / FAISS
*   **Database**: MongoDB
*   **LLMs**: Groq
*   **Search**: Tavily

## 📋 Prerequisites

*   Python 3.9+
*   MongoDB (Local or Cloud)
*   Qdrant (Optional, FAISS fallback available)
*   API Keys:Groq and Tavily

## ⚙️ Installation & Setup

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/AirAbhiii/Contextual-Knowledge-Retrieval-System-with-LLM-and-RAG.git
    cd "Contextual Knowledge Retrieval System with LLM and RAG"
    ```

2.  **Create Virtual Environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    source venv/bin/activate # Linux/Mac
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**:
    Create a `.env` file in the root directory and add your keys:
    ```env
    GROQ_API_KEY=your_groq_key
    TAVILY_API_KEY=your_tavily_key
    MONGODB_URL=mongodb://localhost:27017
    MONGODB_DB_NAME=contextual_knowledge_retrieval
    ```

## 🏃 Running the Application

### 1. Start the Backend (FastAPI)
```bash
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Start the Frontend (Streamlit)
```bash
streamlit run streamlit_app/home.py
```

## 📖 Usage

1.  Access the web interface at `http://localhost:8501`.
2.  Login or create an account.
3.  Upload PDF or TXT documents to build your knowledge base.
4.  Ask questions! The system will decide whether to use your documents, its internal knowledge, or the web.

