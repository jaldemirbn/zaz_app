# =================================================
# OPÇÃO — USAR POST PRONTO
# =================================================
st.divider()
st.markdown("### Ou envie um post já pronto")

arquivo_pronto = st.file_uploader(
    "Upload do post final (opcional)",
    type=["png", "jpg", "jpeg", "mp4", "mov", "webm"],
    label_visibility="collapsed"
)

if arquivo_pronto:

    tipo = arquivo_pronto.type

    if tipo.startswith("image"):
        st.image(arquivo_pronto, use_container_width=True)
        st.session_state["imagem_final_bytes"] = arquivo_pronto.read()

    elif tipo.startswith("video"):
        st.video(arquivo_pronto)
        st.session_state["imagem_final_bytes"] = arquivo_pronto.read()

    st.success("Post carregado ✓")

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

    return  # 🔥 para o resto do canvas antigo
