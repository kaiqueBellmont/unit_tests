import pytest
from main import listar_usuarios, criar_usuario, obter_usuario, atualizar_usuario, excluir_usuario
from faker import Faker

fake = Faker()


# Testes unitários

def test_listar_usuarios():
    # Simule a criação de uma lista de usuários fictícios usando o Faker
    mock_usuarios = [
        {
            "id": i + 1,
            "nome": fake.name(),
            "email": fake.email(),
            "cargo_hospital": fake.job()
        } for i in range(10)
    ]

    result = listar_usuarios()
    assert result == mock_usuarios


def test_obter_usuario():
    # Simule a criação de um usuário fictício usando o Faker
    usuario_id = 1
    mock_usuario = {
        "id": usuario_id,
        "nome": fake.name(),
        "email": fake.email(),
        "cargo_hospital": fake.job()
    }

    result = obter_usuario(usuario_id)
    assert result == mock_usuario


def test_obter_usuario_nao_encontrado():
    usuario_id = 13

    result = obter_usuario(usuario_id)
    assert result == {"mensagem": "Usuário não encontrado"}


def test_criar_usuario():
    novo_usuario = {
        "nome": fake.name(),
        "email": fake.email(),
        "cargo_hospital": fake.job()
    }

    result = criar_usuario(novo_usuario)
    assert result["id"] == 11  # Verifica se o ID foi atribuído corretamente


def test_atualizar_usuario():
    usuario_id = 1
    dados_atualizados = {
        "nome": fake.name(),
        "email": fake.email(),
        "cargo_hospital": fake.job()
    }

    result = atualizar_usuario(usuario_id, dados_atualizados)
    assert result == {"mensagem": "Usuário atualizado com sucesso"}


def test_atualizar_usuario_nao_encontrado():
    usuario_id = 13
    dados_atualizados = {
        "nome": fake.name(),
        "email": fake.email(),
        "cargo_hospital": fake.job()
    }

    result = atualizar_usuario(usuario_id, dados_atualizados)
    assert result == {"mensagem": "Usuário não encontrado"}


def test_excluir_usuario():
    usuario_id = 1

    result = excluir_usuario(usuario_id)
    assert result == {"mensagem": "Usuário excluído com sucesso"}


def test_excluir_usuario_nao_encontrado():
    usuario_id = 13

    result = excluir_usuario(usuario_id)
    assert result == {"mensagem": "Usuário não encontrado"}


if __name__ == "__main__":
    pytest.main()
