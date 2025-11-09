from fastapi import FastAPI
from hero_mvc_vivian.controller.hero_controller import router as hero_router

app = FastAPI(title="Hero MVC API (Banco em Memória)")

app.include_router(hero_router)

@app.get("/")
def raiz():
    return {"mensagem": "API MVC de Hero em memória funcionando!"}
