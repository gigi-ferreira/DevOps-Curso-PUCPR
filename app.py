from fastapi import FastAPI
from datetime import datetime

APP = FastAPI()
TAREFAS = []

# Estrutura da tarefa
"""
{
    "id" -> int,
    "titulo" -> str,
    "descricao" -> str,
    "concluida" -> bool,
    "criada_em" -> datetime
}
"""
def criar_tarefa(titulo, descricao):
    return {
        "id": len(TAREFAS),
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False,
        "criada_em": datetime.now()
    }

#Retorna apenas id e titulo de tarefa
@APP.get("/tarefas")
async def tarefas():
    listar_id_titulo = []

    for tarefa in TAREFAS:
        id_tarefa = tarefa['id']
        titulo_tarefa = tarefa['titulo']
        listar_id_titulo.append({id_tarefa: titulo_tarefa})

    return listar_id_titulo

# Função para criar tarefa
@APP.post("/tarefas")
async def post_tarefa(titulo: str, descricao: str):
    global TAREFAS

    tarefa_nova = criar_tarefa(titulo, descricao)

    TAREFAS.append(tarefa_nova)

    return {"mensagem": "OK"}

# Consultando tarefa específica
@APP.get("/tarefas/{id}")
async def consulta_tarefa(id: int):
    for tarefa in TAREFAS:
        if id == int (tarefa['id']):
            return tarefa

# Conclui tarefa caso ela exista
@APP.put("/tarefas/[id]")
async def concluir_tarefa(id: int):
    for tarefa in TAREFAS:
        if id == int (tarefa['id']):
            tarefa['concluida'] = True
            tarefa['concluida_em'] = datetime.now()
            return {"mensagem": "Tarefa Concluida!"}
        
    return {"mensagem:": "Tarefa não existe"}

# Excluir uma tarefa
@APP.delete("/tarefas/{id}")
async def apagar_tarefa(id: int):
    global TAREFAS
    
    indice = 0
    for tarefa in TAREFAS:
        if id == int(tarefa['id']):
            TAREFAS.pop(indice)
            return {"mensagem": "Tarefa apagada"}

        indice += 1
    
    return {"mensagem": "Tarefa não existe"}

@APP.get("/")
async def index():
    return {"mensagem": "Olá, mundo!"}