"""Teste unitário para a classe Tarefa"""
from datetime import datetime, timezone
from app.modelo import Tarefa


def criar_tarefa_mock():
    """Cria uma tarefa mock para teste"""
    return Tarefa(
        titulo="Tarefa teste",
        data_criacao=datetime.now().replace(microsecond=0),
    )


def test_nova_tarefa():
    """Teste unitário para criar uma nova tarefa"""
    t = criar_tarefa_mock()

    assert t.get_id() is None
    assert t.titulo == "Tarefa teste"
    assert t.descricao is None
    assert t.data_criacao == datetime.now().replace(microsecond=0)
    assert t.data_conclusao is None
    assert t.concluida is False

def test_tarefa_concluida():
    """Teste unitário para concluir uma tarefa"""
    t = criar_tarefa_mock()

    t.finalizar()
    assert t.concluida is True
    assert t.data_conclusao == datetime.now().astimezone(timezone.utc).replace(microsecond=0)
