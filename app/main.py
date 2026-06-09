from .services import atualizar_status_chamado, criar_ticket, listar_chamados
from .validators import CATEGORIAS_VALIDAS, PRIORIDADES_VALIDAS, STATUS_VALIDOS


def mostrar_menu():
    print("\n=== Nortedesk ===")
    print("1. Criar ticket")
    print("2. Ver tickets")
    print("3. Alterar status")
    print("4. Sair")


def escolher_opcao(titulo: str, opcoes: list[str]) -> str | None:
    print(f"\n{titulo}")

    for indice, opcao in enumerate(opcoes, start=1):
        print(f"{indice}. {opcao}")

    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        return None

    if escolha < 1 or escolha > len(opcoes):
        return None

    return opcoes[escolha - 1]


def menu_criar_ticket():
    titulo = input("Digite o título do ticket: ")
    descricao = input("Digite a descrição do ticket: ")
    solicitante = input("Digite o nome do solicitante: ")

    categoria = escolher_opcao("Categorias disponíveis:", CATEGORIAS_VALIDAS)
    if categoria is None:
        print("Categoria inválida.")
        return

    prioridade = escolher_opcao("Prioridades disponíveis:", PRIORIDADES_VALIDAS)
    if prioridade is None:
        print("Prioridade inválida.")
        return

    sucesso, mensagem = criar_ticket(
        titulo=titulo,
        descricao=descricao,
        categoria=categoria,
        prioridade=prioridade,
        solicitante=solicitante,
    )

    print(mensagem)


def menu_ver_tickets():
    chamados = listar_chamados()

    if not chamados:
        print("Nenhum ticket cadastrado.")
        return

    print("\n=== Tickets cadastrados ===")

    for chamado in chamados:
        print(
            f"#{chamado.id} | "
            f"{chamado.titulo} | "
            f"{chamado.categoria} | "
            f"{chamado.prioridade} | "
            f"{chamado.status}"
        )


def menu_alterar_status():
    try:
        id_chamado = int(input("Digite o ID do chamado: "))
    except ValueError:
        print("ID inválido. Digite apenas números.")
        return

    novo_status = escolher_opcao("Status disponíveis:", STATUS_VALIDOS)
    if novo_status is None:
        print("Status inválido.")
        return

    sucesso, mensagem = atualizar_status_chamado(id_chamado, novo_status)
    print(mensagem)


def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_criar_ticket()
        elif escolha == "2":
            menu_ver_tickets()
        elif escolha == "3":
            menu_alterar_status()
        elif escolha == "4":
            print("Saindo do Nortedesk. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
