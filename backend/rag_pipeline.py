import faiss
import pickle
from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL, INDEX_PATH, META_PATH


embedding_model = SentenceTransformer(EMBED_MODEL)

index = faiss.read_index(INDEX_PATH)

with open(META_PATH, "rb") as f:
    metadata = pickle.load(f)  

def retrieve_context(query: str, intent: str = None, top_k: int = 10) -> str:
    """
    Semantic search over full FAISS index, filter by intent if specified.
    """
    query_vec = embedding_model.encode([query]).astype("float32")
    scores, indices = index.search(query_vec, top_k * 2)  # Overfetch

    results = []
    for i in indices[0]:
        if i == -1 or i >= len(metadata):
            continue
        entry = metadata[i]
        if intent is None or entry.get("intent") == intent:
            results.append(entry["text"])
        if len(results) >= top_k:
            break

    return "\n\n".join(results) if results else ""


if __name__ == "__main__":
    context = retrieve_context("how do I file a motor claim?", intent="motor_claim", top_k=5)
    print(context)
