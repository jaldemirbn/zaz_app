import resend
import streamlit as st

resend.api_key = st.secrets["RESEND_API_KEY"]


def enviar_email_confirmacao(destino: str, link: str):

    st.warning(f"🚀 DEBUG: tentando enviar email para {destino}")

    try:
        response = resend.Emails.send({
            "from": "zAz <noreply@appzaz.com.br>",
            "to": destino,
            "subject": "Teste envio zAz",
            "html": "<h1>Se você recebeu isso, o Resend está OK</h1>"
        })

        st.success("✅ DEBUG: Resend respondeu")
        st.write(response)

    except Exception as e:
        st.error(f"❌ ERRO RESEND: {e}")
