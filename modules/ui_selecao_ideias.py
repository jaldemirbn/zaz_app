# =====================================================
# zAz — MÓDULO 02
# ETAPA 02 — Seleção de Ideias
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st


# =====================================================
# RENDER
# =====================================================
def render_etapa_selecao_ideias():

    # -----------------------------
    # STATE
    # -----------------------------
    if "ideias_originais" not in st.session_state:
        st.session_state.ideias_originais = []

    if "ideias_visiveis" not in st.session_state:
        st.session_state.ideias_visiveis = st.session_state.ideias_originais.copy()

    if "ideias_filtradas" not in st.session_state:
        st.session_state.ideias_filtradas = []


    # -----------------------------
    # TÍTULO
    # -----------------------------
    st.markdown(
        "<h3 style='color:#ff9d28;'>02. Escolha as ideias que quer usar</h3>",
        unsafe_allow_html=True
    )


    # =====================================================
    # CHECKBOXES (lista de ideias)
    # =====================================================
    selecionadas = []

    for ideia in st.session_state.ideias_visiveis:

        marcado = st.checkbox(
            ideia,
            key=f"ideia_{ideia}",
            value=ideia in st.session_state.ideias_filtradas
        )

        if marcado:
            selecionadas.append(ideia)


    # =====================================================
    # BOTÃO CONFIRMAR → filtra visualmente as ideias
    # =====================================================
    if st.button("Confirmar ideias", use_container_width=True):

        if selecionadas:
            st.session_state.ideias_filtradas = selecionadas
            st.session_state.ideias_visiveis = selecionadas
            st.success(f"{len(selecionadas)} ideias selecionadas ✓")
            st.rerun()
        else:
            st.warning("Selecione pelo menos uma ideia.")


    # =====================================================
    # BOTÃO MOSTRAR IDEIAS → restaura lista completa
    # =====================================================
    if st.session_state.ideias_visiveis != st.session_state.ideias_originais:

        if st.button("Mostrar ideias"):
            st.session_state.ideias_visiveis = st.session_state.ideias_originais.copy()
            st.rerun()


    # =====================================================
    # NAVEGAÇÃO (SEMPRE POR ÚLTIMO)
    # =====================================================
    st.divider()

    col1, col2 = st.columns(2)


    # =====================================================
    # BOTÃO VOLTAR → retorna para etapa 1 (tema)
    # =====================================================
    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 1
            st.rerun()


    # =====================================================
    # BOTÃO SEGUIR → avança para etapa 3 (headline)
    # =====================================================
    with col2:
        if st.button(
            "Seguir ➜",
            use_container_width=True,
            disabled=not st.session_state.ideias_filtradas
        ):
            st.session_state.etapa = 3
            st.rerun()
