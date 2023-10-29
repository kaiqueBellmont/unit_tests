import pytest
from fastapi.testclient import TestClient
from main import app, usuarios
from faker import Faker

fake = Faker()
client = TestClient(app)

# Função de setup para criar uma lista de usuários fictícios para testes
def setup_function():
    mock_usuarios = [
        {
            "id": i + 1,
            "nome": fake.name(),
            "email": fake.email(),
            "cargo_hospital": fake.job()
        } for i in range(10)
    ]
    usuarios.clear()  # Limpa a lista de usuários original
    usuarios.extend(mock_usuarios)

# Função de teardown para limpar a lista de usuários após os testes
def teardown_function():
    usuarios.clear()

def test_listar_usuarios():
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert response.json() == usuarios

def test_obter_usuario():
    usuario_id = 1
    response = client.get(f"/usuarios/{usuario_id}")
    assert response.status_code == 200
    assert response.json() == usuarios[usuario_id - 1]

def test_obter_usuario_nao_encontrado():
    usuario_id = 13
    response = client.get(f"/usuarios/{usuario_id}")
    assert response.status_code == 404
    assert response.json() == {"mensagem": "Usuário não encontrado"}

def test_criar_usuario():
    novo_usuario = {
        "nome": fake.name(),
        "email": fake.email(),
        "cargo_hospital": fake.job()
    }
    response = client.post("/usuarios/", json=novo_usuario)
    assert response.status_code == 200
    assert response.json()["id"] == 11

def test_atualizar_usuario():
    usuario_id = 1
    dados_atualizados = {
        "nome": fake.name(),
        "email": fake.email(),
        "cargo_hospital": fake.job()
    }
    response = client.put(f"/usuarios/{usuario_id}", json=dados_atualizados)
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Usuário atualizado com sucesso"}

def test_atualizar_usuario_nao_encontrado():
    usuario_id = 13
    dados_atualizados = {
        "nome": fake.name(),
        "email": fake.email(),
        "cargo_hospital": fake.job()
    }
    response = client.put(f"/usuarios/{usuario_id}", json=dados_atualizados)
    assert response.status_code == 404
    assert response.json() == {"mensagem": "Usuário não encontrado"}

def test_excluir_usuario():
    usuario_id = 1
    response = client.delete(f"/usuarios/{usuario_id}")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Usuário excluído com sucesso"}

def test_excluir_usuario_nao_encontrado():
    usuario_id = 13
    response = client.delete(f"/usuarios/{usuario_id}")
    assert response.status_code == 404
    assert response.json() == {"mensagem": "Usuário não encontrado"}

if __name__ == "__main__":
    pytest.main()
