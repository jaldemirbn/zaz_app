import streamlit as st
from supabase import create_client
import base64

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
    background-color: transparent !important;
    color: #FF9D28 !important;
    font-weight: 700 !important;
    border: 1px solid #FF9D28 !important;
    box-shadow: none !important;
}
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
# 🔐 LOGIN PERSISTENTE (NOVO — AQUI ESTÁ A MÁGICA)
# =====================================================
sessao = supabase.auth.get_session()

if sessao and sessao.session:
    st.session_state.logado = True
    st.session_state.email = sessao.session.user.email
else:
    st.session_state.logado = False


# =====================================================
# 💾 DRAFT (mantido como estava)
# =====================================================
def salvar_draft(email):

    dados = {}

    for k, v in st.session_state.items():

        if isinstance(v, (str, int, float, bool)):
            dados[k] = v

    supabase.table("user_draft").upsert({
        "email": email,
        "etapa": st.session_state.etapa,
        "dados": dados
    }).execute()


def carregar_draft(email):

    resp = (
        supabase
        .table("user_draft")
        .select("*")
        .eq("email", email)
        .execute()
    )

    if not resp.data:
        return

    row = resp.data[0]

    st.session_state.etapa = row["etapa"]

    dados = row["dados"] or {}

    for k, v in dados.items():
        st.session_state[k] = v


# =====================================================
# LOGO GLOBAL
# =====================================================
render_logo()


# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:

    st.markdown("### zAz app")

    if st.button("📚 Histórico", use_container_width=True):
        st.session_state.etapa = 9
        st.rerun()


# =====================================================
# SESSION DEFAULTS
# =====================================================
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
# CARREGAR DRAFT
# =====================================================
email = st.session_state.get("email")

if email and not st.session_state.get("draft_carregado"):
    carregar_draft(email)
    st.session_state.draft_carregado = True


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
# SALVAR DRAFT
# =====================================================
if email:
    salvar_draft(email)


# =====================================================
# WIZARD
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
