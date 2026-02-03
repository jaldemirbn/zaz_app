import streamlit as st


def render_login(validar_usuario):

    if "logado" not in st.session_state:
        st.session_state.logado = False

    email = st.text_input("Email", key="login_email")
    senha = st.text_input("Senha", type="password", key="login_senha")

    if st.button("Entrar", use_container_width=True):

        if validar_usuario(email, senha):
            st.session_state.logado = True

            # 🔥 ESSENCIAL → salvar dono do usuário
            st.session_state["email"] = email.strip().lower()

            st.rerun()
        else:
            st.error("Email ou senha inválidos")
