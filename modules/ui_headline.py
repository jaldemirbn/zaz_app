# =====================================================
# zAz — MÓDULO 04
# ETAPA HEADLINE (RED LINE)
# =====================================================
# Função:
# - gerar headlines curtas com IA
# - usuário escolhe 1
# - salvar no session_state
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR HEADLINES
# -------------------------------------------------
def _gerar_headlines(base_texto: str):

    prompt = f"""
Com base no contexto abaixo, gere headlines curtas para Instagram.

Contexto:
{base_texto}

Regras obrigatórias:
- máximo 7 palavras
- frase única
- impacto forte
- linguagem direta
- estilo marketing
- sem explicações
- sem emojis
- sem pontuação longa

Retorne:
apenas uma lista numerada com 5 headlines.
"""

    resposta = gerar_texto(prompt)

    linhas = [l.strip("-• ").strip() for l in resposta.split("\n") if l.strip()]

    return linhas[:5]


# -------------------------------------------------
# RENDER
# -------------------------------------------------
def render_etapa_headline():

    # só aparece após imagem escolhida
    if not st.session_state.get("imagem_escolhida"):
        return

    st.markdown(
        "<h3 style='color:#FF9D28; margin-top:24px;'>05. Headline</h3>",
        unsafe_allow_html=True
    )

    if "headlines" not in st.session_state:
        st.session_state.headlines = []

    if "headline_escolhida" not in st.session_state:
        st.session_state.headline_escolhida = None

    # -------------------------------------------------
    # GERAR
    # -------------------------------------------------
    if st.button("Gerar headlines", use_container_width=True):

        base = st.session_state.get("conceito_visual", "")

        with st.spinner("Criando headlines..."):
            st.session_state.headlines = _gerar_headlines(base)

        st.session_state.headline_escolhida = None
        st.rerun()

    # -------------------------------------------------
    # LISTA
    # -------------------------------------------------
    if st.session_state.headlines:

        escolha = st.radio(
            "Escolha a headline:",
            st.session_state.headlines,
            index=None
        )

        if escolha:
            st.session_state.headline_escolhida = escolha

    # preview
    if st.session_state.headline_escolhida:
        st.success(f"Selecionada: {st.session_state.headline_escolhida}")
