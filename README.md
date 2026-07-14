# 🧙 Harry Potter RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions about **Harry Potter and the Philosopher's Stone** using semantic search, LangChain, ChromaDB, and Azure OpenAI.

---

## 📌 Overview

This project uses Retrieval-Augmented Generation (RAG) to answer user queries based on the contents of the Harry Potter book. Instead of relying only on the LLM's knowledge, the chatbot retrieves the most relevant passages from the book and uses them to generate accurate, context-aware responses.

---

## ✨ Features

- 📖 Answers questions from the Harry Potter book
- 🔍 Semantic search using vector embeddings
- 🤖 AI-powered responses using Azure OpenAI
- 📚 PDF document ingestion
- 🧩 Intelligent text chunking
- ⚡ Fast retrieval using ChromaDB

---

## 🛠️ Tech Stack

- Python
- LangChain
- Azure OpenAI
- ChromaDB
- Sentence Transformers
- Streamlit
- python-dotenv

---

## 📂 Project Structure

```text
harry-potter-chatbot/
│
├── data/
├── scripts/
├── src/
├── app.py
├── test_embedding.py
├── test_llm.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/swassstiiiii/harry-potter-chatbot.git
```

Move into the project

```bash
cd harry-potter-chatbot
```

Create a virtual environment

```bash
conda create -n harryrag python=3.11
conda activate harryrag
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your Azure OpenAI credentials.

Example:

```env
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
AZURE_OPENAI_API_VERSION=your_api_version
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
```

> Replace the variable names above with the exact names used in your project if they differ.

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Once the server starts, open the local URL displayed in your terminal (typically `http://localhost:8501`) in your browser.

---

## 📄 License

This project is for educational purposes only.

The Harry Potter book is copyrighted by J.K. Rowling and is **not included for redistribution**. Users should provide their own copy of the document when running this project.

---

## 👩‍💻 Author

**Swasti Jain**