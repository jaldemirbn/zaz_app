# =====================================================
# zAz — MÓDULO 03
# ETAPA 04 — UPLOAD DE IMAGEM
# =====================================================
# Função:
# - aparece após etapa 3
# - usuário envia imagem criada externamente
# - salva no session_state
# - não gera nada
# - independente de conceito
# =====================================================

import streamlit as st
from PIL import Image


def render_etapa_imagens():

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28; margin-top:24px;'>04. Enviar imagem</h3>",
        unsafe_allow_html=True
    )

    st.caption("Faça upload da imagem criada no site.")

    # -------------------------------------------------
    # UPLOAD
    # -------------------------------------------------
    arquivo = st.file_uploader(
        "Selecionar imagem",
        type=["png", "jpg", "jpeg", "webp"],
        label_visibility="collapsed"
    )

    if not arquivo:
        return

    # -------------------------------------------------
    # CARREGAR IMAGEM
    # -------------------------------------------------
    img = Image.open(arquivo)

    st.image(img, use_column_width=True)

    # salvar estado
    st.session_state["imagem_escolhida"] = img
