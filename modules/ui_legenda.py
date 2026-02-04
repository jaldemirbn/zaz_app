# =====================================================
# zAz — MÓDULO 08
# ETAPA 08 — LEGENDA DO POST
# =====================================================

# =====================================================
# IMPORTS
# =====================================================
import streamlit as st


# =====================================================
# RENDER
# =====================================================
def render_etapa_legenda():

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>08. Legenda do post</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # STATE
    # -------------------------------------------------
    if "legenda_final" not in st.session_state:
        st.session_state.legenda_final = ""

    if "legenda_base" not in st.session_state:
        st.session_state.legenda_base = ""

    # -------------------------------------------------
    # TEXTO BASE (VINDO DA ETAPA 06, SE EXISTIR)
    # -------------------------------------------------
    texto_base = st.session_state.get("descricao_post", "")

    if texto_base:
        st.caption("Texto base sugerido (editável)")
        st.text_area(
            "Base da legenda",
            value=texto_base,
            height=140,
            key="legenda_base"
        )

    # -------------------------------------------------
    # CAMPO FINAL DE LEGENDA
    # -------------------------------------------------
    st.text_area(
        "Legenda final",
        value=st.session_state.legenda_final,
        height=260,
        key="legenda_final"
    )

    # -------------------------------------------------
    # AÇÕES
    # -------------------------------------------------
    col_a, col_b = st.columns(2)

    with col_a:
        if st.button("Usar texto base", use_container_width=True):
            st.session_state.legenda_final = texto_base

    with col_b:
        if st.button("Limpar legenda", use_container_width=True):
            st.session_state.legenda_final = ""

    # -------------------------------------------------
    # PREVIEW (SÓ TEXTO)
    # -------------------------------------------------
    if st.session_state.legenda_final.strip():
        st.caption("Preview da legenda")
        st.code(
            st.session_state.legenda_final,
            language="text"
        )

    # -------------------------------------------------
    # NAVEGAÇÃO
    # -------------------------------------------------
    st.divider()
    col1, col2 = st.columns(2)

    # ⬅ VOLTAR → ETAPA 07 (CANVAS)
    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 7
            st.rerun()

    # ➡ PROSSEGUIR → ETAPA 09 (POSTAGEM)
    with col2:
        if st.button("Prosseguir ➡", use_container_width=True):
            if not st.session_state.legenda_final.strip():
                st.warning("Finalize a legenda antes de continuar.")
            else:
                st.session_state.etapa = 9
                st.rerun()
