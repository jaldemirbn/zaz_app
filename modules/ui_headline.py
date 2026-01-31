# =====================================================
# zAz — MÓDULO 04
# ETAPA HEADLINE
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR HEADLINES
# -------------------------------------------------
def _gerar_headlines(tema: str, ideias: list[str], conceito: str):

    ideias_txt = "\n".join(ideias)

    prompt = f"""
Você é um copywriter sênior de marketing.

Crie 3 headlines altamente persuasivas para Instagram.

Contexto:
Tema: {tema}
Ideias: {ideias_txt}
Imagem: {conceito}

Regras:
- máximo 7 palavras
- frase única
- impacto forte
- linguagem direta

Retorne lista numerada com 3 headlines.
"""

    resposta = gerar_texto(prompt)

    linhas = [l.strip("-• ").strip() for l in resposta.split("\n") if l.strip()]

    return linhas[:3]


# -------------------------------------------------
# RENDER
# -------------------------------------------------
def render_etapa_headline():

    if not st.session_state.get("etapa_4_liberada"):
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
    if st.button("Gerar Headline", use_container_width=True):

        tema = st.session_state.get("tema", "")
        ideias = st.session_state.get("ideias", [])
        conceito = st.session_state.get("conceito_visual", "")

        with st.spinner("Gerando..."):
            st.session_state.headlines = _gerar_headlines(
                tema,
                ideias,
                conceito
            )

        st.session_state.headline_escolhida = None
        st.rerun()

    # -------------------------------------------------
    # FILTRAGEM
    # -------------------------------------------------
    opcoes = st.session_state.headlines

    if st.session_state.headline_escolhida:
        opcoes = [st.session_state.headline_escolhida]

    # -------------------------------------------------
    # RADIO
    # -------------------------------------------------
    if opcoes:

        escolha = st.radio(
            "",
            opcoes,
            index=0 if st.session_state.headline_escolhida else None
        )

        # 🔥 AQUI É O SEGREDO (rerun imediato)
        if escolha and escolha != st.session_state.headline_escolhida:
            st.session_state.headline_escolhida = escolha
            st.rerun()
