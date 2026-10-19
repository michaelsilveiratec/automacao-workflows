from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "API funcionando!"}

@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    return {"resultado": a + b}

@app.get("/subtrair/{a}/{b}")
def subtrair(a: int, b: int):
    return {"resultado": a - b}

@app.get("/multiplicar/{a}/{b}")
def multiplicar(a: int, b: int):
    return {"resultado": a * b}

@app.get("/dividir/{a}/{b}")
def dividir(a: int, b: int):
    if b == 0:
        return {"erro": "Divisão por zero não é permitida."}
    return {"resultado": a / b} 
