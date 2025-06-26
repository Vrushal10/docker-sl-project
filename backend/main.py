from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, ToDo
import os

# Environment variables from Docker
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ToDo API is running"}

@app.get("/todos")
def get_todos():
    db = SessionLocal()
    todos = db.query(ToDo).all()
    db.close()
    return todos

@app.post("/todos")
def create_todo(task: str):
    db = SessionLocal()
    new_task = ToDo(task=task)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    db.close()
    return new_task

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    db = SessionLocal()
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not todo:
        db.close()
        raise HTTPException(status_code=404, detail="ToDo not found")
    db.delete(todo)
    db.commit()
    db.close()
    return {"message": "Deleted successfully"}
