#======================================================
#             Arquivo de Limpeza
#======================================================
import streamlit as st


# =====================================================
# 🔒 ESTADOS PROTEGIDOS (NUNCA APAGAR)
# =====================================================
PROTEGIDOS = [
    "logado",
    "email",
    "plano",
    "etapa"
]


# =====================================================
# BASE
# =====================================================
def _pop(lista):
    for k in lista:
        st.session_state.pop(k, None)


# =====================================================
# ETAPA 01 — IDEIAS
# =====================================================
def limpar_ideias():
    _pop([
        "ideias",
        "ideias_originais",
        "modo_filtrado"
    ])


# =====================================================
# ETAPA 02 — CONCEITO
# =====================================================
def limpar_conceito():
    _pop([
        "conceito_visual"
    ])


# =====================================================
# ETAPA 03 — IMAGENS
# =====================================================
def limpar_imagens():
    _pop([
        "descricoes_imagem",
        "descricao_escolhida",
        "imagem_escolhida"
    ])


# =====================================================
# ETAPA 04 — TEXTO
# =====================================================
def limpar_texto():
    _pop([
        "legenda_gerada",
        "headline_escolhida"
    ])


# =====================================================
# ETAPA 05 — POSTAGEM
# =====================================================
def limpar_postagem():
    _pop([
        "imagem_final_bytes",
        "layout_final"
    ])


# =====================================================
# 🔥 LIMPEZA TOTAL (reset do fluxo inteiro)
# =====================================================
def limpar_fluxo_completo():

    limpar_ideias()
    limpar_conceito()
    limpar_imagens()
    limpar_texto()
    limpar_postagem()

    st.cache_data.clear()
