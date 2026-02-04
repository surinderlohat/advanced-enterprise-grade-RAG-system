from langchain_community.document_loaders import PyPDFLoader


def load_docs(path):
    return PyPDFLoader(path).load()
