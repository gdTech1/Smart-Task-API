from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime, timezone
from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    status = Column(String, default="todo")  # todo, doing, done

    priority_score = Column(Integer, default=0)
    priority_level = Column(String, default="low")  # low, medium, high

    due_date = Column(DateTime, nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))