import pytest
from main import listar_usuarios, criar_usuario, obter_usuario, atualizar_usuario, excluir_usuario


# Fixture para criar um conjunto de dados de usuários mockados
@pytest.fixture
def mock_usuarios():
    return [
        {
            "id": 1,
            "nome": "Dr. John Smith",
            "email": "dr.john.smith@hospital.com",
            "cargo_hospital": "Médico Chefe"
        },
        {
            "id": 2,
            "nome": "Enfermeira Mary Johnson",
            "email": "enfermeira.mary.johnson@hospital.com",
            "cargo_hospital": "Enfermeira Sênior"
        },
        {
            "id": 3,
            "nome": "Administração Hospitalar",
            "email": "admin.hospital@hospital.com",
            "cargo_hospital": "Administrador Hospitalar"
        },
        {
            "id": 4,
            "nome": "Técnico de Laboratório David",
            "email": "tecnico.laboratorio.david@hospital.com",
            "cargo_hospital": "Técnico de Laboratório"
        },
        {
            "id": 5,
            "nome": "Farmacêutico Sarah Brown",
            "email": "farmaceutico.sarah.brown@hospital.com",
            "cargo_hospital": "Farmacêutico Clínico"
        },
        {
            "id": 6,
            "nome": "Dr. Michael Anderson",
            "email": "dr.michael.anderson@hospital.com",
            "cargo_hospital": "Cirurgião"
        },
        {
            "id": 7,
            "nome": "Enfermeira Emily Smith",
            "email": "enfermeira.emily.smith@hospital.com",
            "cargo_hospital": "Enfermeira"
        },
        {
            "id": 8,
            "nome": "Administração Geral",
            "email": "admin.geral@hospital.com",
            "cargo_hospital": "Administrador Geral"
        },
        {
            "id": 9,
            "nome": "Analista de Laboratório Robert",
            "email": "analista.laboratorio.robert@hospital.com",
            "cargo_hospital": "Analista de Laboratório"
        },
        {
            "id": 10,
            "nome": "Técnico de Farmácia Laura",
            "email": "tecnico.farmacia.laura@hospital.com",
            "cargo_hospital": "Técnico de Farmácia"
        }
    ]


# Testes unitários

def test_listar_usuarios(mock_usuarios):
    result = listar_usuarios()
    assert result == mock_usuarios


def test_obter_usuario(mock_usuarios):
    usuario_id = 1
    expected_result = mock_usuarios[0]

    result = obter_usuario(usuario_id)
    assert result == expected_result


def test_obter_usuario_nao_encontrado(mock_usuarios):
    usuario_id = 13

    result = obter_usuario(usuario_id)
    assert result == {"mensagem": "Usuário não encontrado"}


def test_criar_usuario(mock_usuarios):
    novo_usuario = {
        "nome": "Novo Usuário",
        "email": "novo_usuario@example.com",
        "cargo_hospital": "Novo Cargo"
    }

    result = criar_usuario(novo_usuario)
    assert result["id"] == 11  # Verifica se o ID foi atribuído corretamente


def test_atualizar_usuario(mock_usuarios):
    usuario_id = 1
    dados_atualizados = {
        "nome": "Novo Nome",
        "email": "novo_email@example.com"
    }

    result = atualizar_usuario(usuario_id, dados_atualizados)
    assert result == {"mensagem": "Usuário atualizado com sucesso"}
    usuario_atualizado = obter_usuario(usuario_id)
    assert usuario_atualizado["nome"] == "Novo Nome"
    assert usuario_atualizado["email"] == "novo_email@example.com"


def test_atualizar_usuario_nao_encontrado(mock_usuarios):
    usuario_id = 13
    dados_atualizados = {
        "nome": "Novo Nome",
        "email": "novo_email@example.com"
    }

    result = atualizar_usuario(usuario_id, dados_atualizados)
    assert result == {"mensagem": "Usuário não encontrado"}


def test_excluir_usuario(mock_usuarios):
    usuario_id = 1

    result = excluir_usuario(usuario_id)
    assert result == {"mensagem": "Usuário excluído com sucesso"}


def test_excluir_usuario_nao_encontrado(mock_usuarios):
    usuario_id = 13

    result = excluir_usuario(usuario_id)
    assert result == {"mensagem": "Usuário não encontrado"}


if __name__ == "__main__":
    pytest.main()
