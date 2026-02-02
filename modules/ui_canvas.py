# =====================================================
# zAz — MÓDULO CANVAS INTERNO
# Preview + Texto sobre imagem + Exportar
# =====================================================

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


def render_etapa_canvas():

    if not st.session_state.get("imagem_escolhida"):
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )

    img = st.session_state["imagem_escolhida"]

    # -------------------------------------------------
    # CONTROLES
    # -------------------------------------------------

    headline = st.session_state.get("headline_escolhida", "")

    texto = st.text_input("Texto", headline)

    col1, col2 = st.columns(2)

    with col1:
        x = st.slider("Posição X", 0, img.width, 40)

    with col2:
        y = st.slider("Posição Y", 0, img.height, 40)

    tamanho = st.slider("Tamanho da fonte", 20, 200, 80)


    # -------------------------------------------------
    # DESENHAR
    # -------------------------------------------------

    preview = img.copy()
    draw = ImageDraw.Draw(preview)

    try:
        font = ImageFont.truetype("arial.ttf", tamanho)
    except:
        font = ImageFont.load_default()

    draw.text((x, y), texto, fill="white", font=font)

    st.image(preview, use_container_width=True)


    # -------------------------------------------------
    # EXPORTAR
    # -------------------------------------------------

    buffer = io.BytesIO()
    preview.save(buffer, format="PNG")

    st.download_button(
        "⬇️ Baixar post final",
        buffer.getvalue(),
        file_name="post_final.png",
        mime="image/png",
        use_container_width=True
    )
