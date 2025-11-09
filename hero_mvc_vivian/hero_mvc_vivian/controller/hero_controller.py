# from fastapi import APIRouter
# from hero_mvc_vivian.model.hero_model import HeroBase
# from hero_mvc_vivian.repository.hero_repository import HeroRepository

# router = APIRouter(prefix="/heroes", tags=["Heroes"])
# repo = HeroRepository()

# @router.get("/")
# def listar_heroes():
#     return repo.listar()

# @router.get("/{id_hero}")
# def buscar_hero(id_hero: int):
#     hero = repo.buscar_por_id(id_hero)
#     return hero or {"erro": "Herói não encontrado"}

# @router.post("/")
# def criar_hero(hero: HeroBase):
#     return repo.criar(hero.dict())

# @router.delete("/{id_hero}")
# def deletar_hero(id_hero: int):
#     return repo.deletar(id_hero)

from fastapi import APIRouter, HTTPException
from hero_mvc_vivian.repository.hero_repository import listar_heroes, buscar_hero_por_id

router = APIRouter(prefix="/heroes", tags=["Heroes"])

@router.get("/")
def get_all_heroes():
    return listar_heroes()

@router.get("/{hero_id}")
def get_hero(hero_id: int):
    hero = buscar_hero_por_id(hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Herói não encontrado")
    return hero
