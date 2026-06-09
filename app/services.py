from .models import criar_chamado
from .storage import carregar_chamados, salvar_chamados
from .validators import validar_categoria, validar_prioridade, validar_status, validar_texto


chamados = carregar_chamados()


def criar_ticket(
    titulo: str,
    descricao: str,
    categoria: str,
    prioridade: str,
    solicitante: str,
):
    if not validar_texto(titulo):
        return False, "Título é obrigatório."

    if not validar_texto(descricao):
        return False, "Descrição é obrigatória."

    if not validar_texto(solicitante):
        return False, "Solicitante é obrigatório."

    if not validar_categoria(categoria):
        return False, "Categoria inválida."

    if not validar_prioridade(prioridade):
        return False, "Prioridade inválida."

    id_chamado = len(chamados) + 1
    chamado = criar_chamado(
        id_chamado=id_chamado,
        titulo=titulo.strip(),
        descricao=descricao.strip(),
        categoria=categoria,
        prioridade=prioridade,
        solicitante=solicitante.strip(),
    )

    chamados.append(chamado)
    salvar_chamados(chamados)

    return True, f"Ticket #{chamado.id} criado com sucesso."


def listar_chamados():
    return chamados


def buscar_chamado_por_id(id_chamado: int):
    for chamado in chamados:
        if chamado.id == id_chamado:
            return chamado

    return None


def atualizar_status_chamado(id_chamado: int, novo_status: str):
    if not validar_status(novo_status):
        return False, "Status inválido."

    chamado = buscar_chamado_por_id(id_chamado)

    if chamado is None:
        return False, f"Chamado com ID {id_chamado} não encontrado."

    chamado.status = novo_status
    salvar_chamados(chamados)

    return True, f"Status do chamado #{id_chamado} atualizado para {novo_status}."
