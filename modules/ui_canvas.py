# =====================================================
# zAz — MÓDULO 07
# ETAPA 07 — CANVAS DO POST
# =====================================================

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


# =====================================================
# HELPERS
# =====================================================
def crop_aspect(img, ratio):
    w, h = img.size
    current = w / h

    if current > ratio:
        new_w = int(h * ratio)
        offset = (w - new_w) // 2
        return img.crop((offset, 0, offset + new_w, h))
    else:
        new_h = int(w / ratio)
        offset = (h - new_h) // 2
        return img.crop((0, offset, w, new_h + offset))


# =====================================================
# RENDER
# =====================================================
def render_etapa_canvas():

    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )


    # =================================================
    # IMAGEM BASE (ORIGINAL)
    # =================================================
    imagem_base = st.session_state.get("imagem_bytes")

    if not imagem_base:
        st.info("Envie uma imagem na etapa anterior.")
        return


    # =================================================
    # UPLOAD OPCIONAL (SUBSTITUI IMAGEM)
    # =================================================
    st.divider()
    st.markdown("### (Opcional) Substituir pelo post pronto")

    arquivo_pronto = st.file_uploader(
        "Upload do post final",
        type=["png", "jpg", "jpeg", "mp4", "mov", "webm"],
        label_visibility="collapsed"
    )

    if arquivo_pronto:
        imagem_base = arquivo_pronto.read()

        if arquivo_pronto.type.startswith("image"):
            st.image(imagem_base, use_container_width=True)
        else:
            st.video(imagem_base)


    # =================================================
    # PROCESSAMENTO NORMAL (SEM RETURN)
    # =================================================
    base_img = Image.open(io.BytesIO(imagem_base)).convert("RGBA")


    texto = st.text_area(
        "Texto",
        st.session_state.get("headline_escolhida", ""),
        height=120
    )


    x = st.slider("X", 0, base_img.width, 40)
    y = st.slider("Y", 0, base_img.height, 40)
    tamanho = st.slider("Tamanho", 20, 200, 80)

    cor_texto = st.color_picker("Cor texto", "#FFFFFF")
    usar_fundo = st.checkbox("Fundo atrás do texto", True)
    cor_fundo = st.color_picker("Cor fundo", "#000000")
    alpha = st.slider("Transparência", 0, 255, 140)


    font = ImageFont.truetype("DejaVuSans-Bold.ttf", tamanho)

    preview = base_img.copy()
    overlay = Image.new("RGBA", preview.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    bbox = draw.multiline_textbbox((x, y), texto, font=font)
    padding = 20

    if usar_fundo:
        r = int(cor_fundo[1:3], 16)
        g = int(cor_fundo[3:5], 16)
        b = int(cor_fundo[5:7], 16)
        draw.rectangle(
            (bbox[0]-padding, bbox[1]-padding, bbox[2]+padding, bbox[3]+padding),
            fill=(r, g, b, alpha)
        )

    draw.multiline_text((x, y), texto, font=font, fill=cor_texto)

    preview = Image.alpha_composite(preview, overlay)

    st.image(preview, use_container_width=True)


    # =================================================
    # NAVEGAÇÃO
    # =================================================
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 6
            st.rerun()

    with col2:
        if st.button("Próximo ➜", use_container_width=True):
            st.session_state.etapa = 8
            st.rerun()
