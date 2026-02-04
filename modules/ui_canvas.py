# =====================================================
# zAz — MÓDULO 07
# ETAPA 07 — UPLOAD DO POST FINAL
# Responsabilidade: receber arte pronta do usuário
# =====================================================

import streamlit as st


def render_etapa_canvas():

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Enviar post final</h3>",
        unsafe_allow_html=True
    )

    st.caption(
        "Depois de criar o post no Canva/CapCut/Adobe, envie o arquivo final aqui."
    )


    # =================================================
    # UPLOADER
    # =================================================
    arquivo = st.file_uploader(
        "Selecione o post pronto",
        type=["png", "jpg", "jpeg", "mp4", "mov", "webm"],
        label_visibility="collapsed"
    )


    # =================================================
    # PREVIEW
    # =================================================
    if arquivo:

        tipo = arquivo.type

        if tipo.startswith("image"):
            st.image(arquivo, use_container_width=True)
            st.session_state["post_final_bytes"] = arquivo.read()

        elif tipo.startswith("video"):
            st.video(arquivo)
            st.session_state["post_final_bytes"] = arquivo.read()


    # =================================================
    # NAVEGAÇÃO
    # =================================================
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 6
            st.rerun()

    with col2:
        if st.button(
            "Próximo ➜",
            use_container_width=True,
            disabled="post_final_bytes" not in st.session_state
        ):
            st.session_state.etapa = 8
            st.rerun()
