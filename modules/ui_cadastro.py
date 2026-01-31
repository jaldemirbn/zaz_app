import streamlit as st


# ===============================
# STATES
# ===============================
def _init_states():

    defaults = {
        "aceite_termos": False,
        "aceite_privacidade": False,
        "abrir_termos": False,
        "abrir_privacidade": False,
    }

    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ===============================
# DIALOGS
# ===============================
@st.dialog("Termos de Uso", width="large")
def dialog_termos():

    st.markdown("""
    ## Termos de Uso

    Cole aqui o texto completo dos termos.
    """)

    aceite = st.checkbox("Aceitar termos")

    if st.button("Confirmar"):
        if aceite:
            st.session_state.aceite_termos = True
            st.session_state.abrir_termos = False
            st.rerun()


@st.dialog("Política de Privacidade", width="large")
def dialog_privacidade():

    st.markdown("""
    ## Política de Privacidade

    Cole aqui o texto completo.
    """)

    aceite = st.checkbox("Aceitar política")

    if st.button("Confirmar"):
        if aceite:
            st.session_state.aceite_privacidade = True
            st.session_state.abrir_privacidade = False
            st.rerun()


# ===============================
# RENDER
# ===============================
def render_cadastro(criar_usuario):

    _init_states()

    email = st.text_input("Email", key="cad_email")
    senha = st.text_input("Senha", type="password", key="cad_senha")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.aceite_termos:
            st.success("✅ Termos aceitos")
        elif st.button("Aceitar os Termos de Uso"):
            st.session_state.abrir_termos = True

    with col2:
        if st.session_state.aceite_privacidade:
            st.success("✅ Política aceita")
        elif st.button("Aceitar a Política de Privacidade"):
            st.session_state.abrir_privacidade = True


    if st.session_state.abrir_termos:
        dialog_termos()

    if st.session_state.abrir_privacidade:
        dialog_privacidade()


    st.markdown("---")

    pode_criar = (
        st.session_state.aceite_termos
        and
        st.session_state.aceite_privacidade
    )

    if st.button("Criar conta", use_container_width=True, disabled=not pode_criar):
        criar_usuario(email, senha)
        st.success("Conta criada com sucesso. Faça login.")

