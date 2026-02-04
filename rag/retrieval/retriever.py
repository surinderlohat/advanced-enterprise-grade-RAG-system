from retrieval.embeddings import embed_query, embed_texts
from retrieval.sparse_index import SparseIndex
from retrieval.vector_store import VectorStore

vector_store = None
sparse_index = None

def build_index(chunks):
    global vector_store, sparse_index

    embeddings = embed_texts(chunks)
    dim = len(embeddings[0])

    vector_store = VectorStore(dim)
    vector_store.add(embeddings, chunks)

    sparse_index = SparseIndex()
    sparse_index.add(chunks)

def hybrid_search(query: str, k=5):
    dense_results = vector_store.search(embed_query(query), k)
    sparse_results = sparse_index.search(query, k)

    # merge + deduplicate
    combined = list(dict.fromkeys(dense_results + sparse_results))
    return combined[:k]
