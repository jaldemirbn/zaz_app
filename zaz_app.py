# =====================================================
# zAz — ORQUESTRADOR (WHATSAPP OTP ONLY • LIMPO)
# =====================================================

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
# 🔥 WHATSAPP ENVIO
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
# AUTH HELPERS
# =====================================================
def validar_usuario(email, senha):

    # 🔥 CORREÇÃO OBRIGATÓRIA: normalizar email
    email = email.strip().lower()

    r = (
        conectar()
        .table("usuarios")
        .select("*")
    )
