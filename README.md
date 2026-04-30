🚀 An AI-powered chatbot that answers queries using real college website data, reducing hallucinations with Retrieval-Augmented Generation (RAG).

📌 Overview

The RAG bot is designed to provide accurate and reliable answers to queries about college information by using actual scraped data instead of generic LLM responses.

Unlike traditional chatbots, this system:

Retrieves relevant context from real data

Uses LLM only for grounded responses

Minimizes hallucinations significantly

🧠 Key Features

📚 RAG-Based Architecture

Combines retrieval + generation for accurate answers

🌐 Automated Data Extraction

Scrapes college website using Python

🧹 Data Cleaning Pipeline

Removes noise like headers, navbars, irrelevant HTML

🔍 Semantic Search (Embeddings)

Retrieves most relevant chunks for each query

🤖 Context-Aware Responses

LLM answers strictly based on retrieved data

🏗️ Architecture

User Query → Retriever (Embeddings Search) → Context → LLM → Response

🛠️ Tech Stack

Language: Python

Scraping: BeautifulSoup, Requests

AI: LLM + Embeddings

RAG Pipeline: Chunking, Vector Storage, Retrieval

Optional UI: CLI / Web Interface

🚀 How It Works

Scrape data from college website

Clean and preprocess content

Split data into chunks

Generate embeddings

Store in vector database

Retrieve relevant chunks for query

LLM generates answer using context

📂 Project Structure

PEC-Chatbot/

│── data/               # Raw + cleaned data  

│── scraper/           # Web scraping scripts  

│── processing/        # Cleaning & chunking  

│── embeddings/        # Embedding generation  

│── vector_db/         # Storage  

│── chatbot/           # Query handling  

│── app.py             # Main entry point  

⚙️ Installation

git clone <your-repo-link>

cd PEC-Chatbot

pip install -r requirements.txt

▶️ Run

python app.py

🎯 Problem Solved

❌ LLM hallucinations

❌ Inaccurate college info

❌ Static FAQ limitations

✅ Provides accurate, real-data-driven answers

📊 Future Improvements

🌐 Web UI with chat interface

📡 Auto re-scraping & re-indexing

🧠 Better embeddings / hybrid search

☁️ Cloud deployment

🤝 Author
👨‍💻 Abhishek Reddy 
