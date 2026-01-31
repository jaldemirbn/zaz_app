# =====================================================
# zAz — MÓDULO HISTÓRICO
# ETAPA 06 — HISTÓRICO DE POSTAGENS
# =====================================================

import streamlit as st


# -------------------------------------------------
# RENDER
# -------------------------------------------------
def render_etapa_historico():

    historico = st.session_state.get("historico_posts", [])

    if not historico:
        return


    st.markdown(
        "<h3 style='color:#FF9D28;'>06 • Histórico</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # LISTA (máx 10 já vem controlado da postagem)
    # -------------------------------------------------
    for i, texto in enumerate(historico):

        numero = len(historico) - i

        with st.expander(f"Postagem #{numero}"):

            st.text_area(
                label="",
                value=texto,
                height=150,
                key=f"hist_{i}"
            )

