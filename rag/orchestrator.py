from retrieval.retriever import search

from rag.llm import generate_answer


def run_rag(question: str):
    chunks = search(question)
    context = "\n\n".join(chunks)

    answer = generate_answer(context, question)

    return {"answer": answer, "sources": chunks}
