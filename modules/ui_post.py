# =====================================================
# zAz — MÓDULO 06
# ETAPA 06 - Post
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA — GERAR DESCRIÇÃO DO POST
# =====================================================

def _gerar_descricao_post(conceito, headline):

    prompt = f"""
Você é um designer gráfico sênior especialista em criação de posts para Instagram.

REGRAS OBRIGATÓRIAS:
- escrever SOMENTE em português do Brasil
- NÃO criar nova imagem
- NÃO alterar a cena
- usar exatamente a descrição da imagem fornecida
- apenas planejar a MONTAGEM do post

Descrição original da imagem (base fixa):
{conceito}

Headline escolhida:
{headline}

Tarefa:
Descrever como o post será montado visualmente, explicando:
- onde a headline será posicionada
- hierarquia visual
- contraste
- legibilidade
- composição
- equilíbrio do layout

Explique como a headline se encaixa na imagem existente.

Retorne somente a descrição final em português.
"""

    return gerar_texto(prompt).strip()


# =====================================================
# RENDER
# =====================================================

def render_etapa_post():

    if not st.session_state.get("criar_descricao_post"):
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>06. Post visual</h3>",
        unsafe_allow_html=True
    )

    if st.button(
        "Criar descrição do post",
        use_container_width=True,
        key="btn_criar_descricao_post"
    ):

        conceito = st.session_state.get("conceito_visual")
        headline = st.session_state.get("headline_escolhida")

        if conceito and headline:
            with st.spinner("Criando descrição..."):
                st.session_state["descricao_post"] = _gerar_descricao_post(
                    conceito,
                    headline
                )

    if st.session_state.get("descricao_post"):

        st.text_area(
            "Descrição do post",
            st.session_state["descricao_post"],
            height=400
        )

