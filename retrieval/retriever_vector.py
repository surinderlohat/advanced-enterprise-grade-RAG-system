from ingest.vector_store import load_vector_store


def retrieve(query, k=6):
    db = load_vector_store()
    retriever = db.as_retriever(search_kwargs={"k": k})
    return retriever.get_relevant_documents(query)
