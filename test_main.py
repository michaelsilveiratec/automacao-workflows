
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_inicio():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "API funcionando!"}


def test_somar():
    response = client.get("/somar/10/20")
    assert response.status_code == 200
    assert response.json() == {"resultado": 30}

def test_subtrair():
    response = client.get("/subtrair/20/10")
    assert response.status_code == 200
    assert response.json() == {"resultado": 10}

def test_multiplicar():
    response = client.get("/multiplicar/5/6")
    assert response.status_code == 200
    assert response.json() == {"resultado": 30}

def test_dividir():
    response = client.get("/dividir/20/10")
    assert response.status_code == 200
    assert response.json() == {"resultado": 2}

    
def test_dividir_por_zero():
    response = client.get("/dividir/10/0")
    assert response.status_code == 200
    assert response.json() == {
        "erro": "Divisão por zero não é permitida."
    }


def test_somar_com_valor_negativo():
    response = client.get("/somar/-5/10")
    assert response.status_code == 200
    assert response.json() == {"resultado": 5}


def test_somar_com_valor_invalido():
    response = client.get("/somar/abc/10")
    assert response.status_code == 422

