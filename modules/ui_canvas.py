# =====================================================
# zAz — MÓDULO 07
# ETAPA 07 — CANVAS DO POST
# =====================================================

# =====================================================
# IMPORTS
# =====================================================
import streamlit as st


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
        type=["png", "jpg", "jpeg", "mp4", "mov", "webm"],
        accept_multiple_files=False
    )

    if arquivo is not None:
        st.session_state.arquivo_upload = arquivo.read()
        st.session_state.tipo_upload = (
            "video" if arquivo.type.startswith("video") else "imagem"
        )

    # -------------------------------------------------
    # 4. FEEDBACK VISUAL (CONFIRMAÇÃO)
    # -------------------------------------------------
    if st.session_state.arquivo_upload is None:
        st.info("Envie uma imagem ou vídeo para continuar.")
    else:
        if st.session_state.tipo_upload == "video":
            st.success("Vídeo carregado com sucesso.")
            st.video(st.session_state.arquivo_upload)
        else:
            st.success("Imagem carregada com sucesso.")

    # -------------------------------------------------
    # 5. NAVEGAÇÃO (SEMPRE POR ÚLTIMO)
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
