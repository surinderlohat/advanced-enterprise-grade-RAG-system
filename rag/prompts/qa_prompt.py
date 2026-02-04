from langchain_core.prompts import PromptTemplate

QA_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are an enterprise AI assistant.
Answer ONLY using the context.
If not found, say "Information not available".

Context:
{context}

Question:
{question}
""",
)
