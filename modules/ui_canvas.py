# =====================================================
# zAz — MÓDULO CANVAS INTERNO
# Preview + Texto sobre imagem + Exportar
# =====================================================

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


def render_etapa_canvas():

    # -------------------------------------------------
    # SÓ APARECE DEPOIS DO BOTÃO "CRIAR POST"
    # -------------------------------------------------
    if not st.session_state.get("mostrar_canvas"):
        return

    if not st.session_state.get("imagem_escolhida"):
        return


    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )

    img = st.session_state["imagem_escolhida"]

    # -------------------------------------------------
    # CONTROLES
    # ----------------------------------------------
