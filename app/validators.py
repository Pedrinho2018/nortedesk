CATEGORIAS_VALIDAS = [
    "Computador",
    "Internet",
    "Impressora",
    "Sistema",
    "Usuário/Acesso",
    "Câmeras",
    "E-mail",
    "Outros",
]

PRIORIDADES_VALIDAS = ["Baixa", "Média", "Alta"]
STATUS_VALIDOS = ["Aberto", "Em andamento", "Resolvido", "Fechado"]


def validar_texto(texto: str) -> bool:
    return bool(texto and texto.strip())


def validar_categoria(categoria: str) -> bool:
    return categoria in CATEGORIAS_VALIDAS


def validar_prioridade(prioridade: str) -> bool:
    return prioridade in PRIORIDADES_VALIDAS


def validar_status(status: str) -> bool:
    return status in STATUS_VALIDOS
