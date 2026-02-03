import streamlit as st


def render_login(supabase):

    if "logado" not in st.session_state:
        st.session_state.logado = False

    email = st.text_input("Email", key="login_email")
    senha = st.text_input("Senha", type="password", key="login_senha")

    if st.button("Entrar", use_container_width=True):

        try:
            res = supabase.auth.sign_in_with_password({
                "email": email.strip().lower(),
                "password": senha
            })

            st.session_state.logado = True
            st.session_state["user"] = res.user
            st.session_state["email"] = res.user.email

            st.rerun()

        except Exception as e:
            st.error(e)
