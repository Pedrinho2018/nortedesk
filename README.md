# Nortedesk

Sistema simples de chamados de TI criado em Python.

## Funcionalidades

- Criar chamados
- Listar chamados
- Alterar status
- Validar categoria, prioridade e status
- Salvar dados em JSON
- Interface web com Streamlit
- Interface de terminal

## Estrutura

```text
nortedesk/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── services.py
│   ├── storage.py
│   └── validators.py
├── data/
│   └── chamados.json
└── streamlit_app.py
```

## Como Rodar a Interface Web

```powershell
streamlit run streamlit_app.py
```

## Como Rodar no Terminal

```powershell
python -m app.main
```
