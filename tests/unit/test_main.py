# Testes hardcoded (má prática)
from db.mock_db import usuarios


def test_read_root():
    response = {"Hello": "World"}
    assert response == {"Hello": "World"}
    assert dict(response) == {"Hello": "World"}


def test_get_users():
    expected_response = [
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
    assert expected_response == usuarios
    assert type(expected_response) is list


def test_get_user_by_id():
    received_id = 1
    expected_result = {}
    for user in usuarios:
        if user['id'] == received_id:
            expected_result = user

    assert expected_result == usuarios[0]
    assert expected_result['id'] == 1
