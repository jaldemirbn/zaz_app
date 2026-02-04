# =====================================================
# zAz — MÓDULO 02
# ETAPA 02 — Seleção de Ideias
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from modules.state_manager import limpar_fluxo_completo


# =====================================================
# RENDER
# =====================================================
def render_etapa_selecao_ideias():

    # -----------------------------
    # STATES
    # -----------------------------
    if "ideias_originais" not in st.session_state:
        st.session_state.ideias_originais = []

    if "ideias_filtradas" not in st.session_state:
        st.session_state.ideias_filtradas = []

    ideias_base = (
        st.session_state.ideias_filtradas
        if st.session_state.ideias_filtradas
        else st.session_state.ideias_originais
    )


    # -----------------------------
    # CSS
    # -----------------------------
    st.markdown(
        """
        <style>
        div.stButton button p {
            color: #ff9d28 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------
    # TÍTULO
    # -----------------------------
    st.markdown(
        "<h3 style='color:#ff9d28;'>02. Ideias para serem postadas</h3>",
        unsafe_allow_html=True
    )


    # -----------------------------
    # RESULTADO (checkboxes)
    # -----------------------------
    selecionadas = []

    for ideia in ideias_base:
        marcado = st.checkbox(ideia, key=f"ideia_{ideia}")
        if marcado:
            selecionadas.append(ideia)


    # -----------------------------
    # BOTÃO PRINCIPAL (filtrar)
    # -----------------------------
    if st.button("Ideias escolhidas", use_container_width=True):
        if selecionadas:
            st.session_state.ideias_filtradas = selecionadas
            st.rerun()


    # -----------------------------
    # UTILITÁRIOS
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Mostrar todas"):
            st.session_state.ideias_filtradas = []
            st.rerun()

    with col2:
        if st.button("Limpar fluxo"):
            limpar_fluxo_completo()
            st.rerun()


    # -----------------------------
    # NAVEGAÇÃO
    # -----------------------------
    st.divider()

    if st.button("Seguir ➡", use_container_width=True):

        if not st.session_state.ideias_filtradas:
            st.warning("Escolha pelo menos uma ideia.")
        else:
            st.session_state.etapa = 3
            st.rerun()
