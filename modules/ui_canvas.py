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


def desenhar_grade_tercos(imagem, cor=(255, 255, 255, 120), largura=2):
    w, h = imagem.size
    draw = ImageDraw.Draw(imagem)
    x1, x2 = w / 3, 2 * w / 3
    y1, y2 = h / 3, 2 * h / 3
    draw.line((x1, 0, x1, h), fill=cor, width=largura)
    draw.line((x2, 0, x2, h), fill=cor, width=largura)
    draw.line((0, y1, w, y1), fill=cor, width=largura)
    draw.line((0, y2, w, y2), fill=cor, width=largura)
    return imagem


def recortar_com_offset(img, ratio, offset_x, offset_y):
    """
    Recorta mantendo o ratio, mas permite deslocar a janela de recorte
    com offsets normalizados (-1.0 a 1.0).
    """
    W, H = img.size
    current = W / H

    if current > ratio:
        # imagem larga → recorte vertical
        crop_h = H
        crop_w = int(H * ratio)
        max_dx = (W - crop_w) // 2
        dx = int(offset_x * max_dx)
        left = (W - crop_w) // 2 + dx
        top = 0
    else:
        # imagem alta → recorte horizontal
        crop_w = W
        crop_h = int(W / ratio)
        max_dy = (H - crop_h) // 2
        dy = int(offset_y * max_dy)
        left = 0
        top = (H - crop_h) // 2 + dy

    left = max(0, min(left, W - crop_w))
    top = max(0, min(top, H - crop_h))

    return img.crop((left, top, left + crop_w, top + crop_h))


# =====================================================
# RENDER
# =====================================================
def render_etapa_canvas():

    # -------------------------------------------------
    # 1. TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # 2. CONFIGURAÇÕES
    # -------------------------------------------------
    formato = st.selectbox(
        "Formato",
        ["Original", "1:1", "4:5", "9:16", "16:9", "3:4"]
    )

    ratios = {
        "1:1": 1 / 1,
        "4:5": 4 / 5,
        "9:16": 9 / 16,
        "16:9": 16 / 9,
        "3:4": 3 / 4
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

    # -------------------------------------------------
    # 3. AJUSTE MANUAL (REGRA DOS TERÇOS)
    # -------------------------------------------------
    if formato != "Original":
        st.markdown("**Ajuste manual do enquadramento (regra dos terços)**")
        offset_x = st.slider("Deslocamento horizontal", -1.0, 1.0, 0.0, 0.01)
        offset_y = st.slider("Deslocamento vertical", -1.0, 1.0, 0.0, 0.01)
    else:
        offset_x = offset_y = 0.0

    # -------------------------------------------------
    # 4. UPLOAD
    # -------------------------------------------------
    arquivo = st.file_uploader(
        "Envie o post (imagem ou vídeo)",
        type=["png", "jpg", "jpeg", "mp4", "mov", "webm"]
    )

    if arquivo is not None:

        # -----------------------------
        # IMAGEM
        # -----------------------------
        if arquivo.type.startswith("image"):
            base_img = Image.open(arquivo).convert("RGBA")

            if formato != "Original":
                base_img = recortar_com_offset(
                    base_img, ratios[formato], offset_x, offset_y
                )

            font = carregar_fonte(fonte_nome, tamanho)

            preview = base_img.copy()
            overlay = Image.new("RGBA", preview.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)

            if texto.strip():
                bbox = draw.multiline_textbbox((x, y), texto, font=font, spacing=6)
                padding = 20

                if usar_fundo:
                    r = int(cor_fundo[1:3], 16)
                    g = int(cor_fundo[3:5], 16)
                    b = int(cor_fundo[5:7], 16)
                    draw.rectangle(
                        (bbox[0]-padding, bbox[1]-padding, bbox[2]+padding, bbox[3]+padding),
                        fill=(r, g, b, alpha)
                    )

                draw.multiline_text((x, y), texto, font=font, fill=cor_texto, spacing=6)

            preview = Image.alpha_composite(preview, overlay)

            if formato != "Original":
                preview = desenhar_grade_tercos(preview)

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

        # -----------------------------
        # VÍDEO
        # -----------------------------
        else:
            st.video(arquivo)
            st.session_state["midia_final_bytes"] = arquivo.read()
            st.session_state["midia_tipo"] = "video"

    # -------------------------------------------------
    # 5. NAVEGAÇÃO
    # -------------------------------------------------
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 6
            st.rerun()

    with col2:
        if st.button("Próximo ➡", use_container_width=True):
            st.session_state.etapa = 8
            st.rerun()
