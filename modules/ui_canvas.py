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
# HELPERS / LÓGICA PURA
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
    # 2. STATES
    # -------------------------------------------------
    if "arquivo_upload" not in st.session_state:
        st.session_state.arquivo_upload = None

    if "tipo_upload" not in st.session_state:
        st.session_state.tipo_upload = None  # imagem | video

    # -------------------------------------------------
    # 3. UPLOAD (IMAGEM OU VÍDEO)
    # -------------------------------------------------
    arquivo = st.file_uploader(
        "Envie o post (imagem ou vídeo)",
        type=["png", "jpg", "jpeg", "mp4", "mov", "webm"]
    )

    if arquivo is not None:
        st.session_state.arquivo_upload = arquivo.read()
        st.session_state.tipo_upload = "video" if arquivo.type.startswith("video") else "imagem"

    if st.session_state.arquivo_upload is None:
        st.info("Envie um arquivo para continuar.")

        st.divider()
        col1, _ = st.columns(2)
        with col1:
            if st.button("⬅ Voltar", use_container_width=True):
                st.session_state.etapa = 6
                st.rerun()
        return

    # -------------------------------------------------
    # 4. FLUXO PARA VÍDEO
    # -------------------------------------------------
    if st.session_state.tipo_upload == "video":
        st.video(st.session_state.arquivo_upload)
        st.session_state["midia_final_bytes"] = st.session_state.arquivo_upload
        st.session_state["midia_tipo"] = "video"

    # -------------------------------------------------
    # 5. FLUXO PARA IMAGEM (CANVAS MANUAL)
    # -------------------------------------------------
    else:
        base_img = abrir_imagem_segura(st.session_state.arquivo_upload)

        if base_img is None:
            st.error("Arquivo inválido.")
            return

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

        font = carregar_fonte(fonte_nome, tamanho)

        preview = img.copy()
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
    # 6. NAVEGAÇÃO
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
