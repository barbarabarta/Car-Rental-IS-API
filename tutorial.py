"""Small FastAPI example. Start with: python run.py tutorial
Stop the other app first (Ctrl+C); both use port 8000.
Adapted from the official FastAPI First Steps and Path Parameters tutorials.
"""
from fastapi import FastAPI

app = FastAPI(title="First school API")


@app.get("/")
def welcome():
    return {"message": "Hello from the school API"}


@app.get("/students/{student_id}")
def show_input(student_id: int):
    # Only echoes the input: this tutorial does not look up a stored student.
    return {"requested_student_id": student_id}
