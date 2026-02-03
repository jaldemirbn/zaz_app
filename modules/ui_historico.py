# =====================================================
# zAz — MÓDULO HISTÓRICO (SUPABASE)
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
        return

    # =================================================
    # ESTADO VISIBILIDADE
    # =================================================
    if "mostrar_historico" not in st.session_state:
        st.session_state["mostrar_historico"] = False

    if st.button("📚 Histórico", use_container_width=True):
        st.session_state["mostrar_historico"] = not st.session_state["mostrar_historico"]

    if not st.session_state["mostrar_historico"]:
        return

    # =================================================
    # BUSCAR NO BANCO
    # =================================================
    res = (
        conectar()
        .table("posts")
        .select("*")
        .eq("email", email)
        .order("criado_em", desc=True)
        .execute()
    )

    posts = res.data

    if not posts:
        st.info("Nenhum post salvo ainda.")
        return

    # =================================================
    # TÍTULO
    # =================================================
    st.markdown(
        "<h3 style='color:#FF9D28;'>10. Histórico</h3>",
        unsafe_allow_html=True
    )

    # =================================================
    # LISTA
    # =================================================
    for i, post in enumerate(posts, start=1):

        with st.expander(f"Postagem #{i}"):

            # IMAGEM
            img_bytes = base64.b64decode(post["imagem_base64"])
            img = Image.open(io.BytesIO(img_bytes))
            st.image(img, use_container_width=True)

            # LEGENDA
            st.text_area(
                "Legenda",
                post["legenda"],
                height=200,
                key=f"hist_leg_{i}"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.download_button(
                    "⬇️ Baixar imagem",
                    img_bytes,
                    f"post_{i}.png",
                    "image/png",
                    use_container_width=True
                )

            with col2:
                st.download_button(
                    "⬇️ Baixar legenda",
                    post["legenda"],
                    f"legenda_{i}.txt",
                    "text/plain",
                    use_container_width=True
                )
