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

    # escala para CABER no canvas (contain)
    scale_base = min(canvas_w / iw, canvas_h / ih)
    scale = scale_base * zoom

    new_w = int(iw * scale)
    new_h = int(ih * scale)

    img_resized = img.resize((new_w, new_h), Image.LANCZOS)

    # espaço livre
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
    # CONFIGURAÇÕES
    # -------------------------------------------------
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

    texto = st.text_area(
        "Texto (use Enter para quebrar linha)",
        st.session_state.get("headline_escolhida", ""),
        height=120
    )

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        x = st.slider("X", 0, 2000, 40)
    with c2:
        y = st.slider("Y", 0, 2000, 40)
    with c3:
        tamanho = st.slider("Tamanho", 20, 200, 80)
    with c4:
        cor_texto = st.color_picker("Cor texto", "#FFFFFF")
    with c5:
        fonte_nome = st.selectbox(
            "Fonte",
            ["Sans", "Sans Bold", "Serif", "Serif Bold", "Mono", "Mono Bold"]
        )

    usar_fundo = st.checkbox("Fundo atrás do texto", True)
    cor_fundo = st.color_picker("Cor fundo", "#000000")
    alpha = st.slider("Transparência", 0, 255, 140)

    if formato != "Original":
        st.markdown("**Ajuste de enquadramento (zoom sem corte)**")
        zoom = st.slider("Zoom", 1.0, 3.0, 1.0, 0.01)
        offset_x = st.slider("Mover horizontal", -1.0, 1.0, 0.0, 0.01)
        offset_y = st.slider("Mover vertical", -1.0, 1.0, 0.0, 0.01)
    else:
        zoom = 1.0
        offset_x = 0.0
        offset_y = 0.0

    # -------------------------------------------------
    # UPLOAD
    # -------------------------------------------------
    arquivo = st.file_uploader(
        "Envie o post (imagem ou vídeo)",
        type=["png", "jpg", "jpeg", "mp4", "mov", "webm"]
    )

    if arquivo is not None and arquivo.type.startswith("image"):

        base = Image.open(arquivo).convert("RGBA")

        if formato == "Original":
            preview = base.copy()
        else:
            cw, ch = tamanhos[formato]
            preview = aplicar_zoom_e_offset(
                base, cw, ch, zoom, offset_x, offset_y
            )
            preview = desenhar_grade_tercos(preview)

        font = carregar_fonte(fonte_nome, tamanho)
        overlay = Image.new("RGBA", preview.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(overlay)

        if texto.strip():
            bbox = d.multiline_textbbox((x, y), texto, font=font, spacing=6)
            pad = 20
            if usar_fundo:
                r = int(cor_fundo[1:3], 16)
                g = int(cor_fundo[3:5], 16)
                b = int(cor_fundo[5:7], 16)
                d.rectangle(
                    (bbox[0] - pad, bbox[1] - pad, bbox[2] + pad, bbox[3] + pad),
                    fill=(r, g, b, alpha)
                )
            d.multiline_text((x, y), texto, font=font, fill=cor_texto, spacing=6)

        preview = Image.alpha_composite(preview, overlay)

        st.image(preview, use_container_width=True)

        buffer = io.BytesIO()
        preview.convert("RGB").save(buffer, format="PNG")

        st.session_state["midia_final_bytes"] = buffer.getvalue()
        st.session_state["midia_tipo"] = "imagem"

        st.download_button(
            "⬇️ Baixar post final",
            buffer.getvalue(),
            "post_final.png",
            "image/png",
            use_container_width=True
        )

    # -------------------------------------------------
    # NAVEGAÇÃO
    # -------------------------------------------------
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 6
            st.rerun()

    with col2:
        if st.button("Seguir ➡", use_container_width=True):
            st.session_state.etapa = 8
            st.rerun()
