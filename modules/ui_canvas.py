# =====================================================
# zAz — MÓDULO CANVAS INTERNO
# Canvas PRO (texto + fontes + fundo + formatos)
# =====================================================

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


# =====================================================
# CROP CENTRAL POR PROPORÇÃO
# =====================================================
def crop_aspect(img, ratio):

    w, h = img.size
    target = ratio

    current = w / h

    if current > target:
        # corta largura
        new_w = int(h * target)
        offset = (w - new_w) // 2
        box = (offset, 0, offset + new_w, h)
    else:
        # corta altura
        new_h = int(w / target)
        offset = (h - new_h) // 2
        box = (0, offset, w, offset + new_h)

    return img.crop(box)


# =====================================================
# RENDER
# =====================================================
def render_etapa_canvas():

    if "imagem_bytes" not in st.session_state:
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )

    base_img = Image.open(
        io.BytesIO(st.session_state["imagem_bytes"])
    ).convert("RGBA")

    # =================================================
    # FORMATO (NOVO)
    # =================================================

    formato = st.selectbox(
        "Formato do post",
        [
            "Original",
            "1:1 (Quadrado)",
            "4:5 (Instagram Feed)",
            "9:16 (Stories/Reels)",
            "16:9 (Paisagem)",
            "3:4 (Retrato)"
        ]
    )

    ratios = {
        "1:1 (Quadrado)": 1/1,
        "4:5 (Instagram Feed)": 4/5,
        "9:16 (Stories/Reels)": 9/16,
        "16:9 (Paisagem)": 16/9,
        "3:4 (Retrato)": 3/4
    }

    if formato != "Original":
        img = crop_aspect(base_img, ratios[formato])
    else:
        img = base_img.copy()


    # =================================================
    # CONTROLES TEXTO
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

    # =================================================
    # FUNDO TEXTO
    # =================================================

    usar_fundo = st.checkbox("Fundo atrás do texto", True)
    cor_fundo = st.color_picker("Cor fundo", "#000000")
    alpha = st.slider("Transparência", 0, 255, 140)


    # =================================================
    # FONTES
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

    bbox = draw.textbbox((x, y), texto, font=font)
    padding = 20

    if usar_fundo:
        r, g, b = tuple(int(cor_fundo_
