from rag.llm import generate_answer
from rag.retrieval.reranker import rerank
from rag.retrieval.retriever import hybrid_search


def run_rag(question: str):
    candidates = hybrid_search(question, k=10)
    top_chunks = rerank(question, candidates, top_k=5)

    context = "\n\n".join([f"[Source {i + 1}]\n{chunk}" for i, chunk in enumerate(top_chunks)])

    answer = generate_answer(context, question)

    return {"answer": answer, "sources": [{"id": i + 1, "text": chunk} for i, chunk in enumerate(top_chunks)]}
