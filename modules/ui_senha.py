import streamlit as st
import re
import secrets
from datetime import datetime, timedelta

from modules.email_service import enviar_email_confirmacao


# =====================================
# VALIDAÇÃO
# =====================================
def email_valido(email: str) -> bool:
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))


# =====================================
# RENDER
# =====================================
def render_trocar_senha(conectar):

    st.subheader("Redefinir senha")

    email = st.text_input("Digite seu email", key="reset_email")

    email_ok = email_valido(email)

    if email and not email_ok:
        st.warning("Email inválido")

    if st.button(
        "Enviar link de redefinição",
        use_container_width=True,
        disabled=not email_ok
    ):

        supabase = conectar()

        # ---------------------------------
        # verifica se usuário existe
        # ---------------------------------
        r = (
            supabase
            .table("usuarios")
            .select("*")
            .eq("email", email)
            .execute()
        )

        if len(r.data) == 0:
            st.success("Se o email existir, você receberá um link.")
            return

        # ---------------------------------
        # gera token seguro
        # ---------------------------------
        token = secrets.token_urlsafe(32)

        expira = datetime.utcnow() + timedelta(minutes=30)

        # ---------------------------------
        # salva no banco (CORRIGIDO: timestamp puro)
        # ---------------------------------
        supabase.table("usuarios").update({
            "token_reset": token,
            "token_expira": expira
        }).eq("email", email).execute()

        # ---------------------------------
        # cria link mágico
        # ---------------------------------
        base_url = st.get_option("browser.serverAddress") or ""
        link = f"{base_url}?reset={token}"

        # ------------------------
