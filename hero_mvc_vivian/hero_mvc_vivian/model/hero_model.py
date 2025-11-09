from pydantic import BaseModel

class HeroBase(BaseModel):
    nome: str
    idade: int
    cidade: str

class Hero(HeroBase):
    id: int
