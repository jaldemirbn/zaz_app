# =====================================================
# zAz — MÓDULO 08
# ETAPA 08 — LEGENDA (Copywriter IA)
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA — GERAR LEGENDA
# =====================================================

def _gerar_legenda(contexto, texto_usuario, tom):

    prompt = f"""
Você é um copywriter profissional especialista em Instagram.

MISSÃO:
Criar uma legenda envolvente, persuasiva e humana.

REGRAS OBRIGATÓRIAS:
- escrever em português do Brasil
- entre 3 e 7 linhas
- usar emojis estratégicos
- incorporar naturalmente o texto do usuário
- respeitar o tom solicitado
- incluir uma CTA clara no final (comentar, salvar, compartilhar, clicar no link, enviar direct etc)
- finalizar com hashtags relevantes

CONTEXTO DO POST:
Headline: {contexto.get("headline")}
Conceito visual: {contexto.get("conceito")}

TEXTO DO USUÁRIO:
{texto_usuario}

TOM DESEJADO:
{tom}

Gere apenas a legenda final.
"""

    return gerar_texto(prompt).strip()


# =====================================================
# RENDER
# =====================================================

def render_etapa_legenda():

    st.markdown(
        "<h3 style='color:#FF9D28;'>08. Legenda</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # CAMPO TEXTO LIVRE
    # -------------------------------------------------

    texto_usuario = st.text_area(
        "O que você gostaria de colocar na legenda?",
        height=100
    )


    # -------------------------------------------------
    # TOM (temporário — você pode ajustar depois)
    # -------------------------------------------------

    tom = st.selectbox(
        "Tom da legenda",
        [
            "Profissional",
            "Inspirador",
            "Autoridade",
            "Descontraído",
            "Urgente",
            "Emocional",
            "Vendas"
        ]
    )


    # -------------------------------------------------
    # BOTÃO GERAR
    # -------------------------------------------------

    if st.button("Criar legenda", use_container_width=True):

        contexto = {
            "headline": st.session_state.get("headline_escolhida", ""),
            "conceito": st.session_state.get("conceito_visual", "")
        }

        with st.spinner("Escrevendo legenda..."):
            st.session_state["legenda_gerada"] = _gerar_legenda(
                contexto,
                texto_usuario,
                tom
            )


    # -------------------------------------------------
    # RESULTADO
    # -------------------------------------------------

    if st.session_state.get("legenda_gerada"):

        st.text_area(
            "Legenda pronta",
            st.session_state["legenda_gerada"],
            height=220
        )
