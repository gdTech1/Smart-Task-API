from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}