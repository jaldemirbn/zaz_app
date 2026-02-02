# =====================================================
# zAz — MÓDULO 06
# ETAPA 06 - Post
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA
# =====================================================

def _gerar_descricao_post(conceito, headline):

    prompt = f"""
Você é um designer gráfico profissional.

Planeje a montagem do post usando a imagem base.

Imagem:
{conceito}

Headline:
{headline}

Descreva tecnicamente:
posição, fonte, tamanho, cor, contraste e estilo.
"""

    return gerar_texto(prompt).strip()


# =====================================================
# RENDER
# =====================================================

def render_etapa_post():

    # 🔥 garante estado
    if "mostrar_canvas" not in st.session_state:
        st.session_state["mostrar_canvas"] = False


    st.markdown(
        "<h3 style='color:#FF9D28;'>06. Criação do post</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # GERAR DESCRIÇÃO
    # -------------------------------------------------
    if st.button("Criar descrição do post", use_container_width=True):

        conceito = st.session_state.get("conceito_visual")
        headline = st.session_state.get("headline_escolhida")

        if conceito and headline:
            with st.spinner("Criando descrição..."):
                st.session_state["descricao_post"] = _gerar_descricao_post(
                    conceito,
                    headline
                )


    # -------------------------------------------------
    # MOSTRA DESCRIÇÃO
    # -------------------------------------------------
    if st.session_state.get("descricao_post"):

        st.text_area(
            "Descrição do post",
            st.session_state["descricao_post"],
            height=300
        )

        # 🔥 BOTÃO CRÍTICO
        if st.button("Criar post", use_container_width=True):
            st.session_state["mostrar_canvas"] = True
            st.rerun()  # ← força render imediato
