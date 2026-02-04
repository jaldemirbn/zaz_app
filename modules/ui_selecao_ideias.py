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


    # -----------------------------
    # CHECKBOXES
    # -----------------------------
    selecionadas = []

    for ideia in st.session_state.ideias_visiveis:
        if st.checkbox(ideia, key=f"ideia_{ideia}"):
            selecionadas.append(ideia)


    # -----------------------------
    # CONFIRMAR (filtra visualmente)
    # -----------------------------
    if st.button("Confirmar ideias", use_container_width=True):

        if selecionadas:
            st.session_state.ideias_visiveis = selecionadas
            st.session_state.ideias_filtradas = selecionadas
            st.success(f"{len(selecionadas)} ideias selecionadas ✓")
            st.rerun()
        else:
            st.warning("Selecione pelo menos uma ideia.")


    # -----------------------------
    # MOSTRAR TODAS (restaura lista)
    # -----------------------------
    if st.session_state.ideias_visiveis != st.session_state.ideias_originais:
        if st.button("Mostrar ideias"):
            st.session_state.ideias_visiveis = st.session_state.ideias_originais.copy()
            st.session_state.ideias_filtradas = []
            st.rerun()


    # -----------------------------
    # NAVEGAÇÃO (SEMPRE ÚLTIMO)
    # -----------------------------
    st.divider()

    col1, col2 = st.columns(2)

    # 🔥 VOLTAR NÃO LIMPA NADA — SÓ NAVEGA
    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 1
            st.rerun()

    with col2:
        if st.button(
            "Seguir ➜",
            use_container_width=True,
            disabled=not st.session_state.ideias_filtradas
        ):
            st.session_state.etapa = 3
            st.rerun()
