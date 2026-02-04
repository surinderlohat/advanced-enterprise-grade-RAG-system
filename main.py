import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from api.ask import router as ask_router
from api.search import router as search_router
from api.upload import router as upload_router

load_dotenv()

app = FastAPI(title="Enterprise RAG System")

app.include_router(upload_router)
app.include_router(search_router)
app.include_router(ask_router)


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
