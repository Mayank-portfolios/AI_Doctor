# AI_Doctor
A simple **AI-based Doctor Chatbot** that answers health-related questions using **Prompt Engineering** and **RAG (Retrieval-Augmented Generation)**. Built with **Streamlit**, **LangChain**, and **OpenAI API**.

---

## Features

- Ask health-related questions and get responses like a real doctor.
- Uses **Prompt Engineering** to instruct the AI to act as an experienced medical assistant.
- Retrieves relevant information from PDFs using **Vector Store similarity search**.
- Interactive **Streamlit web interface**.

---

## Technology Stack

- Python 3.10+
- Streamlit
- LangChain
- OpenAI API
- PyPDFLoader
- Chroma / FAISS for vector store embeddings
- Pandas & NumPy

---

## Project Structure
Doctorbot/
|
|-main.py
|-.env

How It Works
User Input: User asks a health-related question in the Streamlit input box.
Prompt Engineering: A prompt instructs the AI to answer as an experienced doctor using the context.
AI Response: The AI generates a relevant answer which is displayed in the app.

Learnings
Implemented prompt engineering to make the AI behave like a doctor.
Integrated Streamlit for interactive web apps.
Learned RAG (Retrieval-Augmented Generation) for domain-specific question answering.
Used vector embeddings and similarity search to handle large PDF documents.
