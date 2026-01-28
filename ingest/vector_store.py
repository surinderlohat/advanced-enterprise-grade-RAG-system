from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("vector_store")
    return db

def load_vector_store():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local("vector_store", embeddings)
