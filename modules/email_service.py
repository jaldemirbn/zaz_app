import resend
import streamlit as st

resend.api_key = st.secrets["RESEND_API_KEY"]


def enviar_email_confirmacao(destino: str, link: str):

    st.info("DEBUG → chamando Resend agora")

    response = resend.Emails.send({
        "from": "zAz <noreply@appzaz.com.br>",
        "to": destino,
        "subject": "Teste Resend zAz",
        "html": "<h1>Se chegou, Resend está OK</h1>"
    })

    st.success("DEBUG → resposta do Resend:")
    st.write(response)
