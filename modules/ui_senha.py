import streamlit as st
import re


# =====================================
# VALIDAÇÕES
# =====================================
def email_valido(email: str) -> bool:
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))


def senha_valida(senha: str) -> bool:
    return bool(senha and len(senha) >= 4)


# =====================================
# RENDER
# =====================================
def render_trocar_senha(atualizar_senha, validar_usuario):

    email = st.text_input("Email", key="alt_email")
    nova_senha = st.text_input("Nova senha", type="password", key="alt_senha")

    email_ok = email_valido(email)
    senha_ok = senha_valida(nova_senha)

    if email and not email_ok:
        st.warning("Email inválido")

    if nova_senha and not senha_ok:
        st.warning("Senha mínima: 4 caracteres")

    pode_atualizar = email_ok and senha_ok

    if st.button(
        "Atualizar senha",
        use_container_width=True,
        disabled=not pode_atualizar
    ):

        # verifica se usuário existe antes
        if not validar_usuario(email, nova_senha):
            atualizar_senha(email, nova_senha)
            st.success("Senha atualizada com sucesso.")
        else:
            st.success("Senha atualizada com sucesso.")
