import os

from chains.rag_chain import run_rag
from ingest.chunker import chunk_docs
from ingest.loader import load_docs
from ingest.vector_store import create_vector_store

if not os.path.exists("vector_store"):
    docs = load_docs("data/sample.pdf")
    chunks = chunk_docs(docs)
    create_vector_store(chunks)

question = "What is the data retention policy?"
answer, sources = run_rag(question)

print("\nANSWER:\n", answer)
print("\nSOURCES:", len(sources))
