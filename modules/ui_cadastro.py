import streamlit as st
import re


# =====================================================
# STATES
# =====================================================
def _init_states():

    if "codigo_enviado" not in st.session_state:
        st.session_state.codigo_enviado = False


# =====================================================
# VALIDAÇÃO
# =====================================================
def email_valido(email):
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))


def senha_valida(senha):
    return bool(senha and len(senha) >= 4)


def telefone_valido(tel):
    return tel.isdigit() and 10 <= len(tel) <= 11


# =====================================================
# CADASTRO OTP SIMPLES
# =====================================================
def render_cadastro(criar_usuario, confirmar_codigo):

    _init_states()

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    telefone_raw = st.text_input(
        "WhatsApp (DDD + número)",
        placeholder="85996655017"
    )

    telefone = f"55{telefone_raw}" if telefone_raw else ""

    st.markdown("---")

    # =================================================
    # ETAPA 1 — ENVIAR CÓDIGO
    # =================================================
    if not st.session_state.codigo_enviado:

        valido = (
            email_valido(email)
            and senha_valida(senha)
            and telefone_valido(telefone_raw)
        )

        if st.button("Enviar código no WhatsApp", disabled=not valido):

            criar_usuario(email, senha, telefone)

            st.session_state.codigo_enviado = True
            st.rerun()

        return

    # =================================================
    # ETAPA 2 — CONFIRMAR
    # =================================================
    codigo = st.text_input("Digite o código recebido")

    if st.button("Confirmar código"):

        if confirmar_codigo(email, codigo):
            st.success("Conta confirmada. Faça login.")
        else:
            st.error("Código inválido")
