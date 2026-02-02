# =====================================================
# zAz — MÓDULO IMAGEM
# ETAPA 05 — COLAR/UPLOAD IMAGEM
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
    # RENDER
    # -------------------------------------------------
    if arquivo:

        img = Image.open(arquivo)

        # =================================================
        # 🔥 CORREÇÃO CRÍTICA
        # salvar BYTES (estável no session_state)
        # =================================================
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")

        st.session_state["imagem_bytes"] = buffer.getvalue()

        # PREVIEW
        st.image(img, use_container_width=True)

        # DOWNLOAD
        st.download_button(
            label="⬇️ Baixar imagem",
            data=buffer.getvalue(),
            file_name="post.png",
            mime="image/png",
            use_container_width=True
        )
