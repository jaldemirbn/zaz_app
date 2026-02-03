import streamlit as st
from PIL import Image
import io
import base64
from supabase import create_client


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
# SALVAR NO BANCO
# =====================================================

def salvar_post():

    if "imagem_final_bytes" not in st.session_state:
        return

    if "legenda_gerada" not in st.session_state:
        return

    imagem_b64 = base64.b64encode(
        st.session_state["imagem_final_bytes"]
    ).decode()

    dados = {
        "email": st.session_state.get("email"),  # dono
        "headline": st.session_state.get("headline_escolhida", ""),
        "conceito": st.session_state.get("conceito_visual", ""),
        "legenda": st.session_state.get("legenda_gerada", ""),
        "imagem_base64": imagem_b64
    }

    conectar().table("posts").insert(dados).execute()


# =====================================================
# RENDER
# =====================================================

def render_etapa_postagem():

    st.markdown(
        "<h3 style='color:#FF9D28;'>09. Postagem</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # IMAGEM
    # -------------------------------------------------

    if "imagem_final_bytes" in st.session_state:

        img = Image.open(
            io.BytesIO(st.session_state["imagem_final_bytes"])
        )

        st.image(img, use_container_width=True)

    else:
        st.info("⚠️ Gere o Canvas para visualizar a imagem final.")

    # -------------------------------------------------
    # LEGENDA
    # -------------------------------------------------

    if "legenda_gerada" in st.session_state:

        st.text_area(
            "Legenda final",
            st.session_state["legenda_gerada"],
            height=550
        )

    else:
        st.info("⚠️ Gere a legenda para visualizar aqui.")

    # -------------------------------------------------
    # AÇÕES
    # -------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        if "imagem_final_bytes" in st.session_state:
            st.download_button(
                "⬇️ Baixar imagem",
                st.session_state["imagem_final_bytes"],
                "post_final.png",
                "image/png",
                use_container_width=True
            )

    with col2:
        if "legenda_gerada" in st.session_state:
            st.download_button(
                "⬇️ Baixar legenda",
                st.session_state["legenda_gerada"],
                "legenda.txt",
                "text/plain",
                use_container_width=True
            )

    # -------------------------------------------------
    # 🔥 SALVAR HISTÓRICO
    # -------------------------------------------------

    with col3:
        if st.button("💾 Salvar no histórico", use_container_width=True):

            salvar_post()
            st.success("Post salvo no histórico!")
