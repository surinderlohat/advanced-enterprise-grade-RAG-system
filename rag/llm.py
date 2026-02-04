import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(context: str, question: str) -> str:
    prompt = f"""
You are a helpful assistant.
Use ONLY the context below to answer.
If answer is not in context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini", messages=[{"role": "user", "content": prompt}], temperature=0
    )

    return response.choices[0].message.content
