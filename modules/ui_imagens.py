# =====================================================
# zAz — MÓDULO IMAGEM
# ETAPA 04 — COLAR/UPLOAD IMAGEM
# =====================================================

import streamlit as st
from PIL import Image
import io


def render_etapa_imagens():

    if not st.session_state.get("etapa_4_liberada"):
        return

    st.markdown(
        "<h3 style='color:#FF9D28; margin-top:0;'>05. Colar imagem</h3>",
        unsafe_allow_html=True
    )

    st.caption("Cole ou selecione a imagem do seu computador.")

    # -------------------------------------------------
    # UPLOAD
    # -------------------------------------------------
    arquivo = st.file_uploader(
        "Selecione ou arraste a imagem",
        type=["png", "jpg", "jpeg"],
        label_visibility="collapsed"
    )

    # -------------------------------------------------
    # SÓ RENDERIZA SE EXISTIR (SEM RETURN)
    # -------------------------------------------------
    if arquivo:

        img = Image.open(arquivo)

        # PREVIEW
        st.image(img, use_container_width=True)

        # DOWNLOAD
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")

        st.download_button(
            label="⬇️ Baixar imagem",
            data=buffer.getvalue(),
            file_name="post.png",
            mime="image/png",
            use_container_width=True
        )
