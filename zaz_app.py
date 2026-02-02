import streamlit as st
import random
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
# WHATSAPP
# =====================================================
def enviar_whatsapp(numero, mensagem):

    url = f"https://graph.facebook.com/v22.0/{st.secrets['WA_PHONE_ID']}/messages"


    headers = {
        "Authorization": f"Bearer {st.secrets['WA_TOKEN']}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": mensagem}
    }

    requests.post(url, headers=headers, json=payload)


# =====================================================
# AUTH
# =====================================================
def validar_usuario(email, senha):

    email = email.strip().lower()

    r = conectar().table("usuarios") \
        .select("*") \
        .eq("email", email) \
        .eq("senha", senha) \
        .eq("email_confirmado", True) \
        .execute()

    return len(r.data) > 0


def criar_usuario(email, senha, telefone):

    codigo = str(random.randint(100000, 999999))

    dados = {
        "email": email.strip().lower(),
        "senha": senha,
        "telefone": telefone,
        "email_confirmado": False,
        "otp_codigo": codigo
    }

    conectar().table("usuarios").insert(dados).execute()

    enviar_whatsapp(
        telefone,
        f"Seu código de confirmação zAz é: {codigo}"
    )


def confirmar_codigo(email, codigo_digitado):

    email = email.strip().lower()
    codigo_digitado = str(codigo_digitado).strip()

    resp = conectar().table("usuarios") \
        .select("otp_codigo") \
        .eq("email", email) \
        .single() \
        .execute()

    if not resp.data:
        return False

    if str(resp.data["otp_codigo"]).strip() != codigo_digitado:
        return False

    conectar().table("usuarios") \
        .update({
            "email_confirmado": True,
            "otp_codigo": None
        }) \
        .eq("email", email) \
        .execute()

    return True


def atualizar_senha(email, senha):

    conectar().table("usuarios") \
        .update({"senha": senha}) \
        .eq("email", email) \
        .execute()


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
        render_cadastro(criar_usuario, confirmar_codigo)

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
