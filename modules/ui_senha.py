# =====================================================
# zAz — RESET DE SENHA (EMAIL + TOKEN)
# =====================================================

import streamlit as st
import re
import secrets
from datetime import datetime, timedelta

from modules.email_service import enviar_email_confirmacao


# =====================================================
# VALIDAÇÃO
# =====================================================
def email_valido(email: str) -> bool:
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))


# =====================================================
# RENDER
# =====================================================
def render_trocar_senha(conectar):

    st.subheader("Redefinir senha")

    email = st.text_input("Digite seu email", key="reset_email")

    if not email:
        return

    if not email_valido(email):
        st.warning("Email inválido")
        return

    if not st.button("Enviar link de redefinição", use_container_width=True):
        return


    # =================================================
    # SUPABASE
    # =================================================
    supabase = conectar()

    r = (
        supabase
        .table("usuarios")
        .select("*")
        .eq("email", email)
        .execute()
    )

    # nunca revelar se existe ou não
    if len(r.data) == 0:
        st.success("Se o email existir, você receberá um link.")
        return


    # =================================================
    # GERAR TOKEN
    # =================================================
    token = secrets.token_urlsafe(32)

    # 👉 TEXTO, não timestamp (Supabase odeia timestamp via API)
    expira = (datetime.utcnow() + timedelta(minutes=30)).isoformat()


    # =================================================
    # SALVAR (100% compatível)
    # =================================================
    supabase.table("usuarios").update({
        "token_reset": token,
        "token_expira": expira
    }).eq("email", email).execute()


    # =================================================
    # LINK
    # =================================================
    base = st.get_option("browser.serverAddress") or ""
    link = f"{base}?reset={token}"


    # =================================================
    # EMAIL
    # =================================================
    enviar_email_confirmacao(email, link)

    st.success("Email enviado. Verifique sua caixa de entrada.")
