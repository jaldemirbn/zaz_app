import streamlit as st
from supabase import create_client

from modules.ui_login import render_login
from modules.ui_cadastro import render_cadastro
from modules.ui_senha import render_trocar_senha
from modules.ui_logo import render_logo

from modules.ui_ideias import render_etapa_ideias
from modules.ui_headline import render_etapa_headline
from modules.ui_conceito import render_etapa_conceito
from modules.ui_imagens import render_etapa_imagens
from modules.ui_post import render_etapa_post
from modules.ui_canvas import render_etapa_canvas
from modules.ui_legenda import render_etapa_legenda
from modules.ui_postagem import render_etapa_postagem
from modules.ui_historico import render_etapa_historico


# =====================================================
# CONFIG
# =====================================================
st.set_page_config(page_title="zAz", layout="centered", page_icon="🚀")


# =====================================================
# 🎨 ESTILO GLOBAL zAz (CORRIGIDO)
# =====================================================
st.markdown("""
<style>

/* ===== TODOS OS TIPOS DE BOTÃO ===== */
div.stButton > button,
div.stDownloadButton > button,
div.stFormSubmitButton > button,
button[kind="primary"] {

    background: transparent !important;
    background-color: transparent !important;

    color: #FF9D28 !important;

    font-weight: 700 !important;

    border: 1px solid #FF9D28 !important;

    box-shadow: none !important;
}


/* ===== HOVER ===== */
div.stButton > button:hover,
div.stDownloadButton > button:hover,
div.stFormSubmitButton > button:hover,
button[kind="primary"]:hover {

    background-color: rgba(255,157,40,0.08) !important;
    box-shadow: none !important;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# SUPABASE
# =====================================================
@st.cache_resource
def conectar():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


supabase = conectar()


# =====================================================
# LOGO GLOBAL (sempre aparece)
# =====================================================
render_logo()


# =====================================================
# SESSION
# =====================================================
if "logado" not in st.session_state:
    st.session_state.logado = False

if "etapa" not in st.session_state:
    st.session_state.etapa = 1


# =====================================================
# AUTH FLOW
# =====================================================
if not st.session_state.logado:

    tab_login, tab_cadastro, tab_senha = st.tabs(
        ["🔐 Entrar", "🆕 Criar conta", "♻️ Trocar senha"]
    )

    with tab_login:
        render_login(supabase)

    with tab_cadastro:
        render_cadastro(supabase)

    with tab_senha:
        st.info("Troca de senha será via Supabase futuramente")

    st.stop()


# =====================================================
# LOGOUT
# =====================================================
col1, col2 = st.columns([8, 1])

with col2:
    if st.button("🚪 Sair"):
        supabase.auth.sign_out()
        st.session_state.clear()
        st.rerun()


# =====================================================
# APP FLOW (WIZARD SEQUENCIAL)
# =====================================================
etapa = st.session_state.etapa


if etapa == 1:
    render_etapa_ideias()

elif etapa == 2:
    render_etapa_headline()

elif etapa == 3:
    render_etapa_conceito()

elif etapa == 4:
    render_etapa_imagens()

elif etapa == 5:
    render_etapa_post()

elif etapa == 6:
    render_etapa_canvas()

elif etapa == 7:
    render_etapa_legenda()

elif etapa == 8:
    render_etapa_postagem()

elif etapa == 9:
    render_etapa_historico()
