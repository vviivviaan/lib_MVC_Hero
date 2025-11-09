# 
from hero_mvc_vivian.util.memory_database import heroes

def listar_heroes():
    return heroes

def buscar_hero_por_id(hero_id: int):
    for hero in heroes:
        if hero["id"] == hero_id:
            return hero
    return None
