# =====================================================
# zAz — MÓDULO MÍDIA
# ETAPA 04 — UPLOAD IMAGEM OU VÍDEO
# =====================================================

import streamlit as st
from PIL import Image
import io


# =====================================================
# RENDER PRINCIPAL
# =====================================================
def render_etapa_imagens():

    st.markdown(
        "<h3 style='color:#FF9D28; margin-top:0;'>05. Enviar mídia</h3>",
        unsafe_allow_html=True
    )

    st.caption("Envie uma imagem ou vídeo do seu computador.")


    # -------------------------------------------------
    # UPLOADER (🔥 SUPORTE A VÍDEO)
    # -------------------------------------------------
    arquivo = st.file_uploader(
        "Selecione ou arraste a mídia",
        type=["png", "jpg", "jpeg", "mp4", "mov", "webm"],
        label_visibility="collapsed"
    )


    # =================================================
    # SEM ARQUIVO → NÃO SOME A TELA
    # =================================================
    if not arquivo:
        st.info("Faça upload de uma imagem ou vídeo para continuar.")
        return


    tipo = arquivo.type


    # =================================================
    # IMAGEM
    # =================================================
    if tipo.startswith("image"):

        img = Image.open(arquivo)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")

        st.session_state["imagem_bytes"] = buffer.getvalue()
        st.session_state.pop("video_bytes", None)

        st.image(img, use_container_width=True)


    # =================================================
    # VÍDEO
    # =================================================
    elif tipo.startswith("video"):

        video_bytes = arquivo.read()

        st.session_state["video_bytes"] = video_bytes
        st.session_state.pop("imagem_bytes", None)

        st.video(video_bytes)


    # -------------------------------------------------
    # DOWNLOAD (somente para imagem)
    # -------------------------------------------------
    if "imagem_bytes" in st.session_state:

        st.download_button(
            label="⬇️ Baixar imagem",
            data=st.session_state["imagem_bytes"],
            file_name="post.png",
            mime="image/png",
            use_container_width=True
        )


    # =================================================
    # NAVEGAÇÃO
    # =================================================
    st.divider()
    col1, col2 = st.columns(2)


    # VOLTAR (conceito)
    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 3
            st.rerun()


    # SEGUIR
    with col2:
        if st.button("Seguir ➡", use_container_width=True):
            st.session_state.etapa = 5
            st.rerun()

