from sentence_transformers import CrossEncoder

_model = None


def get_reranker():
    global _model
    if _model is None:
        _model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    return _model


def rerank(query: str, docs: list[str], top_k=5):
    model = get_reranker()
    pairs = [(query, doc) for doc in docs]
    scores = model.predict(pairs)

    ranked = sorted(zip(scores, docs, strict=False), reverse=True)
    return [doc for _, doc in ranked[:top_k]]
