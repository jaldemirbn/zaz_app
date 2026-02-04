# =====================================================
# zAz — MÓDULO 07
# ETAPA 07 — CANVAS DO POST
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
import io


# =====================================================
# FUNÇÕES AUXILIARES (LÓGICA PURA)
# =====================================================
def abrir_imagem_segura(imagem_bytes):
    if not imagem_bytes or not isinstance(imagem_bytes, (bytes, bytearray)):
        return None
    try:
        return Image.open(io.BytesIO(imagem_bytes)).convert("RGBA")
    except (UnidentifiedImageError, Exception):
        return None


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
    # STATE DA IMAGEM BASE
    # =================================================
    if "imagem_base" not in st.session_state:
        st.session_state.imagem_base = None

    # =================================================
    # UPLOAD DO POST PRONTO (SUBSTITUI IMAGEM BASE)
    # =================================================
    st.markdown("### 📤 Upload do post pronto")

    arquivo = st.file_uploader(
        "Envie o post criado fora do zAz (Canva, CapCut, Adobe, etc)",
        type=["png", "jpg", "jpeg"]
    )

    if arquivo is not None:
        st.session_state.imagem_base = arquivo.read()

    # =================================================
    # ABERTURA SEGURA DA IMAGEM
    # =================================================
    base_img = abrir_imagem_segura(st.session_state.imagem_base)

    if base_img is None:
        st.info("Faça upload de um post pronto para continuar.")

        st.divider()
        col1, _ = st.columns(2)

        with col1:
            if st.button("⬅ Voltar", use_container_width=True):
                st.session_state.etapa = 6
                st.rerun()

        return

    # =================================================
    # CONTROLES
    # =================================================
    texto = st.text_area(
        "Texto (use Enter para quebrar linha)",
        st.session_state.get("headline_escolhida", ""),
        height=120
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        x = st.slider("X", 0, base_img.width, 40)
    with c2:
        y = st.slider("Y", 0, base_img.height, 40)
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
                (bbox[0] - padding, bbox[1] - padding, bbox[2] + padding, bbox[3] + padding),
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
    # NAVEGAÇÃO
    # =================================================
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
