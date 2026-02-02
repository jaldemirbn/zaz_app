# =====================================================
# zAz — MÓDULO CANVAS INTERNO
# Editor visual do post (mini Canva interno PRO)
# =====================================================

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


def render_etapa_canvas():

    if "imagem_bytes" not in st.session_state:
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )

    img = Image.open(io.BytesIO(st.session_state["imagem_bytes"])).convert("RGBA")


    # =================================================
    # CONTROLES
    # =================================================

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
        cor_texto = st.color_picker("Cor texto", "#FFFFFF")

    with col5:
        fonte_nome = st.selectbox(
            "Fonte",
            ["Sans", "Sans Bold", "Serif", "Serif Bold", "Mono", "Mono Bold"]
        )


    # -------------------------------------------------
    # FUNDO DO TEXTO (NOVO)
    # -------------------------------------------------

    col6, col7, col8 = st.columns(3)

    with col6:
        usar_fundo = st.checkbox("Fundo atrás do texto", True)

    with col7:
        cor_fundo = st.color_picker("Cor fundo", "#000000")

    with col8:
        alpha = st.slider("Transparência", 0, 255, 140)


    # =================================================
    # FONTES SEGURAS
    # =================================================

    fontes = {
        "Sans": "DejaVuSans.ttf",
        "Sans Bold": "DejaVuSans-Bold.ttf",
        "Serif": "DejaVuSerif.ttf",
        "Serif Bold": "DejaVuSerif-Bold.ttf",
        "Mono": "DejaVuSansMono.ttf",
        "Mono Bold": "DejaVuSansMono-Bold.ttf"
    }

    font = ImageFont.truetype(fontes[fonte_nome], tamanho)


    # =================================================
    # DESENHAR
    # =================================================

    preview = img.copy()
    overlay = Image.new("RGBA", preview.size, (0, 0, 0, 0))

    draw = ImageDraw.Draw(overlay)

    # mede texto
    bbox = draw.textbbox((x, y), texto, font=font)
    padding = 20

    if usar_fundo:
        r, g, b = tuple(int(cor_fundo[i:i+2], 16) for i in (1, 3, 5))

        draw.rectangle(
            (
                bbox[0] - padding,
                bbox[1] - padding,
                bbox[2] + padding,
                bbox[3] + padding
            ),
            fill=(r, g, b, alpha)
        )

    # contorno
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            draw.text((x + dx, y + dy), texto, font=font, fill="black")

    draw.text((x, y), texto, font=font, fill=cor_texto)

    preview = Image.alpha_composite(preview, overlay)

    st.image(preview, use_container_width=True)


    # =================================================
    # EXPORTAR
    # =================================================

    buffer = io.BytesIO()
    preview.convert("RGB").save(buffer, format="PNG")

    st.download_button(
        "⬇️ Baixar post final",
        buffer.getvalue(),
        "post_final.png",
        "image/png",
        use_container_width=True
    )
