# =====================================================
# zAz — MÓDULO 09
# ETAPA 09 — POSTAGEM (Preview final)
# =====================================================

import streamlit as st
from PIL import Image
import io


def render_etapa_postagem():

    # só aparece se tiver imagem + legenda
    if "imagem_bytes" not in st.session_state:
        return

    if "legenda_gerada" not in st.session_state:
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>09. Postagem</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # PREVIEW IMAGEM
    # -------------------------------------------------

    img = Image.open(io.BytesIO(st.session_state["imagem_bytes"]))

    st.image(
        img,
        caption="Preview do post",
        use_container_width=True
    )


    # -------------------------------------------------
    # PREVIEW LEGENDA
    # -------------------------------------------------

    st.text_area(
        "Legenda final",
        st.session_state["legenda_gerada"],
        height=550
    )
