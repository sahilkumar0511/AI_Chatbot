from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores.faiss import FAISS
import numpy as np

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
index = None

def generate_embeddings(text):
    embeddings = model.encode([text])
    return embeddings

def update_vector_database(post_id, embeddings):
    global index
    if index is None:
        index = FAISS.from_embeddings(embeddings)
    else:
        index.add_embeddings(embeddings)
    # Store post_id to embeddings mapping if necessary
