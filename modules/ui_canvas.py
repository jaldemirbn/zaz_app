# =====================================================
# zAz — MÓDULO 06
# ETAPA 07 — CANVAS DO POST
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io


# =====================================================
# FUNÇÕES AUXILIARES
# =====================================================
def crop_aspect(img, ratio):
    w, h = img.size
    current = w / h

    if current > ratio:
        new_w = int(h * ratio)
        offset = (w - new_w) // 2
        return img.crop((offset, 0, offset + new_w, h))
    else:
        new_h = int(w * ratio)
        offset = (h - new_h) // 2
        return img.crop((0, offset, w, new_h + offset))


# =====================================================
# RENDER PRINCIPAL
# =====================================================
def render_etapa_canvas():

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )


    # =================================================
    # STATE BASE DA IMAGEM (NOVO — PASSO 1)
    # =================================================
    if "imagem_base" not in st.session_state:
        st.session_state.imagem_base = None

    # Alimenta imagem_base a partir do fluxo antigo (LEGADO)
    if st.session_state.imagem_base is None and "imagem_bytes" in st.session_state:
        st.session_state.imagem_base = st.session_state["imagem_bytes"]


    # =================================================
    # VALIDAÇÃO — SEM IMAGEM
    # =================================================
    if st.session_state.imagem_base is None:

        st.info("Envie uma imagem na etapa anterior para continuar.")

        st.divider()
        col1, col2 = st.columns(2)

        # -------------------------------------------------
        # BOTÃO — VOLTAR
        # -------------------------------------------------
        with col1:
            if st.button("⬅ Voltar", use_container_width=True):
                st.session_state.etapa = 5
                st.rerun()

        return


    # =================================================
    # PREPARAR IMAGEM BASE
    # =================================================
    base_img = Image.open(
        io.BytesIO(st.session_state.imagem_base)
    ).convert("RGBA")


    # =================================================
    # CONTROLES
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

    img = crop_aspect(base_img, ratios[formato]) if formato != "Original" else base_img.copy()


    texto = st.text_area(
        "Texto (use Enter para quebrar linha)",
        st.session_state.get("headline_escolhida", ""),
        height=120
    )


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


    usar_fundo = st.checkbox("Fundo atrás do texto", True)
    cor_fundo = st.color_picker("Cor fundo", "#000000")
    alpha = st.slider("Transparência", 0, 255, 140)


    # =================================================
    # DESENHO
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

    draw.multiline_text((x, y), texto, font=font, fill=cor_texto, spacing=6)

    preview = Image.alpha_composite(preview, overlay)


    # =================================================
    # PREVIEW + DOWNLOAD
    # =================================================
    st.image(preview, use_container_width=True)

    buffer = io.BytesIO()
    preview.convert("RGB").save(buffer, format="PNG")
    st.session_state["imagem_final_bytes"] = buffer.getvalue()

    st.download_button(
        "⬇️ Baixar post final",
        buffer.getvalue(),
        "post_final.png",
        "image/png",
        use_container_width=True
    )


    # =================================================
    # BOTÕES
    # =================================================
    st.divider()
    col1, col2 = st.columns(2)


    # -------------------------------------------------
    # BOTÃO — VOLTAR
    # -------------------------------------------------
    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 5
            st.rerun()


    # -------------------------------------------------
    # BOTÃO — PRÓXIMO
    # -------------------------------------------------
    with col2:
        if st.button("Próximo ➡", use_container_width=True):
            st.session_state.etapa = 7
            st.rerun()
