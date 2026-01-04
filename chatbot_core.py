import faiss
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "all-MiniLM-L6-v2"
LLM_NAME = "models/gemini-2.5-flash"



model = SentenceTransformer(MODEL_NAME)
index = faiss.read_index("faiss.index")

with open("chunks.txt", "r", encoding="utf-8") as f:
    CHUNKS = f.readlines()

def ask_college_bot(question, top_k=4):
    q_emb = model.encode([question])
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
