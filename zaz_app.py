import streamlit as st
from supabase import create_client


# =====================================
# CONFIG GLOBAL
# =====================================
st.set_page_config(
    page_title="zAz",
    layout="wide",
    page_icon="🚀"
)


# =====================================
# CONEXÃO BANCO
# =====================================
@st.cache_resource
def conectar():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


def validar_usuario(email, senha):
    supabase = conectar()

    res = (
        supabase
        .table("usuarios")
        .select("id")
        .eq("email", email)
        .eq("senha", senha)
        .execute()
    )

    return len(res.data) > 0


# =====================================
# LOGO
# =====================================
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("assets/logo.png", width=450)


st.markdown("<br><br>", unsafe_allow_html=True)


# =====================================
# LOGIN
# =====================================
col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    st.markdown(
        "<h2 style='color:#ff9d28;'>Entrar</h2>",
        unsafe_allow_html=True
    )

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar", use_container_width=True):

        if validar_usuario(email, senha):
            st.session_state["logado"] = True
            st.success("Login realizado com sucesso 🚀")
            st.rerun()
        else:
            st.error("Email ou senha incorretos")


# =====================================
# ÁREA INTERNA (após login)
# =====================================
if st.session_state.get("logado"):

    st.divider()
    st.header("Painel do Sistema")
    st.write("Você está logado 🔥")
