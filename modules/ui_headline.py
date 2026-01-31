# =====================================================
# zAz — MÓDULO 04
# ETAPA HEADLINE
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR HEADLINES (COPY SENIOR)
# -------------------------------------------------
def _gerar_headlines(tema: str, ideias: list[str], conceito: str):

    ideias_txt = "\n".join(ideias)

    prompt = f"""
Você é um COPYWRITER SÊNIOR especialista em marketing digital.

Crie headlines altamente persuasivas para Instagram.

Contexto:

Tema:
{tema}

Ideias:
{ideias_txt}

Descrição da imagem:
{conceito}

Regras:
- gerar apenas 3 headlines
- máximo 7 palavras
- frase única
- impacto forte
- linguagem direta
- estilo marketing profissional
- sem explicações
- sem emojis

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
    # BOTÃO GERAR
    # -------------------------------------------------
    if st.button("Gerar Headline", use_container_width=True):

        tema = st.session_state.get("tema", "")
        ideias = st.session_state.get("ideias", [])
        conceito = st.session_state.get("conceito_visual", "")

        with st.spinner("Copywriting estratégico..."):
            st.session_state.headlines = _gerar_headlines(
                tema,
                ideias,
                conceito
            )

        st.session_state.headline_escolhida = None
        st.rerun()

    # -------------------------------------------------
    # LISTA (SÓ APARECE SE AINDA NÃO ESCOLHEU)
    # -------------------------------------------------
    if st.session_state.headlines and st.session_state.headline_escolhida is None:

        escolha = st.radio(
            "Escolha a headline:",
            st.session_state.headlines,
            index=None
        )

        if escolha:
            st.session_state.headline_escolhida = escolha
            st.rerun()

    # -------------------------------------------------
    # APÓS ESCOLHER → MOSTRA SÓ A SELECIONADA
    # -------------------------------------------------
    if st.session_state.headline_escolhida:
        st.success(f"Selecionada: {st.session_state.headline_escolhida}")
