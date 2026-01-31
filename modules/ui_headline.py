# =====================================================
# zAz — MÓDULO HEADLINE
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA
# -------------------------------------------------
def _gerar_headlines(tema, ideias):

    prompt = f"""
Você é um copywriter sênior.

Tema:
{tema}

Ideias:
{ideias}

Crie 5 headlines curtas, fortes e chamativas em português.

Retorne uma por linha.
"""

    resposta = gerar_texto(prompt)

    return [h.strip() for h in resposta.split("\n") if h.strip()]


# -------------------------------------------------
# RENDER
# -------------------------------------------------
def render_etapa_headline():

    # 🔒 GATE CORRIGIDO (ANTES era etapa_4_liberada)
    if not st.session_state.get("modo_filtrado"):
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>02 • Headline</h3>",
        unsafe_allow_html=True
    )

    tema = st.session_state.get("tema")
    ideias = st.session_state.get("ideias")


    # -------------------------------------------------
    # GERAR
    # -------------------------------------------------
    if st.button("✨ Gerar headline", use_container_width=True):

        with st.spinner("Gerando headlines..."):
            st.session_state["headlines"] = _gerar_headlines(tema, ideias)
            st.session_state["headline_escolhida"] = None


    # -------------------------------------------------
    # LISTA NORMAL
    # -------------------------------------------------
    if "headlines" in st.session_state:

        escolha = st.radio(
            "Escolha a headline:",
            st.session_state["headlines"],
            index=None,
            key="radio_headline"
        )

        if escolha:
            st.session_state["headline_escolhida"] = escolha
