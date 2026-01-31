# =====================================================
# zAz — ORQUESTRADOR
# =====================================================

import streamlit as st
from supabase import create_client
import uuid
import requests
import os


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
# EMAIL (RESEND)
# =====================================================
def enviar_confirmacao(email, token):

    link = f"https://SEUAPP.streamlit.app/?token={token}"  # ⚠️ TROQUE PELO SEU LINK

    requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {st.secrets['RESEND_API_KEY']}",
            "Content-Type": "application/json",
        },
        json={
            "from": "zAz <no-reply@appzaz.com.br>",
            "to": [email],
            "subject": "Confirme sua conta no zAz",
            "html": f"""
                <h2>Confirme sua conta</h2>
                <p>Clique abaixo:</p>
                <a href="{link}"
                style="background:#FFC107;padding:12px 20px;border-radius:8px;text-decoration:none;color:#000;font-weight:bold;">
                Confirmar conta
                </a>
            """
        },
    )


# =====================================================
# FUNÇÕES DB
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


def criar_usuario(email, senha):

    token = str(uuid.uuid4())

    dados = {
        "email": email,
        "senha": senha,
        "token_confirmacao": token,
        "email_confirmado": False
    }

    conectar().table("usuarios").insert(dados).execute()

    enviar_confirmacao(email, token)


def atualizar_senha(email, senha):
    conectar().table("usuarios").update({
        "senha": senha
    }).eq("email", email).execute()


# =====================================================
# CONFIRMAÇÃO VIA TOKEN
# =====================================================
params = st.query_params

if "token" in params:

    token = params["token"]

    conectar().table("usuarios").update({
        "email_confirmado": True,
        "token_confirmacao": None
    }).eq("token_confirmacao", token).execute()

    st.success("Conta confirmada. Agora você pode entrar.")
    st.stop()


# =====================================================
# SESSION
# =====================================================
if "logado" not in st.session_state:
    st.session_state.logado = False


# =====================================================
# IMPORT UI
# =====================================================
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
