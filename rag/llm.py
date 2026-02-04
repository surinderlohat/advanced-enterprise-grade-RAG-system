import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "sk-your_token_here"))


def generate_answer(context: str, question: str) -> str:
    prompt = f"""
    You are an enterprise assistant.
    Answer ONLY using the sources below.
    Cite sources like [Source 1], [Source 2].

    Sources:
    {context}

    Question:
    {question}

    Answer:
    """
    response = client.chat.completions.create(
        model="gpt-4.1-mini", messages=[{"role": "user", "content": prompt}], temperature=0
    )

    return response.choices[0].message.content
