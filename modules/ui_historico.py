# =====================================================
# zAz — MÓDULO 09
# ETAPA 09 — POSTAGEM
# =====================================================

# =====================================================
# IMPORTS
# =====================================================
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
# HELPERS — LIMPEZA DE ESTADO (APENAS ETAPA 09)
# =====================================================
def limpar_estado_postagem():
    campos = [
        "imagem_final_bytes",
        "legenda_gerada",
        "layout_final"
    ]
    for c in campos:
        st.session_state.pop(c, None)

    st.cache_data.clear()


# =====================================================
# HELPERS — LIMITAR POSTS POR USUÁRIO (MAX 10)
# =====================================================
def aplicar_limite_posts(email, limite=10):
    try:
        res = (
            conectar()
            .table("posts")
            .select("id")
            .eq("email", email)
            .order("criado_em", desc=False)  # mais antigos primeiro
            .execute()
        )

        posts = res.data or []

        if len(posts) >= limite:
            excedentes = posts[: len(posts) - limite + 1]

            for p in excedentes:
                conectar().table("posts").delete().eq("id", p["id"]).execute()

    except Exception:
        pass  # falha silenciosa para não travar o fluxo


# =====================================================
# HELPERS — SALVAR POST
# =====================================================
def salvar_post():
    try:
        if "imagem_final_bytes" not in st.session_state:
            return False

        if "legenda_gerada" not in st.session_state:
            return False

        email = st.session_state.get("email")
        if not email:
            return False

        # aplica limite antes de salvar
        aplicar_limite_posts(email, limite=10)

        imagem_b64 = base64.b64encode(
            st.session_state["imagem_final_bytes"]
        ).decode()

        dados = {
            "email": email,
            "headline": st.session_state.get("headline_escolhida", ""),
            "conceito": st.session_state.get("conceito_visual", ""),
            "legenda": st.session_state.get("legenda_gerada", ""),
            "imagem_base64": imagem_b64
        }

        conectar().table("posts").insert(dados).execute()
        return True

    except Exception:
        return False


# =====================================================
# HELPERS — FINALIZAR
# =====================================================
def finalizar_postagem():
    sucesso = salvar_post()

    if sucesso:
        limpar_estado_postagem()
        st.success("Post salvo com sucesso.")
        st.session_state.etapa = 1
        st.rerun()
    else:
        st.error("Erro ao salvar o post. Verifique seus dados e tente novamente.")


# =====================================================
# RENDER
# =====================================================
def render_etapa_postagem():

    # -------------------------------------------------
    # CSS (DENTRO DO RENDER)
    # -------------------------------------------------
    st.markdown("""
    <style>
    div.stButton > button,
    div.stDownloadButton > button {
        background-color: transparent !important;
        color: #FF9D28 !important;
        font-weight: 700;
        border: 1px solid #FF9D28 !important;
    }
    div.stButton > button:hover,
    div.stDownloadButton > button:hover {
        background-color: rgba(255,157,40,0.08) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>09. Postagem</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # PREVIEW DA IMAGEM
    # -------------------------------------------------
    if "imagem_final_bytes" in st.session_state:
        img = Image.open(io.BytesIO(st.session_state["imagem_final_bytes"]))
        st.image(img, use_container_width=True)
    else:
        st.info("⚠️ Gere o Canvas para visualizar a imagem final.")

    # -------------------------------------------------
    # PREVIEW DA LEGENDA
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
    # DOWNLOADS
    # -------------------------------------------------
    col1, col2 = st.columns(2)

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
    # FINALIZAR
    # -------------------------------------------------
    if (
        "imagem_final_bytes" in st.session_state
        and "legenda_gerada" in st.session_state
    ):
        st.divider()
        if st.button("✅ Salvar e finalizar", use_container_width=True):
            finalizar_postagem()

    # -------------------------------------------------
    # VOLTAR
    # -------------------------------------------------
    st.divider()
    if st.button("⬅ Voltar", use_container_width=True):
        st.session_state.etapa = 8
        st.rerun()
