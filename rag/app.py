import os

from rag.chains.rag_chain import run_rag
from rag.ingest.chunker import chunk_docs
from rag.ingest.loader import load_docs
from rag.ingest.vector_store import create_vector_store

if not os.path.exists("vector_store"):
    docs = load_docs("data/sample.pdf")
    chunks = chunk_docs(docs)
    create_vector_store(chunks)

question = "What is the data retention policy?"
answer, sources = run_rag(question)

print("\nANSWER:\n", answer)
print("\nSOURCES:", len(sources))
