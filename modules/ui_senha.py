import streamlit as st
import re


def email_valido(email: str) -> bool:
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))


def render_trocar_senha():

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
        # ainda vamos implementar o envio real
        st.success("Se o email existir, você receberá um link de redefinição.")
