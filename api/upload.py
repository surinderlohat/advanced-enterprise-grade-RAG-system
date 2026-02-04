import os

from fastapi import APIRouter, File, UploadFile

from rag.ingest.chunker import chunk_docs
from rag.ingest.loader import load_docs as load_pdf

router = APIRouter()

UPLOAD_DIR = ".uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, file.filename)

    with open(path, "wb") as f:
        f.write(await file.read())

    docs = load_pdf(path)
    chunks = chunk_docs(docs)

    return {"filename": file.filename, "total_chunks": len(chunks), "preview": chunks[:3]}
