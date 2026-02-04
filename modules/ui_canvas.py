# =================================================
# UPLOAD OPCIONAL
# =================================================
st.divider()
st.markdown("### 📤 (Opcional) Substituir imagem pelo post pronto")

arquivo_pronto = st.file_uploader(
    "Upload do post final",
    type=["png", "jpg", "jpeg", "mp4", "mov", "webm"],
    label_visibility="collapsed"
)

# 🔥 DEFINE QUAL IMAGEM USAR
if arquivo_pronto:
    imagem_base = arquivo_pronto.read()

    if arquivo_pronto.type.startswith("image"):
        st.image(imagem_base, use_container_width=True)
    else:
        st.video(imagem_base)

    st.session_state["imagem_final_bytes"] = imagem_base

else:
    imagem_base = st.session_state.get("imagem_bytes")
