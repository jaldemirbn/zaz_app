# =====================================================
# zAz — MÓDULO HISTÓRICO (SUPABASE)
# =====================================================

# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from supabase import create_client
import base64
import io
from PIL import Image


# =====================================================
# SUPABASE
# =====================================================
@st.cache_resource
def conectar():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


# =====================================================
# RENDER
# =====================================================
def render_etapa_historico():

    email = st.session_state.get("email")
    if not email:
        st.info("Usuário não autenticado.")
        return

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>Histórico de postagens</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # BUSCAR POSTS (COM LIMITE E PROTEÇÃO)
    # -------------------------------------------------
    try:
        res = (
            conectar()
            .table("posts")
            .select("*")
            .eq("email", email)
            .order("criado_em", desc=True)
            .limit(20)
            .execute()
        )
        posts = res.data or []
    except Exception:
        st.error("Erro ao carregar o histórico. Tente novamente.")
        return

    if not posts:
        st.info("Nenhum post salvo ainda.")
        return

    # -------------------------------------------------
    # LISTAGEM
    # -------------------------------------------------
    for i, post in enumerate(posts, start=1):

        with st.expander(f"Postagem #{i}"):

            imagem_base64 = post.get("imagem_base64")
            legenda = post.get("legenda", "")

            # -----------------------------
            # IMAGEM
            # -----------------------------
            if imagem_base64:
                try:
                    img_bytes = base64.b64decode(imagem_base64)
                    img = Image.open(io.BytesIO(img_bytes))
                    st.image(img, use_container_width=True)
                except Exception:
                    st.warning("Imagem indisponível.")
            else:
                st.warning("Imagem não encontrada.")

            # -----------------------------
            # LEGENDA (SOMENTE LEITURA)
            # -----------------------------
            st.text_area(
                "Legenda",
                legenda,
                height=200,
                disabled=True,
                key=f"hist_leg_{i}"
            )

            # -----------------------------
            # DOWNLOADS
            # -----------------------------
            col1, col2 = st.columns(2)

            with col1:
                if imagem_base64:
                    st.download_button(
                        "⬇️ Baixar imagem",
                        img_bytes,
                        f"post_{i}.png",
                        "image/png",
                        use_container_width=True
                    )

            with col2:
                if legenda:
                    st.download_button(
                        "⬇️ Baixar legenda",
                        legenda,
                        f"legenda_{i}.txt",
                        "text/plain",
                        use_container_width=True
                    )

    # -------------------------------------------------
    # VOLTAR AO APP
    # -------------------------------------------------
    st.divider()
    if st.button("⬅ Voltar para o app", use_container_width=True):
        st.session_state.etapa = 1
        st.rerun()
