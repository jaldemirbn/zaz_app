# =====================================================
# zAz — MÓDULO 05
# ETAPA HEADLINE
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA
# -------------------------------------------------
def _gerar_headlines(tema, ideias, conceito):

    prompt = f"""
Você é um copywriter sênior.

Tema:
{tema}

Ideias:
{ideias}

Descrição da imagem:
{conceito}

Crie 5 headlines curtas, fortes e chamativas.

Retorne uma por linha.
"""

    resposta = gerar_texto(prompt)

    return [h.strip() for h in resposta.split("\n") if h.strip()]


# -------------------------------------------------
# RENDER
# -------------------------------------------------
def render_etapa_headline():

    if not st.session_state.get("etapa_4_liberada"):
        return

    st.markdown("### 05 • Headline")

    tema = st.session_state.get("tema")
    ideias = st.session_state.get("ideias")
    conceito = st.session_state.get("conceito_visual")


    # -------------------------------------------------
    # GERAR
    # -------------------------------------------------
    if st.button("✨ Gerar headline", use_container_width=True):

        with st.spinner("Gerando headlines..."):
            st.session_state["headlines"] = _gerar_headlines(
                tema, ideias, conceito
            )
            st.session_state["headline_escolhida"] = None


    # -------------------------------------------------
    # LISTA
    # -------------------------------------------------
    if "headlines" in st.session_state:

        escolha = st.radio(
            "Escolha a headline:",
            st.session_state["headlines"],
            key="radio_headline"
        )

        st.session_state["headline_escolhida"] = escolha


        # -------------------------------------------------
        # BOTÕES (apenas após escolha)
        # -------------------------------------------------
        if st.session_state.get("headline_escolhida"):

            col1, col2 = st.columns(2)

            # reset
            with col1:
                if st.button("🔁 Escolher outra headline", use_container_width=True):
                    del st.session_state["headlines"]
                    del st.session_state["headline_escolhida"]
                    st.rerun()

            # novo botão solicitado
            with col2:
                if st.button(
                    "Criar descrição do post",
                    use_container_width=True,
                    key="btn_descricao_post"
                ):
                    st.session_state["criar_descricao_post"] = True
