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


    # =================================================
    # ESTADO VISIBILIDADE
    # =================================================
    if "mostrar_historico" not in st.session_state:
        st.session_state["mostrar_historico"] = False


    # =================================================
    # BOTÃO HISTÓRICO
    # =================================================
    if st.button("📚 Histórico", use_container_width=True):
        st.session_state["mostrar_historico"] = not st.session_state["mostrar_historico"]


    # =================================================
    # SE NÃO ABRIR → PARA AQUI
    # =================================================
    if not st.session_state["mostrar_historico"]:
        return


    # =================================================
    # TÍTULO
    # =================================================
    st.markdown(
        "<h3 style='color:#FF9D28;'>06 • Histórico</h3>",
        unsafe_allow_html=True
    )


    # =================================================
    # LIMPAR
    # =================================================
    if st.button("🗑 Limpar histórico", use_container_width=True):
        st.session_state["historico_posts"] = []
        st.session_state["mostrar_historico"] = False
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

            with col1:
                if st.button("↩ Usar novamente", key=f"reuse_{i}"):
                    st.session_state["postagem_final"] = texto
                    st.rerun()

            with col2:
                st.code(texto, language="text")
