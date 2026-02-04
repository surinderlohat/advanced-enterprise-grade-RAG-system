from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(title="Enterprise RAG System")


@app.get("/health")
def health():
    return {"status": "ok"}
