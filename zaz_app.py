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
# 🎨 ESTILO GLOBAL zAz
# =====================================================
st.markdown("""
<style>

div.stButton > button,
div.stDownloadButton > button,
div.stFormSubmitButton > button,
button[kind="primary"] {
    background: transparent !important;
    color: #FF9D28 !important;
    font-weight: 700 !important;
    border: 1px solid #FF9D28 !important;
}

div.stButton > button:hover,
div.stDownloadButton > button:hover,
div.stFormSubmitButton > button:hover,
button[kind="primary"]:hover {
    background-color: rgba(255,157,40,0.08) !important;
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
# 🔥 PERSISTÊNCIA DE ETAPA
# =====================================================
def salvar_etapa(email, etapa):
    supabase.table("user_state").upsert({
        "email": email,
        "etapa": etapa
    }).execute()


def carregar_etapa(email):
    resp = (
        supabase
        .table("user_state")
        .select("etapa")
        .eq("email", email)
        .execute()
    )

    if resp.data:
        return resp.data[0]["etapa"]

    return 1


# =====================================================
# LOGO GLOBAL
# =====================================================
render_logo()


# =====================================================
# 🔥 SIDEBAR GLOBAL
# =====================================================
with st.sidebar:

    st.markdown("### zAz app")

    # 🔥 NÃO salva etapa aqui
    if st.button("📚 Histórico", use_container_width=True):
        st.session_state.etapa = 9
        st.rerun()


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
# 🔥 CARREGAR ETAPA SALVA
# =====================================================
email = st.session_state.get("email")

if email and not st.session_state.get("etapa_carregada"):
    st.session_state.etapa = carregar_etapa(email)
    st.session_state.etapa_carregada = True


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
# 🔥 SALVAR ETAPA AUTOMATICAMENTE (exceto histórico)
# =====================================================
if email and st.session_state.etapa != 9:
    salvar_etapa(email, st.session_s
