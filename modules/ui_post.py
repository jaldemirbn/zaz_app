# =====================================================
# zAz — MÓDULO 06
# ETAPA 06 - Post
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA — GERAR DESCRIÇÃO DO POST (DIREÇÃO DE ARTE)
# =====================================================

def _gerar_descricao_post(conceito, headline):

    prompt = f"""
Você é um designer gráfico sênior especialista em criação de posts profissionais para Instagram.

Seu papel NÃO é criar imagem nova.
Seu papel é atuar como diretor de arte e planejar a montagem do layout sobre a imagem existente.

REGRAS OBRIGATÓRIAS:
- escrever SOMENTE em português do Brasil
- NÃO criar nova imagem
- NÃO alterar a cena
- usar exatamente a descrição da imagem fornecida
- apenas descrever a MONTAGEM do post

Imagem base (fixa):
{conceito}

Headline escolhida:
{headline}

Tarefa:
Crie um briefing técnico e executável explicando como montar o post.

Descreva de forma prática, como instruções para um designer ou Canva.

Especifique obrigatoriamente:
- posição exata da headline (topo, centro, base, esquerda, direita)
- tamanho relativo do texto
- tipografia sugerida (moderna, serifada, elegante, minimalista etc)
- peso da fonte (bold, light, extra bold)
- cores do texto
- contraste com o fundo
- sombras, boxes, degradês ou overlays se necessário
- alinhamento
- hierarquia visual
- estilo estético (clean, premium, minimalista, sofisticado)
- equilíbrio e composição

Evite termos vagos como "bonito" ou "legal".
Seja técnico, específico e direto.

Retorne somente a descrição final do layout.
"""

    return gerar_texto(prompt).strip()


# =====================================================
# RENDER
# =====================================================

def render_etapa_post():

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>06. Criação do post</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # BOTÃO (AÇÃO MANUAL)
    # -------------------------------------------------
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

    # -------------------------------------------------
    # RESULTADO
    # -------------------------------------------------
    if st.session_state.get("descricao_post"):

        st.text_area(
            "Descrição do post",
            st.session_state["descricao_post"],
            height=400
        )
