import os
import pickle
import faiss
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import DATA_PATH, INDEX_DIR, META_PATH, EMBED_MODEL, CHUNK_SIZE, CHUNK_OVERLAP, USE_HNSW


def clean_text(text):
    return text.replace('\n', ' ').strip().lower()

def load_text_chunks(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = clean_text(content)

    # Chunk using LangChain
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    docs = splitter.create_documents([content])
    texts = [doc.page_content for doc in docs]
    return texts

def build_index(embeddings, use_hnsw=False):
    dim = embeddings.shape[1]
    embeddings = embeddings.astype("float32")

    if use_hnsw:
        index = faiss.IndexHNSWFlat(dim, 32)
    else:
        index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def run():
    os.makedirs(INDEX_DIR, exist_ok=True)

    print("[*] Loading and chunking scraped document...")
    texts = load_text_chunks(DATA_PATH)

    if not texts:
        raise ValueError("No valid chunks found.")

    print(f"[*] Loaded {len(texts)} chunks.")

    print("[*] Loading embedding model...")
    model = SentenceTransformer(EMBED_MODEL)

    print("[*] Generating embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True).astype("float32")

    print("[*] Building FAISS index...")
    index = build_index(embeddings, use_hnsw=USE_HNSW)
    faiss.write_index(index, os.path.join(INDEX_DIR, "index.faiss"))

    print("[*] Saving metadata...")
    metadata = [{"text": text} for text in texts]
    with open(META_PATH, "wb") as f:
        pickle.dump(metadata, f)

    print(f"[✓] Successfully indexed {len(texts)} chunks from scraped.txt")

if __name__ == "__main__":
    run()
