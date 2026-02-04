# =====================================================
# zAz — MÓDULO 01
# ETAPA 01 — Tema
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from modules.ia_engine import gerar_ideias


# =====================================================
# RENDER
# =====================================================
def render_etapa_tema():

    # -----------------------------
    # STATE
    # -----------------------------
    if "ideias_originais" not in st.session_state:
        st.session_state.ideias_originais = []


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
        "<h3 style='color:#ff9d28;'>01. O que você deseja postar hoje?</h3>",
        unsafe_allow_html=True
    )


    # -----------------------------
    # INPUT
    # -----------------------------
    tema = st.text_input(
        "",
        placeholder="Sem ideia? Digita uma palavra. A gente cria o post.",
        label_visibility="collapsed"
    )


    # -----------------------------
    # BOTÃO GERAR (SEM FORM)
    # -----------------------------
    if st.button("Gerar ideias", use_container_width=True):

        if tema:
            with st.spinner("Gerando ideias..."):
                resposta = gerar_ideias(tema)

            ideias = [i.strip() for i in resposta.split("\n") if i.strip()]

            st.session_state.ideias_originais = ideias


    # -----------------------------
    # BOTÃO SEGUIR (APARECE NA HORA)
    # -----------------------------
    if st.session_state.ideias_originais:

        st.divider()

        if st.button("Seguir ➡", use_container_width=True):
            st.session_state.etapa = 2
            st.rerun()
