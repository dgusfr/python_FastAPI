from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List
import models
import schemas

# Cria as tabelas no PostgresSQL caso não existam
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
