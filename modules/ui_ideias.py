# =====================================================
# 🔒 ARQUITETURA SEQUENCIAL — REGRA GLOBAL DO zAz
# =====================================================
# Este módulo é o PONTO DE ENTRADA do sistema.
#
# Filosofia do fluxo:
# 01 Ideias      → raiz (sempre aparece)
# 02 Conceito    → depende das ideias confirmadas
# 03 Imagens     → depende do conceito
# 04/05 Headline → depende da imagem escolhida
# 06 Post        → depende da headline
# 07 Legenda     → depende do post
#
# Dentro deste módulo:
# - Etapa 01 → gerar ideias (livre)
# - Etapa 02 → só aparece após gerar ideias
# - Etapa 03 → apenas prepara estados internos
#
# Somente quando:
#     st.session_state.modo_filtrado == True
# os próximos módulos são liberados.
#
# ⚠️ IMPORTANTE:
# Este é o único módulo independente do app.
# NÃO criar dependência anterior aqui.
# =====================================================


# =====================================================
# zAz — MÓDULO 01
# ETAPA IDEIAS
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_ideias


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
    # INPUT + BOTÃO (AGORA COM FORM → ENTER FUNCIONA)
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


        # -------------------------------------------------
        # GERAR (fica dentro do form)
        # -------------------------------------------------
        if gerar and tema:

            with st.spinner("Gerando ideias..."):
                resposta = gerar_ideias(tema)

            ideias = [i.strip() for i in resposta.split("\n") if i.strip()]

            st.session_state.ideias = ideias
            st.session_state.ideias_originais = ideias.copy()
            st.session_state.modo_filtrado = False


	
    # -------------------------------------------------
    # LIMPAR (NOVO)
    # -------------------------------------------------
    col_space, col_reset = st.columns([7, 2], gap="small")

    with col_reset:
        if st.button("Limpar", use_container_width=True):
            st.session_state.clear()
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
# NAVEGAÇÃO WIZARD (🔥 apenas acrescentado)
# =================================================
st.divider()

if st.button("Prosseguir ➡", use_container_width=True):

    if not st.session_state.get("modo_filtrado"):
        st.warning("Escolha pelo menos uma ideia primeiro.")
    else:
        st.session_state.etapa = 2
        st.rerun()

# -------------------------------------------------
# ETAPA 03 (LÓGICA SOMENTE - NÃO RENDERIZA)
# -------------------------------------------------
def preparar_etapa_imagens():

    if "descricoes_imagem" not in st.session_state:
        st.session_state.descricoes_imagem = {}

    if "descricao_escolhida" not in st.session_state:
        st.session_state.descricao_escolhida = {}

