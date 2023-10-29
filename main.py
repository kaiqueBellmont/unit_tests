from fastapi import FastAPI
from db.mock_db import usuarios

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Rota para listar todos os usuários
@app.get("/usuarios/")
def listar_usuarios():
    return usuarios


# Rota para criar um novo usuário
@app.post("/usuarios/")
def criar_usuario(usuario: dict):
    new_user = {'id': len(usuarios) + 1, **usuario}
    usuarios.append(new_user)
    return new_user


# Rota para obter um usuário por ID
@app.get("/usuarios/{usuario_id}")
def obter_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario
    return {"mensagem": "Usuário não encontrado"}


# Rota para atualizar um usuário por ID
@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, dados_atualizados: dict):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            usuario.update(dados_atualizados)
            return {"mensagem": "Usuário atualizado com sucesso"}
    return {"mensagem": "Usuário não encontrado"}


# Rota para excluir um usuário por ID
@app.delete("/usuarios/{usuario_id}")
def excluir_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            usuarios.remove(usuario)
            return {"mensagem": "Usuário excluído com sucesso"}
    return {"mensagem": "Usuário não encontrado"}
