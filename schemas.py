from pydantic import BaseModel


class EstudanteBase(BaseModel):
    name: str
    age: int


class EstudanteCreate(EstudanteBase):
    pass


# Definimos que podemos ler os campos do estudante direto do modelo
class EstudanteResponse(EstudanteBase):
    id: int

    class Config:
        from_atributes = True


class MatriculaBase(BaseModel):
    student_id: int
    discipline_name: str
