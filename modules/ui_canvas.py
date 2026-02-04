# =====================================================
# zAz — MÓDULO 07
# ETAPA 07 — CANVAS DO POST
# Responsabilidade:
#   • montar layout manual OU
#   • receber post pronto (upload)
# =====================================================


# =====================================================
# IMPORTS
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

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>07. Canvas do post</h3>",
        unsafe_allow_html=True
    )


    # =================================================
    # STATES
    # =================================================
    imagem_base = st.session_state.get("imagem_bytes")
    imagem_final = st.session_state.get("imagem_final_bytes")


    # =================================================
    # =================================================
    # 🔥 MODO 1 — UPLOAD DO POST PRONTO
    # =================================================
    # =================================================
    st.divider()
    st.markdown("### 📤 Ou envie um post já pronto")

    arquivo_pronto = st.file_uploader(
        "Upload do post final",
        type=["png", "jpg", "jpeg", "mp4", "mov", "webm"],
        label_visibility="collapsed"
    )

    if arquivo_pronto:

        dados = arquivo_pronto.read()

        if arquivo_pronto.type.startswith("image"):
            st.image(dados, use_container_width=True)
        else:
            st.video(dados)

        st.session_state["imagem_final_bytes"] = dados

        _render_navegacao(voltar=6, proximo=8)
        return


    # =================================================
    # =================================================
    # 🔥 MODO 2 — CANVAS MANUAL (ORIGINAL)
    # =================================================
    # =================================================
    st.divider()
    st.markdown("### ✏️ Ou montar layout aqui dentro")


    # -------------------------------------------------
    # VALIDAÇÃO
    # -------------------------------------------------
    if not imagem_base:
        st.info("Envie uma imagem na etapa anterior.")
        _render_navegacao(voltar=5, proximo=None)
        return


    # -------------------------------------------------
    # BASE
    # -------------------------------------------------
    base_img = Image.open(io.BytesIO(imagem_base)).convert("RGBA")


    # -------------------------------------------------
    # CONTROLES
    # -------------------------------------------------
    formato = st.selectbox(
        "Formato",
        ["Original", "1:1", "4:5", "9:16", "16:9", "3:4"]
    )

    ratios = {
        "1:1": 1,
        "4:5": 4/5,
        "9:16": 9/16,
        "16:9": 16/9,
        "3:4": 3/4
    }

    img = crop_aspect(base_img, ratios[formato]) if formato != "Original" else base_img.copy()


    texto = st.text_area(
        "Texto",
        st.session_state.get("headline_escolhida", ""),
        height=120
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        x = st.slider("X", 0, img.width, 40)

    with col2:
        y = st.slider("Y", 0, img.height, 40)

    with col3:
        tamanho = st.slider("Tamanho", 20, 200, 80)


    cor_texto = st.color_picker("Cor texto", "#FFFFFF")
    usar_fundo = st.checkbox("Fundo atrás do texto", True)
    cor_fundo = st.color_picker("Cor fundo", "#000000")
    alpha = st.slider("Transparência", 0, 255, 140)


    # -------------------------------------------------
    # DESENHO
    # -------------------------------------------------
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", tamanho)

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


    # -------------------------------------------------
    # PREVIEW
    # -------------------------------------------------
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


    # -------------------------------------------------
    # NAVEGAÇÃO
    # -------------------------------------------------
    _render_navegacao(voltar=6, proximo=8)



# =====================================================
# COMPONENTE PADRÃO — NAVEGAÇÃO
# =====================================================
def _render_navegacao(voltar=None, proximo=None):

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if voltar and st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = voltar
            st.rerun()

    with col2:
        if proximo and st.button("Próximo ➜", use_container_width=True):
            st.session_state.etapa = proximo
            st.rerun()
