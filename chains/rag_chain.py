from langchain_openai import ChatOpenAI

from prompts.qa_prompt import QA_PROMPT
from retrieval.reranker import rerank
from retrieval.retriever_vector import retrieve

llm = ChatOpenAI(temperature=0)


def run_rag(query):
    docs = retrieve(query)
    docs = rerank(query, docs)
    context = "\n\n".join(d.page_content for d in docs)

    prompt = QA_PROMPT.format(context=context, question=query)
    return llm.predict(prompt), docs
