# =====================================================
# zAz — MÓDULO 07
# ETAPA 07 — CANVAS DO POST
# =====================================================

# =====================================================
# IMPORTS
# =====================================================
import streamlit as st


# =====================================================
# RENDER
# =====================================================
def render_etapa_canvas():

    # -------------------------------------------------
    # 1. TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # 2. CONTEÚDO (VÁZIO — BASE LIMPA)
    # -------------------------------------------------
    st.info("Etapa 07 (Canvas) iniciada. Estrutura base pronta.")

    # -------------------------------------------------
    # 3. NAVEGAÇÃO (SEMPRE POR ÚLTIMO)
    # -------------------------------------------------
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 6
            st.rerun()

    with col2:
        if st.button("Próximo ➡", use_container_width=True):
            st.session_state.etapa = 8
            st.rerun()
