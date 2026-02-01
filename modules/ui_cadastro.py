import streamlit as st
import re


# =====================================================
# STATES
# =====================================================
def _init_states():

    defaults = {
        "aceite_termos": False,
        "aceite_privacidade": False,
        "abrir_termos": False,
        "abrir_privacidade": False,

        "cadastro_executado": False,
        "codigo_enviado": False,
        "codigo_confirmado": False
    }

    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# =====================================================
# VALIDAÇÃO
# =====================================================
def email_valido(email: str) -> bool:
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))


def senha_valida(senha: str) -> bool:
    return bool(senha and len(senha) >= 4)


def telefone_valido(tel: str) -> bool:
    return tel.isdigit() and len(tel) >= 10


# =====================================================
# TERMOS
# =====================================================
@st.dialog("Termos de Uso", width="large")
def dialog_termos():

    aceite = st.checkbox("Aceitar termos")

    if st.button("Confirmar"):
        if aceite:
            st.session_state.aceite_termos = True
            st.session_state.abrir_termos = False
            st.rerun()


# =====================================================
# PRIVACIDADE
# =====================================================
@st.dialog("Política de Privacidade", width="large")
def dialog_privacidade():

    aceite = st.checkbox("Aceitar política")

    if st.button("Confirmar"):
        if aceite:
            st.session_state.aceite_privacidade = True
            st.session_state.abrir_privacidade = False
            st.rerun()


# =====================================================
# 🔥 CADASTRO COM WHATSAPP OTP
# =====================================================
def render_cadastro(criar_usuario, confirmar_codigo):

    _init_states()

    email = st.text_input("Email", key="cad_email")
    senha = st.text_input("Senha", type="password", key="cad_senha")
    telefone = st.text_input(
        "WhatsApp (somente números, ex: 5585987154528)",
        key="cad_tel"
    )

    st.markdown("---")

    # termos
    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.aceite_termos:
            st.success("✅ Termos aceitos")
        elif st.button("Aceitar Termos"):
            st.session_state.abrir_termos = True

    with col2:
        if st.session_state.aceite_privacidade:
            st.success("✅ Privacidade aceita")
        elif st.button("Aceitar Privacidade"):
            st.session_state.abrir_privacidade = True

    if st.session_state.abrir_termos:
        dialog_termos()

    if st.session_state.abrir_privacidade:
        dialog_privacidade()

    st.markdown("---")

    email_ok = email_valido(email)
    senha_ok = senha_valida(senha)
    tel_ok = telefone_valido(telefone)

    pode_criar = (
        email_ok
        and senha_ok
        and tel_ok
        and st.session_state.aceite_termos
        and st.session_state.aceite_privacidade
    )

    # =================================================
    # 🔥 ENVIAR CÓDIGO
    # =================================================
    if not st.session_state.codigo_enviado:

        if st.button(
            "Enviar código no WhatsApp",
            use_container_width=True,
            disabled=not pode_criar
        ):

            criar_usuario(email, senha, telefone)

            st.session_state.codigo_enviado = True
            st.success("📲 Código enviado no WhatsApp")

        return False

    # =================================================
    # 🔥 CONFIRMAR CÓDIGO
    # =================================================
    codigo = st.text_input("Digite o código recebido")

    if st.button("Confirmar código", use_container_width=True):

        if confirmar_codigo(email, codigo):
            st.success("✅ Conta confirmada. Agora faça login.")
            st.session_state.codigo_confirmado = True
        else:
            st.error("Código inválido")

    return False
