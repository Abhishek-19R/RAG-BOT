import faiss
from dotenv import load_dotenv
import os
from google import genai
import numpy as np
import hashlib

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=API_KEY)

LLM_NAME = "models/gemini-2.5-flash"

# Load FAISS index and chunks
index = faiss.read_index("faiss.index")

with open("chunks.txt", "r", encoding="utf-8") as f:
    CHUNKS = f.readlines()

# Simple deterministic embedding replacement (NO ML)
def pseudo_embedding(text, dim=384):
    h = hashlib.sha256(text.encode()).digest()
    vec = np.frombuffer(h, dtype=np.uint8).astype("float32")
    vec = np.pad(vec, (0, dim - len(vec) % dim))
    return vec[:dim].reshape(1, -1)

def ask_college_bot(question, top_k=4):
    q_emb = pseudo_embedding(question)
    _, ids = index.search(q_emb, top_k)

    context = ""
    for i in ids[0]:
        context += CHUNKS[i] + "\n"

    prompt = f"""
You are an official AI assistant for Pragati Engineering College.
Answer ONLY using the provided context.
If the answer is not found, say:
"This information is not available in official college records."

CONTEXT:
{context}

QUESTION:
{question}
"""

    response = client.models.generate_content(
        model=LLM_NAME,
        contents=prompt
    )

    return response.text.strip()
