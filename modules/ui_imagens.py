# =====================================================
# zAz — MÓDULO 05
# ETAPA 05 — IMAGEM (UPLOAD)
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from PIL import Image
import io


# =====================================================
# RENDER
# =====================================================
def render_etapa_imagens():

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>05. Enviar imagem ou vídeo</h3>",
        unsafe_allow_html=True
    )

    st.caption(
        "Envie a imagem criada no ImageFX ou qualquer mídia salva no seu dispositivo."
    )


    # =================================================
    # UPLOAD
    # =================================================
    arquivo = st.file_uploader(
        "Selecione ou arraste a mídia",
        type=["png", "jpg", "jpeg", "mp4", "mov", "webm"],
        label_visibility="collapsed"
    )


    # =================================================
    # PREVIEW + SALVAR
    # =================================================
    if arquivo:

        tipo = arquivo.type


        # -------------------------
        # IMAGEM
        # -------------------------
        if tipo.startswith("image"):

            img = Image.open(arquivo)

            buffer = io.BytesIO()
            img.save(buffer, format="PNG")

            st.session_state["imagem_bytes"] = buffer.getvalue()
            st.session_state.pop("video_bytes", None)

            st.image(img, use_container_width=True)


        # -------------------------
        # VÍDEO
        # -------------------------
        elif tipo.startswith("video"):

            video_bytes = arquivo.read()

            st.session_state["video_bytes"] = video_bytes
            st.session_state.pop("imagem_bytes", None)

            st.video(video_bytes)


    else:
        st.info("Faça upload para continuar.")
        return


    # =================================================
    # NAVEGAÇÃO
    # =================================================
    st.divider()
    col1, col2 = st.columns(2)


    # ⬅ VOLTAR
    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa -= 1
            st.rerun()


    # ➡ SEGUIR
    with col2:
        if st.button("Seguir ➜", use_container_width=True):
            st.session_state.etapa += 1
            st.rerun()
