# =====================================================
# zAz — MÓDULO 02
# ETAPA 03 — HEADLINE
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA — GERAÇÃO
# =====================================================
def _gerar_headlines(tema, ideias):

    prompt = f"""
Você é um copywriter sênior.

Tema:
{tema}

Ideias:
{ideias}

Crie 5 headlines curtas e fortes em português.
Retorne uma por linha.
"""

    resposta = gerar_texto(prompt)
    return [h.strip() for h in resposta.split("\n") if h.strip()]


# =====================================================
# RENDER PRINCIPAL
# =====================================================
def render_etapa_headline():

    # -------------------------------------------------
    # REGRA DE EXIBIÇÃO
    # -------------------------------------------------
    if not st.session_state.get("modo_filtrado"):
        return


    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>03. Headline</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # STATES
    # -------------------------------------------------
    tema = st.session_state.get("tema")
    ideias = st.session_state.get("ideias")


    # =================================================
    # BOTÃO — GERAR (permanece em cima)
    # =================================================
    if st.button("✨ Gerar headline", use_container_width=True):

        with st.spinner("Gerando headlines..."):
            st.session_state["headlines"] = _gerar_headlines(tema, ideias)
            st.session_state["headline_escolhida"] = None

        st.rerun()


    # =================================================
    # LISTA DE HEADLINES
    # =================================================
    if "headlines" not in st.session_state:
        return

    headlines = st.session_state["headlines"]
    escolhida = st.session_state.get("headline_escolhida")

    opcoes = [escolhida] if escolhida else headlines

    escolha = st.radio(
        "Escolha a headline:",
        opcoes,
        index=0 if escolhida else None,
        key="radio_headline"
    )

    if escolha and not escolhida:
        st.session_state["headline_escolhida"] = escolha
        st.rerun()


    # =================================================
    # BOTÕES INFERIORES (todos juntos)
    # =================================================
   st.divider()

espaco, centro = st.columns([1, 2])

with centro:
    col_voltar, col_prox = st.columns(2)

    with col_voltar:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 1
            st.rerun()

    with col_prox:
        if st.button("Próximo ➡", use_container_width=True):
            st.session_state.etapa = 3
            st.rerun()


    # TROCAR
    with col1:
        if escolhida:
            if st.button("🔁 Trocar", use_container_width=True):
                st.session_state["headline_escolhida"] = None
                st.rerun()


    # VOLTAR
    with col2:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 1
            st.rerun()


    # PRÓXIMO
    with col3:
        if st.button("Próximo ➡", use_container_width=True):
            st.session_state.etapa = 3
            st.rerun()
