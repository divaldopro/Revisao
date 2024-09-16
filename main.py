from fastapi import FastAPI # importando biblioteca FastAPI

app = FastAPI()   # instanciando  um fastapi na variavel app


@app.get("/")   #retornar mensagem hello word 127.0.0.1:8000/
async def root():    # função assincrona
    return {"message": "Hello World"}

@app.get("/teste")   #retornar mensagem 127.0.0.1:8000/teste
async def funcaoteste():    # função assincrona
    return {"teste": "deu certo"}

@app.get("/teste2")   #retornar mensagem 127.0.0.1:8000/teste2
async def funcaoteste2():    # função assincrona
    return {"teste": "deu certo teste 2"}

@app.get("/teste2")   #retornar mensagem 127.0.0.1:8000/teste3
async def funcaoteste2():    # função assincrona
    return {"teste": "deu certo teste 3"}