# =====================================================
# zAz — MÓDULO POSTAGEM
# ETAPA FINAL — POST COMPLETO (COPY)
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR LEGENDA
# -------------------------------------------------
def _gerar_postagem(tema, ideias, headline, conceito):

    ideias_txt = "\n".join(ideias)

    prompt = f"""
Você é um copywriter sênior especialista em Instagram.

Crie a melhor legenda possível para um post profissional.

Base estratégica:

Tema do post:
{tema}

Ideias:
{ideias_txt}

Headline:
{headline}

Conceito visual:
{conceito}

Objetivo:
- abrir com gancho forte
- linguagem humana e natural
- persuasiva
- gerar desejo/curiosidade
- conduzir para ação
- incluir CTA
- finalizar com hashtags relevantes

Estrutura:
Gancho
Texto principal persuasivo
CTA
5 a 10 hashtags

Regras:
- português brasileiro
- tom moderno profissional
- fluido
- sem texto robótico
- sem emojis excessivos

Retorne apenas a legenda final pronta.
"""

    return gerar_texto(prompt).strip()


# -------------------------------------------------
# RENDER
# -------------------------------------------------
def render_etapa_postagem():

    st.markdown(
        "<h3 style='color:#FF9D28;'>05 • Postagem</h3>",
        unsafe_allow_html=True
    )

    tema = st.session_state.get("tema")
    ideias = st.session_state.get("ideias")
    headline = st.session_state.get("headline_escolhida")
    conceito = st.session_state.get("conceito_visual")

    # 🔒 só depende de dados estratégicos (não imagem)
    if not (tema and ideias and headline and conceito):
        return


    # -------------------------------------------------
    # GERAR
    # -------------------------------------------------
    if st.button("✨ Gerar legenda", use_container_width=True):

        with st.spinner("Escrevendo legenda..."):
            st.session_state["post_legenda"] = _gerar_postagem(
                tema, ideias, headline, conceito
            )


    # -------------------------------------------------
    # EXIBIR
    # -------------------------------------------------
    if "post_legenda" in st.session_state:

        legenda = st.text_area(
            "Legenda pronta",
            st.session_state["post_legenda"],
            height=260
        )

        col1, col2 = st.columns(2)

        with col1:
            st.code(legenda, language="text")

        with col2:
            if st.button("🔁 Nova legenda", use_container_width=True):
                del st.session_state["post_legenda"]
                st.rerun()
