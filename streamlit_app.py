import streamlit as st

from app.services import atualizar_status_chamado, criar_ticket, listar_chamados
from app.validators import CATEGORIAS_VALIDAS, PRIORIDADES_VALIDAS, STATUS_VALIDOS

st.set_page_config(page_title="Nortedesk", page_icon=":clipboard:", layout="centered")
st.title("Nortedesk - Sistema de Chamados")
st.caption("Interface simples para abertura e acompanhamento de chamados de TI.")

st.markdown(
    """
    <style>
    .chamado-card {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        background: #ffffff;
    }

    .chamado-header {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        align-items: flex-start;
        margin-bottom: 10px;
    }

    .chamado-titulo {
        font-size: 1.05rem;
        font-weight: 700;
        color: #111827;
    }

    .chamado-status {
        border-radius: 999px;
        padding: 4px 10px;
        background: #eef2ff;
        color: #3730a3;
        font-size: 0.82rem;
        font-weight: 600;
        white-space: nowrap;
    }

    .chamado-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 8px 14px;
        color: #374151;
        font-size: 0.92rem;
    }

    .chamado-label {
        color: #6b7280;
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0;
    }

    @media (max-width: 640px) {
        .chamado-header {
            display: block;
        }

        .chamado-status {
            display: inline-block;
            margin-top: 8px;
        }

        .chamado-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.form("form_criar_ticket"):
    st.subheader("Criar Novo Chamado")
    titulo = st.text_input("Título do Chamado")
    descricao = st.text_area("Descrição do Chamado")
    solicitante = st.text_input("Nome do Solicitante")

    categoria = st.selectbox("Categoria", CATEGORIAS_VALIDAS)
    prioridade = st.selectbox("Prioridade", PRIORIDADES_VALIDAS)

    submitted = st.form_submit_button("Criar Chamado")

    if submitted:
        sucesso, mensagem = criar_ticket(
            titulo=titulo,
            descricao=descricao,
            categoria=categoria,
            prioridade=prioridade,
            solicitante=solicitante,
        )
        if sucesso:
            st.success(mensagem)
        else:
            st.error(mensagem)

st.divider()
st.subheader("Chamados Cadastrados")

chamados = listar_chamados()

if not chamados:
    st.info("Nenhum chamado cadastrado.")
else:
    for chamado in chamados:
        data_criacao = chamado.data_criacao.strftime("%d/%m/%Y %H:%M")

        st.markdown(
            f"""
            <div class="chamado-card">
                <div class="chamado-header">
                    <div class="chamado-titulo">#{chamado.id} - {chamado.titulo}</div>
                    <div class="chamado-status">{chamado.status}</div>
                </div>
                <div class="chamado-grid">
                    <div>
                        <div class="chamado-label">Solicitante</div>
                        <div>{chamado.solicitante}</div>
                    </div>
                    <div>
                        <div class="chamado-label">Categoria</div>
                        <div>{chamado.categoria}</div>
                    </div>
                    <div>
                        <div class="chamado-label">Prioridade</div>
                        <div>{chamado.prioridade}</div>
                    </div>
                    <div>
                        <div class="chamado-label">Data</div>
                        <div>{data_criacao}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.subheader("Alterar Status")

if not chamados:
    st.info("Crie um chamado antes de alterar status.")
else:
    ids_chamados = [chamado.id for chamado in chamados]

    with st.form("form_alterar_status"):
        id_chamado = st.selectbox("Chamado", ids_chamados)
        novo_status = st.selectbox("Novo status", STATUS_VALIDOS)
        atualizar = st.form_submit_button("Atualizar Status")

        if atualizar:
            sucesso, mensagem = atualizar_status_chamado(id_chamado, novo_status)

            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)
