import json
from datetime import datetime
from pathlib import Path

from .models import Chamado


CAMINHO_DADOS = Path(__file__).resolve().parents[1] / "data"
CAMINHO_ARQUIVO = CAMINHO_DADOS / "chamados.json"


def garantir_diretorio():
    CAMINHO_DADOS.mkdir(exist_ok=True)


def chamado_para_dict(chamado: Chamado) -> dict:
    return {
        "id": chamado.id,
        "titulo": chamado.titulo,
        "descricao": chamado.descricao,
        "categoria": chamado.categoria,
        "prioridade": chamado.prioridade,
        "solicitante": chamado.solicitante,
        "data_criacao": chamado.data_criacao.isoformat(),
        "status": chamado.status,
    }


def dict_para_chamado(dados: dict) -> Chamado:
    return Chamado(
        id=dados["id"],
        titulo=dados["titulo"],
        descricao=dados["descricao"],
        categoria=dados["categoria"],
        prioridade=dados["prioridade"],
        solicitante=dados["solicitante"],
        data_criacao=datetime.fromisoformat(dados["data_criacao"]),
        status=dados["status"],
    )


def carregar_chamados() -> list[Chamado]:
    garantir_diretorio()

    if not CAMINHO_ARQUIVO.exists() or CAMINHO_ARQUIVO.stat().st_size == 0:
        return []

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return [dict_para_chamado(item) for item in dados]


def salvar_chamados(chamados: list[Chamado]):
    garantir_diretorio()

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            [chamado_para_dict(chamado) for chamado in chamados],
            arquivo,
            ensure_ascii=False,
            indent=4,
        )
