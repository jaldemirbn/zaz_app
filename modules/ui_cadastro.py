import streamlit as st


def render_cadastro(supabase):

    st.subheader("Criar conta")

    email = st.text_input("Email", key="cad_email")
    senha = st.text_input("Senha", type="password", key="cad_senha")

    if st.button("Criar conta", use_container_width=True):

        try:
            supabase.auth.sign_up({
                "email": email.strip().lower(),
                "password": senha
            })

            st.success("Conta criada com sucesso. Agora é só fazer login.")

        except Exception as e:
            st.error(e)
