# =====================================================
# zAz — MÓDULO IMAGEM
# ETAPA 05 — COLAR/UPLOAD IMAGEM
# =====================================================

import streamlit as st
from PIL import Image
import io


# =====================================================
# RENDER PRINCIPAL
# =====================================================
def render_etapa_imagens():

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


    # =================================================
    # SEM IMAGEM → MOSTRA SÓ A TELA (NÃO SOME)
    # =================================================
    if not arquivo:
        st.info("Faça upload de uma imagem para continuar.")
        return


    # =================================================
    # PROCESSAR IMAGEM
    # =================================================
    img = Image.open(arquivo)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")

    st.session_state["imagem_bytes"] = buffer.getvalue()


    # -------------------------------------------------
    # PREVIEW
    # -------------------------------------------------
    st.image(img, use_container_width=True)


    # -------------------------------------------------
    # DOWNLOAD
    # -------------------------------------------------
    st.download_button(
        label="⬇️ Baixar imagem",
        data=buffer.getvalue(),
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


    # PRÓXIMO (post)
    with col2:
        if st.button("Próximo ➡", use_container_width=True):
            st.session_state.etapa = 5
            st.rerun()
