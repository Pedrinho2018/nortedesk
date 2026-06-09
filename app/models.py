from dataclasses import dataclass
from datetime import datetime


@dataclass
class Chamado:
    id: int
    titulo: str
    descricao: str
    categoria: str
    prioridade: str
    solicitante: str
    data_criacao: datetime
    status: str


def criar_chamado(
    id_chamado: int,
    titulo: str,
    descricao: str,
    categoria: str,
    prioridade: str,
    solicitante: str,
) -> Chamado:
    return Chamado(
        id=id_chamado,
        titulo=titulo,
        descricao=descricao,
        categoria=categoria,
        prioridade=prioridade,
        solicitante=solicitante,
        data_criacao=datetime.now(),
        status="Aberto",
    )
