# =====================================================
# zAz — MÓDULO 07
# ETAPA 07 — CANVAS DO POST
# =====================================================

# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
import io
from PIL import Image, ImageDraw, ImageFont


# =====================================================
# HELPERS / LÓGICA PURA
# =====================================================
def carregar_fonte(nome, tamanho):
    fontes = {
        "Sans": "DejaVuSans.ttf",
        "Sans Bold": "DejaVuSans-Bold.ttf",
        "Serif": "DejaVuSerif.ttf",
        "Serif Bold": "DejaVuSerif-Bold.ttf",
        "Mono": "DejaVuSansMono.ttf",
        "Mono Bold": "DejaVuSansMono-Bold.ttf"
    }
    try:
        return ImageFont.truetype(fontes[nome], tamanho)
    except Exception:
        return ImageFont.load_default()


def desenhar_grade_tercos(img, cor=(255, 255, 255, 120), largura=2):
    w, h = img.size
    d = ImageDraw.Draw(img)
    d.line((w / 3, 0, w / 3, h), fill=cor, width=largura)
    d.line((2 * w / 3, 0, 2 * w / 3, h), fill=cor, width=largura)
    d.line((0, h / 3, w, h / 3), fill=cor, width=largura)
    d.line((0, 2 * h / 3, w, 2 * h / 3), fill=cor, width=largura)
    return img


def aplicar_zoom_e_offset(img, canvas_w, canvas_h, zoom, offset_x, offset_y):
    """
    MODO CONTAIN
    - Nunca corta a imagem
    - zoom >= 1.0 aproxima
    - offset move dentro do espaço livre
    """
    iw, ih = img.size

    scale_base = min(canvas_w / iw, canvas_h / ih)
    scale = scale_base * zoom

    new_w = int(iw * scale)
    new_h = int(ih * scale)

    img_resized = img.resize((new_w, new_h), Image.LANCZOS)

    free_x = canvas_w - new_w
    free_y = canvas_h - new_h

    dx = int((free_x / 2) + offset_x * (free_x / 2))
    dy = int((free_y / 2) + offset_y * (free_y / 2))

    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    canvas.paste(img_resized, (dx, dy))

    return canvas


# =====================================================
# RENDER
# =====================================================
def render_etapa_canvas():

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # LAYOUT EM DUAS COLUNAS
    # -------------------------------------------------
    col_controles, col_preview = st.columns([1, 2])

    # =================================================
    # COLUNA ESQUERDA — CONTROLES
    # =================================================
    with col_controles:

        formato = st.selectbox(
            "Formato",
            ["Original", "1:1", "4:5", "9:16", "16:9"]
        )

        tamanhos = {
            "1:1": (1080, 1080),
            "4:5": (1080, 1350),
            "9:16": (1080, 1920),
            "16:9": (1920, 1080)
        }

        if formato != "Original":
            zoom = st.slider("Zoom", 1.0, 6.0, 1.0, 0.01)
            offset_x = st.slider("Mover horizontal", -1.0, 1.0, 0.0, 0.01)
            offset_y = st.slider("Mover vertical", -1.0, 1.0, 0.0, 0.01)
        else:
            zoom = 1.0
            offset_x = 0.0
            offset_y = 0.0

        texto = st.
