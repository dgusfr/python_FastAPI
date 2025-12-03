from pydantic import BaseModel


class EstudanteBase(BaseModel):
    name: str
    age: int


class EstudanteCreate(EstudanteBase):
    pass
