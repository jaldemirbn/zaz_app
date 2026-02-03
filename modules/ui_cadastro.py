import streamlit as st


def render_cadastro(supabase):

    # =====================================================
    # TÍTULO
    # =====================================================
    st.subheader("Criar conta")


    # =====================================================
    # CAMPOS
    # =====================================================
    email = st.text_input("Email", key="cad_email")
    senha = st.text_input("Senha", type="password", key="cad_senha")


    st.divider()


    # =====================================================
    # TERMOS OBRIGATÓRIOS
    # =====================================================
    aceite_termos = st.checkbox("Li e aceito os Termos de Uso")
    aceite_privacidade = st.checkbox("Li e aceito a Política de Privacidade")

    st.caption("É obrigatório aceitar os termos para criar a conta.")


    st.divider()


    # =====================================================
    # BOTÃO CRIAR CONTA
    # =====================================================
    if st.button("Criar conta", use_container_width=True):

        # 🔥 BLOQUEIO SE NÃO ACEITAR
        if not (aceite_termos and aceite_privacidade):
            st.warning("Você precisa aceitar os Termos de Uso e a Política de Privacidade para continuar.")
            return

        # 🔥 BLOQUEIO CAMPOS VAZIOS
        if not email or not senha:
            st.warning("Preencha email e senha.")
            return

        try:
            supabase.auth.sign_up({
                "email": email.strip().lower(),
                "password": senha
            })

            st.success("Conta criada com sucesso. Agora é só fazer login.")

        except Exception as e:
            st.error(e)
