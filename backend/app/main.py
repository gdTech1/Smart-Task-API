from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.tasks import router as task_router

app = FastAPI(title="Smart Task API")

app.include_router(task_router)

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}