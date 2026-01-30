import streamlit as st
from supabase import create_client
from modules.ui_ideias import render_etapa_ideias


# ======================
# SUPABASE
# ======================
@st.cache_resource
def conectar():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


def validar_usuario(email, senha):
    supabase = conectar()

    resp = (
        supabase.table("usuarios")
        .select("*")
        .eq("email", email)
        .eq("senha", senha)
        .execute()
    )

    return len(resp.data) > 0


# ======================
# SESSION
# ======================
if "logado" not in st.session_state:
    st.session_state.logado = False


# ======================
# LOGIN
# ======================
if not st.session_state.logado:

    st.subheader("Entrar")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar", use_container_width=True):

        if validar_usuario(email, senha):
            st.session_state.logado = True
            st.rerun()
        else:
            st.error("Email ou senha inválidos")


# ======================
# APP
# ======================
else:
    render_etapa_ideias()
