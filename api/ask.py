from fastapi import APIRouter
from rag.orchestrator import run_rag

router = APIRouter()


@router.get("/ask")
def ask(question: str):
    return run_rag(question)
