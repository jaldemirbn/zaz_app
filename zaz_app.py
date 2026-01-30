import streamlit as st
from modules.ui_ideias import render_etapa_ideias


if "logado" not in st.session_state:
    st.session_state.logado = False


# ======================
# LOGIN
# ======================
if not st.session_state.logado:

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):

        if validar_usuario(email, senha):
            st.session_state.logado = True
            st.rerun()
        else:
            st.error("Email ou senha inválidos")


# ======================
# APP (DEPOIS DO LOGIN)
# ======================
else:

    render_etapa_ideias()
