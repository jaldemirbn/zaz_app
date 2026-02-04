# =====================================================
# LAYOUT EM DUAS COLUNAS
# =====================================================
col_controles, col_preview = st.columns([1, 2])

# -----------------------------
# COLUNA ESQUERDA — CONTROLES
# -----------------------------
with col_controles:

    formato = st.selectbox(
        "Formato",
        ["Original", "1:1", "4:5", "9:16", "16:9"]
    )

    if formato != "Original":
        zoom = st.slider("Zoom", 1.0, 6.0, 1.0, 0.01)
        offset_x = st.slider("Mover horizontal", -1.0, 1.0, 0.0, 0.01)
        offset_y = st.slider("Mover vertical", -1.0, 1.0, 0.0, 0.01)
    else:
        zoom = 1.0
        offset_x = offset_y = 0.0

    texto = st.text_area(
        "Texto",
        st.session_state.get("headline_escolhida", ""),
        height=120
    )

    tamanho = st.slider("Tamanho da fonte", 20, 200, 80)
    fonte_nome = st.selectbox(
        "Fonte",
        ["Sans", "Sans Bold", "Serif", "Serif Bold", "Mono", "Mono Bold"]
    )

    cor_texto = st.color_picker("Cor do texto", "#FFFFFF")
    usar_fundo = st.checkbox("Fundo atrás do texto", True)
    cor_fundo = st.color_picker("Cor do fundo", "#000000")
    alpha = st.slider("Transparência", 0, 255, 140)

    arquivo = st.file_uploader(
        "Upload da imagem",
        type=["png", "jpg", "jpeg"]
    )

# -----------------------------
# COLUNA DIREITA — PREVIEW
# -----------------------------
with col_preview:

    if arquivo is not None:
        base = Image.open(arquivo).convert("RGBA")

        if formato != "Original":
            cw, ch = tamanhos[formato]
            preview = aplicar_zoom_e_offset(
                base, cw, ch, zoom, offset_x, offset_y
            )
            preview = desenhar_grade_tercos(preview)
        else:
            preview = base.copy()

        # texto + overlay (igual já está no seu código)
        font = carregar_fonte(fonte_nome, tamanho)
        overlay = Image.new("RGBA", preview.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(overlay)

        if texto.strip():
            bbox = d.multiline_textbbox((40, 40), texto, font=font, spacing=6)
            pad = 20
            if usar_fundo:
                r = int(cor_fundo[1:3], 16)
                g = int(cor_fundo[3:5], 16)
                b = int(cor_fundo[5:7], 16)
                d.rectangle(
                    (bbox[0]-pad, bbox[1]-pad, bbox[2]+pad, bbox[3]+pad),
                    fill=(r, g, b, alpha)
                )
            d.multiline_text((40, 40), texto, font=font, fill=cor_texto, spacing=6)

        preview = Image.alpha_composite(preview, overlay)

        st.image(preview, use_container_width=True)
