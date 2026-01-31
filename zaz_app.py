import streamlit as st
from supabase import create_client

from modules.ui_ideias import render_etapa_ideias
from modules.ui_headline import render_etapa_headline
from modules.ui_conceito import render_etapa_conceito
from modules.ui_imagens import render_etapa_imagens   # 👈 ADICIONADO


# =====================================================
# CONFIG
# =====================================================
st.set_page_config(
    page_title="zAz",
    layout="wide",
    page_icon="🚀"
)


# =====================================================
# SUPABASE
# =====================================================
@st.cache_resource
def conectar():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


def validar_usuario(email, senha):
    supabase = conectar()

    r = (
        supabase.table("usuarios")
        .select("*")
        .eq("email", email)
        .eq("senha", senha)
        .execute()
    )

    return len(r.data) > 0


# =====================================================
# SESSION
# =====================================================
if "logado" not in st.session_state:
    st.session_state.logado = False


# =====================================================
# LOGIN
# =====================================================
if not st.session_state.logado:

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.image("assets/logo.png", width=450)

        st.markdown(
            "<h2 style='text-align:center; color:#ff9d28;'>Entrar</h2>",
            unsafe_allow_html=True
        )

        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar", use_container_width=True):
            if validar_usuario(email, senha):
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Email ou senha inválidos")

    st.stop()  # 🔒 bloqueia o app até logar


# =====================================================
# FLUXO DO APP (ORDEM ATUAL)
# =====================================================

render_etapa_ideias()      # 01
render_etapa_headline()   # 02
render_etapa_conceito()   # 03
render_etapa_imagens()    # 04 ✅ próximo exibido
