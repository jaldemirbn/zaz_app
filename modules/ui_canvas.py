import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


# =====================================================
# CROP CENTRAL POR PROPORÇÃO
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
        return img.crop((0, offset, w, offset + new_h))


# =====================================================
# RENDER CANVAS
# =====================================================
def render_etapa_canvas():

    if "imagem_bytes" not in st.session_state:
        return

    st.markdown("### 07. Canvas do post")

    base_img = Image.open(
        io.BytesIO(st.session_state["imagem_bytes"])
    ).convert("RGBA")


    # =================================================
    # FORMATO
    # =================================================
    formato = st.selectbox(
        "Formato",
        ["Original", "1:1", "4:5", "9:16", "16:9", "3:4"]
    )

    ratios = {
        "1:1": 1/1,
        "4:5": 4/5,
        "9:16": 9/16,
        "16:9": 16/9,
        "3:4": 3/4
    }

    if formato != "Original":
        img = crop_aspect(base_img, ratios[formato])
    else:
        img = base_img.copy()


    # =================================================
    # TEXTO (AGORA MULTILINHA)
    # =================================================
    texto = st.text_area(
        "Texto (use Enter para quebrar linha)",
        st.session_state.get("headline_escolhida", ""),
        height=120
    )


    # =================================================
    # CONTROLES
    # =================================================
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        x = st.slider("X", 0, img.width, 40)

    with c2:
        y = st.slider("Y", 0, img.height, 40)

    with c3:
        tamanho = st.slider("Tamanho", 20, 200, 80)

    with c4:
        cor_texto = st.color_picker("Cor texto", "#FFFFFF")

    with c5:
        fonte_nome = st.selectbox(
            "Fonte",
            ["Sans", "Sans Bold", "Serif", "Serif Bold", "Mono", "Mono Bold"]
        )


    # =================================================
    # FUNDO DO TEXTO
    # =================================================
    usar_fundo = st.checkbox("Fundo atrás do texto", True)
    cor_fundo = st.color_picker("Cor fundo", "#000000")
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

    draw.multiline_text(
        (x, y),
        texto,
        font=font,
        fill=cor_texto,
        spacing=6
    )

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
