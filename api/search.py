from fastapi import APIRouter

from rag.retrieval.retriever import hybrid_search

router = APIRouter()


@router.get("/search")
def semantic_search(q: str):
    results = hybrid_search(q)
    return {"query": q, "results": results}
