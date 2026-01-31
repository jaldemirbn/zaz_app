# =====================================================
# zAz — ORQUESTRADOR
# =====================================================

import streamlit as st
from supabase import create_client
import secrets

from modules.ui_login import render_login
from modules.ui_cadastro import render_cadastro
from modules.ui_senha import render_trocar_senha

from modules.ui_ideias import render_etapa_ideias
from modules.ui_headline import render_etapa_headline
from modules.ui_conceito import render_etapa_conceito
from modules.ui_imagens import render_etapa_imagens
from modules.ui_postagem import render_etapa_postagem
from modules.ui_historico import render_etapa_historico

from modules.email_service import enviar_email_confirmacao


# =====================================================
# CONFIG
# =====================================================
st.set_page_config(page_title="zAz", layout="centered", page_icon="🚀")


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
# FUNÇÕES
# =====================================================
def validar_usuario(email, senha):
    r = (
        conectar()
        .table("usuarios")
        .select("*")
        .eq("email", email)
        .eq("senha", senha)
        .execute()
    )
    return len(r.data) > 0


def criar_usuario(email, senha):
    supabase = conectar()

    try:
        token = secrets.token_urlsafe(32)

        supabase.table("usuarios").insert({
            "email": email,
            "senha": senha,
            "email_confirmado": False,
            "token_confirmacao": token
        }).execute()

    except:
        st.error("Email já cadastrado.")
        return

    base = st.get_option("browser.serverAddress") or ""
    link = f"{base}?confirm={token}"

    enviar_email_confirmacao(email, link)

    st.success("Conta criada. Verifique seu email para confirmar.")


def atualizar_senha(email, senha):
    conectar().table("usuarios").update({
        "senha": senha
    }).eq("email", email).execute()


# =====================================================
# SESSION
# =====================================================
if "logado" not in st.session_state:
    st.session_state.logado = False


# =====================================================
# AUTH
# =====================================================
if not st.session_state.logado:

    tab_login, tab_cadastro, tab_senha = st.tabs(
        ["🔐 Entrar", "🆕 Criar conta", "♻️ Trocar senha"]
    )

    with tab_login:
        render_login(validar_usuario)

    with tab_cadastro:
        render_cadastro(criar_usuario)

    with tab_senha:
        render_trocar_senha(conectar)

    st.stop()


# =====================================================
# APP FLOW
# =====================================================
render_etapa_ideias()
render_etapa_headline()
render_etapa_conceito()
render_etapa_imagens()
render_etapa_postagem()
render_etapa_historico()
