import resend
import streamlit as st


resend.api_key = st.secrets["RESEND_API_KEY"]


def enviar_email_confirmacao(destino: str, link: str):

    resend.Emails.send({
        "from": "zAz <noreply@appzaz.com.br>",
        "to": destino,
        "subject": "Redefinição de senha — zAz",
        "html": f"""
        <div style="font-family: Arial; padding:20px">
            <h2>Redefinir sua senha</h2>
            <p>Clique no botão abaixo para criar uma nova senha:</p>
            <a href="{link}"
               style="background:#FFC107;padding:12px 20px;
               text-decoration:none;color:#000;border-radius:6px;font-weight:bold;">
               Redefinir senha
            </a>
            <p style="margin-top:20px;font-size:12px;color:#666">
               Se você não solicitou, ignore este email.
            </p>
        </div>
        """
    })
