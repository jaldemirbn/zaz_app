# =====================================================
# zAz — MÓDULO CANVAS INTERNO
# =====================================================

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


def render_etapa_canvas():

    # 🔥 só depende da imagem
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

    col1, col2 = st.columns(2)

    with col1:
        x = st.slider("X", 0, img.width, 40)

    with col2:
        y = st.slider("Y", 0, img.height, 40)

    tamanho = st.slider("Tamanho", 20, 200, 80)

    preview = img.copy()
    draw = ImageDraw.Draw(preview)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", tamanho)
    except:
        font = ImageFont.load_default()

    draw.text((x, y), texto, fill="white", font=font)

    st.image(preview, use_container_width=True)

    buffer = io.BytesIO()
    preview.save(buffer, format="PNG")

    st.download_button(
        "⬇️ Baixar post final",
        buffer.getvalue(),
        "post_final.png",
        "image/png",
        use_container_width=True
    )
