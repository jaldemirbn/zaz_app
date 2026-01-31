import resend
import streamlit as st


resend.api_key = st.secrets["RESEND_API_KEY"]


def enviar_email_confirmacao(destino: str, link: str):

    st.write("DEBUG → enviando email para:", destino)

    try:
        r = resend.Emails.send({
            "from": "zAz <noreply@appzaz.com.br>",
            "to": destino,
            "subject": "Teste zAz",
            "html": f"<a href='{link}'>Clique aqui</a>"
        })

        st.write("DEBUG → resposta resend:", r)

    except Exception as e:
        st.error(f"ERRO RESEND: {e}")
