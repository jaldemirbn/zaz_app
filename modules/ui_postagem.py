# =====================================================
# zAz — MÓDULO POSTAGEM
# ETAPA 05 — POSTAGEM
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA
# -------------------------------------------------
def _gerar_postagem(tema, ideias, headline, conceito):

    ideias_txt = "\n".join(ideias)

    prompt = f"""
Você é um copywriter sênior especialista em Instagram.

Crie a legenda perfeita para um post.

Base:
Tema:
{tema}

Ideias:
{ideias_txt}

Headline:
{headline}

Conceito visual:
{conceito}

Objetivo:
- gancho forte na primeira linha
- texto persuasivo
- linguagem humana
- CTA claro
- hashtags relevantes

Português brasileiro.
Retorne somente a legenda final.
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

    # 🔒 só aparece se dados mínimos existirem
    if not (tema and ideias and headline and conceito):
        return


    # =================================================
    # BOTÃO CRIAR POSTAGEM
    # =================================================
    if st.button("✨ Criar postagem", use_container_width=True):

        with st.spinner("Gerando postagem..."):
            st.session_state["postagem_final"] = _gerar_postagem(
                tema, ideias, headline, conceito
            )


    # =================================================
    # EXIBIR RESULTADO
    # =================================================
    if "postagem_final" in st.session_state:

        st.text_area(
            "Postagem pronta",
            st.session_state["postagem_final"],
            height=260
        )

        if st.button("🔁 Criar novamente", use_container_width=True):
            del st.session_state["postagem_final"]
            st.rerun()
