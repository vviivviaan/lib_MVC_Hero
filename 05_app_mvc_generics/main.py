from fastapi import FastAPI
from util.database import init_db
from controller.hero import router as heroes_router
from controller.team import router as teams_router

app = FastAPI(title="FastAPI + SQLModel - MVC + Repository")

init_db()

app.include_router(heroes_router)
app.include_router(teams_router)

@app.get("/")
def health():
    return {"status": "ok"}


# from fastapi import FastAPI
# from app.controller.hero import HeroController

# app = FastAPI()
# controller = HeroController()


# @app.post("/heroes")
# def create_hero(name: str, power: str):
#     return controller.create_hero(name, power)


# @app.get("/heroes")
# def list_heroes():
#     return controller.list_heroes()


# @app.get("/heroes/{hero_id}")
# def get_hero(hero_id: int):
#     return controller.get_hero(hero_id)


# @app.delete("/heroes/{hero_id}")
# def delete_hero(hero_id: int):
#     return controller.delete_hero(hero_id)
