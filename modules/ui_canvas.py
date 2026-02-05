base_canvas = aplicar_zoom_e_offset(
    base, cw, ch, zoom, offset_x, offset_y
)

# ---------- PREVIEW COM GRADE (só visual) ----------
preview_visual = base_canvas.copy()
preview_visual = desenhar_grade_tercos(preview_visual)

# ---------- FINAL SEM GRADE ----------
preview_final = base_canvas.copy()

font = carregar_fonte(fonte_nome, tamanho)
overlay = Image.new("RGBA", preview_visual.size, (0, 0, 0, 0))
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

preview_visual = Image.alpha_composite(preview_visual, overlay)
preview_final = Image.alpha_composite(preview_final, overlay)

# MOSTRA SÓ O VISUAL
st.image(preview_visual, use_container_width=True)

# SALVA SÓ O FINAL LIMPO
buffer = io.BytesIO()
preview_final.convert("RGB").save(buffer, format="PNG")

st.session_state["midia_final_bytes"] = buffer.getvalue()
st.session_state["midia_tipo"] = "imagem"
