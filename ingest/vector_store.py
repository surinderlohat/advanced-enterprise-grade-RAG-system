from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def create_vector_store(chunks):
    db = FAISS.from_documents(chunks, OpenAIEmbeddings())
    db.save_local('vector_store')
