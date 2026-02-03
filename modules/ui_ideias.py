# =====================================================
# zAz — MÓDULO 01
# ETAPA IDEIAS (WIZARD PADRÃO)
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_ideias


def render_etapa_ideias():

    # -------------------------------------------------
    # COR PADRÃO BOTÕES
    # -------------------------------------------------
    st.markdown(
        """
        <style>
        div.stButton button p {
            color: #ff9d28 !important;
            font-weight: 600;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        """
        <h3 style='color:#ff9d28; text-align:left; margin-bottom:8px;'>
        01. O que você deseja postar hoje?
        </h3>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # STATE
    # -------------------------------------------------
    if "ideias" not in st.session_state:
        st.session_state.ideias = []

    if "ideias_originais" not in st.session_state:
        st.session_state.ideias_originais = []

    if "modo_filtrado" not in st.session_state:
        st.session_state.modo_filtrado = False

    # -------------------------------------------------
    # FORM
    # -------------------------------------------------
    with st.form("form_gerar_ideias"):

        col_input, col_btn = st.columns([7, 2])

        with col_input:
            tema = st.text_input(
                "",
                placeholder="Sem ideia? Digita uma palavra. A gente cria o post.",
                label_visibility="collapsed"
            )

        with col_btn:
            gerar = st.form_submit_button("Gerar ideias", use_container_width=True)

        if gerar and tema:
            with st.spinner("Gerando ideias..."):
                resposta = gerar_ideias(tema)

            ideias = [i.strip() for i in resposta.split("\n") if i.strip()]

            st.session_state.ideias = ideias
            st.session_state.ideias_originais = ideias.copy()
            st.session_state.modo_filtrado = False

    # -------------------------------------------------
    # LIMPAR
    # -------------------------------------------------
    if st.button("Limpar", use_container_width=True):
        st.session_state.clear()
        st.rerun()

    # -------------------------------------------------
    # LISTA
    # -------------------------------------------------
    if st.session_state.ideias:

        st.markdown(
            "<h3 style='color:#ff9d28;'>02. Ideias para serem postadas</h3>",
            unsafe_allow_html=True
        )

        selecionadas = []

        for ideia in st.session_state.ideias:
            if st.checkbox(ideia, key=f"ideia_{ideia}"):
                selecionadas.append(ideia)

        st.divider()

        # -------------------------------------------------
        # PRÓXIMO
        # -------------------------------------------------
        if st.button("Próximo ➡", use_container_width=True):

            if not selecionadas:
                st.warning("Selecione pelo menos uma ideia.")
                return

            st.session_state.ideias = selecionadas
            st.session_state.modo_filtrado = True
            st.session_state.etapa = 2
            st.rerun()
