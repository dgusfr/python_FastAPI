from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List
import models
import schemas

# Cria as tabelas no PostgresSQL caso não existam
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/estudantes/", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    # Desestruturamos os dados vindos do navegador e model_dump converte em um dicionario com os dados validados, para chamarmos o construtor e criarmos o objeto estudante
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/estudantes/", response_model=List[schemas.StudentResponse])
def read_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students
