import os
import faiss
from sentence_transformers import SentenceTransformer

DATA_DIR = "data"
MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

chunks = []

def chunk_text(text, size=400):
    words = text.split()
    for i in range(0, len(words), size):
        yield " ".join(words[i:i+size])

for file in os.listdir(DATA_DIR):
    path = os.path.join(DATA_DIR, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        for chunk in chunk_text(content):
            if len(chunk.strip()) > 50:
                chunks.append(chunk)

embeddings = model.encode(chunks)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "faiss.index")

with open("chunks.txt", "w", encoding="utf-8") as f:
    for c in chunks:
        f.write(c.replace("\n", " ") + "\n")

print("✅ Knowledge base built successfully")
