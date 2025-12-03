from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Estudante(Base):
    __tablename__ = "estudantes"
    id = Column(Integer, PramaryKey=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)


class Matricula(Base):
    __tablename__ = "matriculas"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("estudante.id"))
    discipline_name = Column(String(100), nullable=False)
