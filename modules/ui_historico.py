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


    # =================================================
    # BOTÃO LIMPAR
    # =================================================
    if st.button("🗑 Limpar histórico", use_container_width=True):
        st.session_state["historico_posts"] = []
        st.rerun()


    # =================================================
    # LISTA
    # =================================================
    for i, texto in enumerate(historico):

        numero = len(historico) - i

        with st.expander(f"Postagem #{numero}"):

            st.text_area(
                label="",
                value=texto,
                height=150,
                key=f"hist_{i}"
            )

            col1, col2 = st.columns(2)

            # -------------------------------------------------
            # USAR NOVAMENTE
            # -------------------------------------------------
            with col1:
                if st.button("↩ Usar novamente", key=f"reuse_{i}"):
                    st.session_state["postagem_final"] = texto
                    st.rerun()

            # -------------------------------------------------
            # COPIAR VISUAL
            # -------------------------------------------------
            with col2:
                st.code(texto, language="text")
