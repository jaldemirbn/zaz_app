# =====================================================
# zAz — MÓDULO 01
# ETAPA 01 — Tema
# STATUS: CONGELADO
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from modules.ia_engine import gerar_ideias
from modules.state_manager import limpar_fluxo_completo


# =====================================================
# RENDER
# =====================================================
def render_etapa_tema():

    # -----------------------------
    # STATE
    # -----------------------------
    if "ideias_originais" not in st.session_state:
        st.session_state.ideias_originais = []

    if "tema" not in st.session_state:
        st.session_state.tema = ""


    # -----------------------------
    # TÍTULO
    # -----------------------------
    st.markdown(
        "<h3 style='color:#ff9d28;'>01. O que você deseja postar hoje?</h3>",
        unsafe_allow_html=True
    )


    # -----------------------------
    # INPUT (PERSISTENTE)
    # -----------------------------
    st.text_input(
        "",
        placeholder="Sem ideia? Digita uma palavra. A gente cria o post.",
        label_visibility="collapsed",
        key="tema"
    )

    tema = st.session_state.tema


    # -----------------------------
    # GERAR
    # -----------------------------
    if st.button("Gerar ideias", use_container_width=True):

        if tema:
            with st.spinner("Gerando ideias..."):
                resposta = gerar_ideias(tema)

            ideias = [i.strip() for i in resposta.split("\n") if i.strip()]
            st.session_state.ideias_originais = ideias


    # -----------------------------
    # RESULTADO
    # -----------------------------
    if st.session_state.ideias_originais:

        st.success("Ideias prontas. Pode seguir ➜")


        # -----------------------------
        # LIMPAR FLUXO (zera tudo)
        # -----------------------------
        if st.button("Limpar fluxo"):
            limpar_fluxo_completo()
            st.session_state.tema = ""   # 🔥 limpa texto também
            st.rerun()


        # -----------------------------
        # NAVEGAÇÃO
        # -----------------------------
        st.divider()

        if st.button("Seguir ➜", use_container_width=True):
            st.session_state.etapa = 2
            st.rerun()
