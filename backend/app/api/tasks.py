from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import SessionLocal
from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import (
    create_task,
    get_tasks,
    get_task_by_id,
    delete_task
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TaskResponse)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)


@router.get("/", response_model=List[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    task = delete_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted"}