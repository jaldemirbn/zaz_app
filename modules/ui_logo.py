import streamlit as st


# =========================================
# MÓDULO BRANDING — LOGO
# Responsabilidade única:
# renderizar a logomarca centralizada
# =========================================


def render_logo():

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        st.image("assets/logo.png", width=450)

    st.divider()

