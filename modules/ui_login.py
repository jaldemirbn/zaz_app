import streamlit as st


# =====================================================
# LOGIN — RESPONSABILIDADE ÚNICA
# =====================================================
def render_login(validar_usuario, reenviar_confirmacao):

    if "logado" not in st.session_state:
        st.session_state.logado = False

    email = st.text_input("Email", key="login_email")
    senha = st.text_input("Senha", type="password", key="login_senha")

    # ===============================
    # LOGIN
    # ===============================
    if st.button("Entrar", use_container_width=True):

        if validar_usuario(email, senha):
            st.session_state.logado = True
            st.rerun()
        else:
            st.error("Email ou senha inválidos")

    # ===============================
    # REENVIAR CONFIRMAÇÃO
    # ===============================
    st.markdown("---")

    if st.button("Reenviar email de confirmação", use_container_width=True):

        if email:
            reenviar_confirmacao(email)
        else:
            st.warning("Digite seu email primeiro")
