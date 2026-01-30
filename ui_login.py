import streamlit as st
from modules.ui_logo import render_logo


# =========================================
# MÓDULO LOGIN
# Responsabilidade única:
# autenticar usuário e liberar app
# =========================================


def tela_login():

    # se já logado → não mostra tela
    if st.session_state.get("logado", False):
        return True

    render_logo()

    st.subheader("Entrar na sua conta")

    email = st.text_input("Email", placeholder="seu@email.com")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar", use_container_width=True):

        # LOGIN SIMPLES (temporário)
        if email == "admin@zaz.com" and senha == "1234":
            st.session_state.logado = True
            st.success("Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("Email ou senha incorretos")

    return False

