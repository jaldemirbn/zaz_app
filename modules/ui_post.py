# =====================================================
# zAz — MÓDULO 06
# ETAPA 06 — POST
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA — GERAÇÃO DA DESCRIÇÃO
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
# LIMPEZA DA ETAPA
# =====================================================
def _limpar_post():
    st.session_state.pop("descricao_post", None)


# =====================================================
# RENDER PRINCIPAL
# =====================================================
def render_etapa_post():

    st.markdown(
        "<h3 style='color:#FF9D28;'>06. Criação do post</h3>",
        unsafe_allow_html=True
    )


    # =================================================
    # GERAR DESCRIÇÃO
    # =================================================
    if st.button("Criar descrição do post", use_container_width=True):

        conceito = st.session_state.get("conceito_visual")
        headline = st.session_state.get("headline_escolhida")

        if conceito and headline:
            with st.spinner("Criando descrição..."):
                st.session_state["descricao_post"] = _gerar_descricao_post(
                    conceito,
                    headline
                )


    # =================================================
    # MOSTRAR DESCRIÇÃO (🔥 copiar 1 clique)
    # =================================================
    if not st.session_state.get("descricao_post"):
        return


    st.code(
        st.session_state["descricao_post"],
        language="text"
    )


    # -------------------------------------------------
    # LINK CANVA
    # -------------------------------------------------
    st.link_button(
        "🎨 Criar post no Canva IA",
        "https://www.canva.com/ai",
        use_container_width=True
    )


    # =================================================
    # BOTÕES — 🔥 PADRÃO ORIGINAL DO PROJETO
    # =================================================
    st.divider()

    col1, col2 = st.columns(2)


    # ⬅ VOLTAR
    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            _limpar_post()
            st.session_state.etapa = 4
            st.rerun()


    # ➡ SEGUIR
    with col2:
        if st.button("Seguir ➡", use_container_width=True):
            st.session_state.etapa = 6
            st.rerun()
