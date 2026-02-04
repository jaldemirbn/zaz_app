# =====================================================
# 🔒 ARQUITETURA SEQUENCIAL — REGRA GLOBAL DO zAz
# =====================================================

# =====================================================
# zAz — MÓDULO 01
# ETAPA IDEIAS
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_ideias
from modules.state_manager import limpar_fluxo_completo  # 🔥 NOVO


def render_etapa_ideias():

    st.markdown(
        """
        <h3 style='color:#ff9d28; text-align:left; margin-bottom:8px;'>
        01. O que você deseja postar hoje?
        </h3>
        """,
        unsafe_allow_html=True
    )

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
    # INPUT + BOTÃO
    # -------------------------------------------------
    with st.form("form_gerar_ideias", clear_on_submit=False):

        col_input, col_btn = st.columns([7, 2], gap="small")

        with col_input:
            tema = st.text_input(
                "",
                placeholder="Sem ideia? Digita uma palavra. A gente cria o post.",
                label_visibility="collapsed"
            )

        with col_btn:
            gerar = st.form_submit_button(
                "Gerar ideias",
                use_container_width=True
            )

        if gerar and tema:

            with st.spinner("Gerando ideias..."):
                resposta = gerar_ideias(tema)

            ideias = [i.strip() for i in resposta.split("\n") if i.strip()]

            st.session_state.ideias = ideias
            st.session_state.ideias_originais = ideias.copy()
            st.session_state.modo_filtrado = False


    # -------------------------------------------------
    # LIMPAR (🔥 CORREÇÃO AQUI)
    # -------------------------------------------------
    col_space, col_reset = st.columns([7, 2], gap="small")

    with col_reset:
        if st.button("Limpar", use_container_width=True):
            limpar_fluxo_completo()  # 🔥 NÃO USA CLEAR()
            st.rerun()


    # -------------------------------------------------
    # ETAPA 02
    # -------------------------------------------------
    if st.session_state.ideias:

        st.markdown(
            """
            <h3 style='color:#ff9d28; text-align:left; margin-top:20px;'>
            02. Ideias para serem postadas
            </h3>
            """,
            unsafe_allow_html=True
        )

        selecionadas = []

        for ideia in st.session_state.ideias:
            marcado = st.checkbox(ideia, key=f"ideia_{ideia}")
            if marcado:
                selecionadas.append(ideia)

        if st.button("Ideias escolhidas"):
            if selecionadas:
                st.session_state.ideias = selecionadas
                st.session_state.modo_filtrado = True
                st.rerun()

        if st.session_state.ideias != st.session_state.ideias_originais:
            if st.button("Mostrar ideias"):
                st.session_state.ideias = st.session_state.ideias_originais.copy()
                for ideia in st.session_state.ideias_originais:
                    st.session_state.pop(f"ideia_{ideia}", None)
                st.session_state.modo_filtrado = False
                st.rerun()

        # =================================================
        # 🔥 PROSSEGUIR
        # =================================================
        st.divider()

        if st.button("Prosseguir ➡", use_container_width=True):

            if not st.session_state.get("modo_filtrado"):
                st.warning("Escolha pelo menos uma ideia primeiro.")
            else:
                st.session_state.etapa = 2
                st.rerun()


# -------------------------------------------------
# ETAPA 03 (LÓGICA)
# -------------------------------------------------
def preparar_etapa_imagens():

    if "descricoes_imagem" not in st.session_state:
        st.session_state.descricoes_imagem = {}

    if "descricao_escolhida" not in st.session_state:
        st.session_state.descricao_escolhida = {}
