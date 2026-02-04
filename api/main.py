from dotenv import load_dotenv
from fastapi import FastAPI

from api import upload

load_dotenv()

app = FastAPI(title="Enterprise RAG System")

app.include_router(upload.router)


@app.get("/health")
def health():
    return {"status": "ok"}
