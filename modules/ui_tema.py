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
    # STATES
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
    # FORM GERAR IDEIAS
    # -----------------------------
    with st.form("form_tema"):

        tema = st.text_input(
            "",
            placeholder="Sem ideia? Digita uma palavra. A gente cria o post.",
            label_visibility="collapsed"
        )

        gerar = st.form_submit_button("Gerar ideias", use_container_width=True)

        if gerar and tema:

            with st.spinner("Gerando ideias..."):
                resposta = gerar_ideias(tema)

            ideias = [i.strip() for i in resposta.split("\n") if i.strip()]

            st.session_state.ideias_originais = ideias

            # 🔥 ESSENCIAL → força redesenhar a tela
            st.rerun()


    # -----------------------------
    # BOTÃO SEGUIR (só aparece após gerar)
    # -----------------------------
    if st.session_state.ideias_originais:

        st.divider()

        if st.button("Seguir ➡", use_container_width=True):
            st.session_state.etapa = 2
            st.rerun()
