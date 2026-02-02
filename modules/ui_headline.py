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

Crie 5 headlines curtas e fortes em português.
Retorne uma por linha.
"""

    resposta = gerar_texto(prompt)
    return [h.strip() for h in resposta.split("\n") if h.strip()]


# -------------------------------------------------
# RENDER
# -------------------------------------------------
def render_etapa_headline():

    # aparece só depois das ideias
    if not st.session_state.get("modo_filtrado"):
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>03. Headline</h3>",
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
    # RADIO (layout original + invisível imediato)
    # -------------------------------------------------
    if "headlines" in st.session_state:

        headlines = st.session_state["headlines"]
        escolhida = st.session_state.get("headline_escolhida")

        opcoes = [escolhida] if escolhida else headlines

        escolha = st.radio(
            "Escolha a headline:",
            opcoes,
            index=0 if escolhida else None,
            key="radio_headline"
        )

        # 🔥 CORREÇÃO PRINCIPAL AQUI
        if escolha and not escolhida:
            st.session_state["headline_escolhida"] = escolha
            st.rerun()


        # -------------------------------------------------
        # RESET
        # -------------------------------------------------
        if escolhida:
            if st.button("🔁 Escolher outra headline", use_container_width=True):
                st.session_state["headline_escolhida"] = None
                st.rerun()
