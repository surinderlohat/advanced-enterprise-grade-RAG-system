from rag.retrieval.embeddings import embed_query, embed_texts
from rag.retrieval.vector_store import VectorStore

vector_store = None


def build_index(chunks):
    global vector_store
    # Extract text content from Document objects if needed
    texts = [c.page_content if hasattr(c, "page_content") else str(c) for c in chunks]
    embeddings = embed_texts(texts)
    dim = len(embeddings[0])
    vector_store = VectorStore(dim)
    vector_store.add(embeddings, chunks)


def search(query: str):
    if vector_store is None:
        return []
    q_emb = embed_query(query)
    return vector_store.search(q_emb)
