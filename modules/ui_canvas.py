# =====================================================
# zAz — MÓDULO CANVAS INTERNO
# =====================================================

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


def render_etapa_canvas():

    if not st.session_state.get("imagem_bytes"):
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )

    img = Image.open(io.BytesIO(st.session_state["imagem_bytes"]))

    texto = st.text_input(
        "Texto",
        st.session_state.get("headline_escolhida", "")
    )

    # 🔥 NOVO → cor da fonte
    cor = st.color_picker("Cor do texto", "#FFFFFF")


    margem = 150

    col1, col2 = st.columns(2)

    with col1:
        x = st.slider("X", 0, img.width - margem, 40)

    with col2:
        y = st.slider("Y", 0, img.height - margem, 40)

    tamanho = st.slider("Tamanho", 20, 200, 80)


    preview = img.copy()
    draw = ImageDraw.Draw(preview)

    font = ImageFont.truetype("DejaVuSans-Bold.ttf", tamanho)

    # contorno preto pra legibilidade
    contorno = 3

    for dx in range(-contorno, contorno + 1):
        for dy in range(-contorno, contorno + 1):
            draw.text((x + dx, y + dy), texto, font=font, fill="black")

    # 🔥 usa a cor escolhida
    draw.text((x, y), texto, fill=cor, font=font)

    st.image(preview, use_container_width=True)


    buffer = io.BytesIO()
    preview.save(buffer, format="PNG")

    st.download_button(
        "⬇️ Baixar post final",
        buffe
