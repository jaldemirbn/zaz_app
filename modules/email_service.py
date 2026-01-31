import resend
import streamlit as st

resend.api_key = st.secrets["RESEND_API_KEY"]


def enviar_email_confirmacao(destino: str, link: str = ""):

    st.error("🔥 CHEGOU NA FUNÇÃO DE ENVIO")

    response = resend.Emails.send({
        "from": "zAz <noreply@appzaz.com.br>",
        "to": destino,
        "subject": "Teste fluxo zAz",
        "html": "<h1>Email do fluxo real</h1>"
    })

    st.success("Email enviado via fluxo real")
    st.write(response)
