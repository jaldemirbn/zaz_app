# =====================================================
# zAz — ORQUESTRADOR (VERSÃO FINAL ESTÁVEL + EMAIL)
# =====================================================

import streamlit as st
import uuid
import requests
from supabase import create_client

from modules.ui_login import render_login
from modules.ui_cadastro import render_cadastro
from modules.ui_senha import render_trocar_senha

from modules.ui_ideias import render_etapa_ideias
from modules.ui_headline import render_etapa_headline
from modules.ui_conceito import render_etapa_conceito
from modules.ui_imagens import render_etapa_imagens
from modules.ui_postagem import render_etapa_postagem
from modules.ui_historico import render_etapa_historico


# =====================================================
# CONFIG
# =====================================================
st.set_page_config(
    page_title="zAz",
    layout="centered",
    page_icon="🚀"
)


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
# EMAIL (RESEND)
# =====================================================
def enviar_email_confirmacao(email, link):

    st.info(f"📧 Enviando email para: {email}")

    r = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {st.secrets['RESEND_API_KEY']}",
            "Content-Type": "application/json"
        },
        json={
            "from": "zAz <contato@appzaz.com.br>",

            "to": [email],
            "subject": "Confirme sua conta",
            "html": f"<a href='{link}'>Confirmar conta</a>"
        }
    )

    if r.status_code in (200, 201):
        st.success("✅ Email enviado com sucesso")
    else:
        st.error(f"❌ Falha ao enviar email | status: {r.status_code}")


# =====================================================
# AUTH HELPERS
# =====================================================
def validar_usuario(email, senha):

    r = (
        conectar()
        .table("usuarios")
        .select("*")
        .eq("email", email)
        .eq("senha", senha)
        .eq("email_confirmado", True)
        .execute()
    )

    return len(r.data) > 0


# =====================================================
# 🔥 CRIAR USUÁRIO
# LINHA ~78
# =====================================================
def criar_usuario(email, senha):

    supabase = conectar()

    token = str(uuid.uuid4())

    dados = {
        "email": email,
        "senha": senha,
        "email_confirmado": False,
        "token_confirmacao": token
    }

    supabase.table("usuarios").insert(dados).execute()

    link = f"https://zazapp.streamlit.app/?token={token}"

    enviar_email_confirmacao(email, link)

    return True


# =====================================================
# TROCAR SENHA
# =====================================================
def atualizar_senha(email, senha):

    conectar().table("usuarios").update({
        "senha": str(senha)
    }).eq("email", email).execute()


# =====================================================
# SESSION
# =====================================================
if "logado" not in st.session_state:
    st.session_state.logado = False


# =====================================================
# AUTH FLOW
# =====================================================
if not st.session_state.logado:

    tab_login, tab_cadastro, tab_senha = st.tabs(
        ["🔐 Entrar", "🆕 Criar conta", "♻️ Trocar senha"]
    )

    with tab_login:
        render_login(validar_usuario)

    with tab_cadastro:

        ok = render_cadastro(criar_usuario)

        if ok:
            st.success("Conta criada. Verifique seu email para confirmar.")

    with tab_senha:
        render_trocar_senha(atualizar_senha)

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
