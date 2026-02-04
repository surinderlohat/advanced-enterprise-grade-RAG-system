from fastapi import APIRouter

from rag.retrieval.retriever import search

router = APIRouter()


@router.get("/search")
def semantic_search(q: str):
    results = search(q)
    return {"query": q, "results": results}
