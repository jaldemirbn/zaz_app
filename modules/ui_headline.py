# =====================================================
# zAz — MÓDULO 04
# ETAPA HEADLINE
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR HEADLINES (AGORA 5)
# -------------------------------------------------
def _gerar_headlines(tema: str, ideias: list[str], conceito: str):

    ideias_txt = "\n".join(ideias)

    prompt = f"""
Você é um copywriter sênior especialista em marketing digital.

Crie 5 headlines altamente persuasivas para Instagram.

Contexto:
Tema: {tema}
Ideias: {ideias_txt}
Imagem: {conceito}

Regras:
- máximo 7 palavras
- frase única
- impacto forte
- linguagem direta
- estilo marketing profissional
- parar o scroll

Retorne lista numerada com 5 headlines.
"""

    resposta = gerar_texto(prompt)

    linhas = [l.strip("-• ").strip() for l in resposta.split("\n") if l.strip()]

    return linhas[:5]


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

    # -------------------------------------------------
    # STATES
    # -------------------------------------------------
    if "headlines" not in st.session_state:
        st.session_state.headlines = []

    if "headline_escolhida" not in st.session_state:
        st.session_state.headline_escolhida = None

    # -------------------------------------------------
    # BOTÃO GERAR (5 headlines)
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
    # SE AINDA NÃO ESCOLHEU → MOSTRA TODAS
    # -------------------------------------------------
    if st.session_state.headline_escolhida is None:

        escolha = st.radio(
            "",
            st.session_state.headlines,
            index=None,
            key="headline_radio_full"
        )

        if escolha:
            st.session_state.headline_escolhida = escolha
            st.rerun()

    # -------------------------------------------------
    # SE JÁ ESCOLHEU → MOSTRA SÓ A ESCOLHIDA
    # -------------------------------------------------
    else:

        st.radio(
            "",
            [st.session_state.headline_escolhida],
            index=0,
            key="headline_radio_locked"
        )

        # 🔥 NOVO BOTÃO
        if st.button("Escolher outra headline", use_container_width=True):
            st.session_state.headline_escolhida = None
            st.rerun()
