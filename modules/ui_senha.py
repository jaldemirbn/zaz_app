import streamlit as st
import re
import secrets
from datetime import datetime, timedelta

from modules.email_service import enviar_email_confirmacao


def email_valido(email: str) -> bool:
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))


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

        token = secrets.token_urlsafe(32)

        expira = datetime.utcnow() + timedelta(minutes=30)

        # 🔥 AQUI ESTÁ A CORREÇÃO FINAL
        supabase.table("usuarios").update({
            "token_reset": token,
            "token_expira": expira.isoformat() + "Z"
        }).eq("email", email).execute()

        base_url = st.get_option("browser.serverAddress") or ""
        link = f"{base_url}?reset={token}"

        enviar_email_confirmacao(email, link)

        st.success("Email enviado. Verifique sua caixa de entrada.")
