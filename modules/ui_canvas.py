# =====================================================
# zAz — MÓDULO CANVAS INTERNO
# Editor visual do post (mini Canva interno)
# =====================================================

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


def render_etapa_canvas():

    # -------------------------------------------------
    # só renderiza se tiver imagem
    # -------------------------------------------------
    if "imagem_bytes" not in st.session_state:
        return


    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # CARREGA IMAGEM
    # -------------------------------------------------
    img = Image.open(io.BytesIO(st.session_state["imagem_bytes"]))


    # -------------------------------------------------
    # CONTROLES
    # -------------------------------------------------

    texto = st.text_input(
        "Texto",
        st.session_state.get("headline_escolhida", "")
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        x = st.slider("X", 0, img.width, 40)

    with col2:
        y = st.slider("Y", 0, img.height, 40)

    with col3:
        tamanho = st.slider("Tamanho", 20, 200, 80)

    with col4:
        cor = st.color_picker("Cor", "#FFFFFF")

    # -------------------------------------------------
    # FONTES SEGURAS (DejaVu family)
    # -------------------------------------------------

    with col5:
        fonte_nome = st.selectbox(
            "Fonte",
            [
                "Sans",
                "Sans Bold",
                "Serif",
                "Serif Bold",
                "Mono",
                "Mono Bold"
            ]
        )

    fontes = {
        "Sans": "DejaVuSans.ttf",
        "Sans Bold": "DejaVuSans-Bold.ttf",
        "Light": "DejaVuSans-ExtraLight.ttf",
        "Serif": "DejaVuSerif.ttf",
        "Serif Bold": "DejaVuSerif-Bold.ttf",
        "Mono": "DejaVuSansMono.ttf",
        "Mono Bold": "DejaVuSansMono-Bold.ttf"
    }

    font = ImageFont.truetype(fontes[fonte_nome], tamanho)


    # -------------------------------------------------
    # DESENHAR
    # -------------------------------------------------

    preview = img.copy()
    draw = ImageDraw.Draw(preview)

    # contorno preto para legibilidade
    contorno = 2

    for dx in range(-contorno, contorno + 1):
        for dy in range(-contorno, contorno + 1):
            draw.text((x + dx, y + dy), texto, font=font, fill="black")

    draw.text((x, y), texto, font=font, fill=cor)

    st.image(preview, use_container_width=True)


    # -------------------------------------------------
    # EXPORTAR
    # -------------------------------------------------

    buffer = io.BytesIO()
    preview.save(buffer, format="PNG")

    st.download_button(
        "⬇️ Baixar post final",
        buffer.getvalue(),
        "post_final.png",
        "image/png",
        use_container_width=True
    )
