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

    # -------------------------------------------------
    # CAMPO FINAL DE LEGENDA (ÚNICO)
    # -------------------------------------------------
    st.text_area(
        "Legenda",
        value=st.session_state.legenda_final,
        height=300,
        key="legenda_final"
    )

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
    # NAVEGAÇÃO (CORRETA)
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
