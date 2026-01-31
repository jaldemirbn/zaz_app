import streamlit as st
import resend

resend.api_key = st.secrets["RESEND_API_KEY"]


def enviar_email_confirmacao(destino: str, link: str = ""):

    st.info("🚀 TESTE DIRETO: chamando Resend...")

    try:
        response = resend.Emails.send({
            "from": "zAz <noreply@appzaz.com.br>",
            "to": destino,
            "subject": "Teste direto Resend",
            "html": "<h1>Se você recebeu isso, Resend está OK</h1>"
        })

        st.success("✅ Resend respondeu:")
        st.write(response)

    except Exception as e:
        st.error(f"❌ ERRO RESEND: {e}")
