import streamlit as st
import re


# =====================================================
# VALIDAÇÃO
# =====================================================
def email_valido(email: str) -> bool:
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))


def senha_valida(senha: str) -> bool:
    return bool(senha and len(senha) >= 4)


def telefone_valido(tel: str) -> bool:
    return tel.isdigit() and 10 <= len(tel) <= 11


# =====================================================
# TERMOS
# =====================================================
@st.dialog("Termos de Uso", width="large")
def dialog_termos():
    aceite = st.checkbox("Aceitar termos")

    if st.button("Confirmar"):
        if aceite:
            st.session_state.aceite_termos = True
            st.rerun()


@st.dialog("Política de Privacidade", width="large")
def dialog_privacidade():
    aceite = st.checkbox("Aceitar política")

    if st.button("Confirmar"):
        if aceite:
            st.session_state.aceite_privacidade = True
            st.rerun()


# =====================================================
# 🔥 CADASTRO SIMPLES (SEM OTP)
# =====================================================
def render_cadastro(criar_usuario):

    if "aceite_termos" not in st.session_state:
        st.session_state.aceite_termos = False

    if "aceite_privacidade" not in st.session_state:
        st.session_state.aceite_privacidade = False

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    telefone_raw = st.text_input(
        "Telefone (DDD + número)",
        placeholder="85996655017"
    )

    telefone = f"55{telefone_raw}" if telefone_raw else ""

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.aceite_termos:
            st.success("✅ Termos aceitos")
        elif st.button("Aceitar Termos"):
            dialog_termos()

    with col2:
        if st.session_state.aceite_privacidade:
            st.success("✅ Privacidade aceita")
        elif st.button("Aceitar Privacidade"):
            dialog_privacidade()

    st.markdown("---")

    email_ok = email_valido(email)
    senha_ok = senha_valida(senha)
    tel_ok = telefone_valido(telefone_raw)

    pode_criar = (
        email_ok
        and senha_ok
        and tel_ok
        and st.session_state.aceite_termos
        and st.session_state.aceite_privacidade
    )

    if st.button("Criar conta", use_container_width=True):

        if not pode_criar:
            st.warning("Preencha todos os campos corretamente.")
            return

        criar_usuario(email, senha, telefone)

        st.success("Conta criada com sucesso! Agora faça login.")
