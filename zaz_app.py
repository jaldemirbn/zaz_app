# =====================================================
# zAz — APP PRINCIPAL (SINGLE PAGE)
# =====================================================

import streamlit as st
from supabase import create_client

from modules.ui_ideias import render_etapa_ideias
from modules.ui_headline import render_etapa_headline
from modules.ui_conceito import render_etapa_conceito
from modules.ui_imagens import render_etapa_imagens
from modules.ui_postagem import render_etapa_postagem
from modules.ui_historico import render_etapa_historico


# =====================================================
# CONFIG
# =====================================================
st.set_page_config(
    page_title="zAz",
    layout="centered",
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
    r = (
        conectar()
        .table("usuarios")
        .select("*")
        .eq("email", email)
        .eq("senha", senha)
        .execute()
    )
    return len(r.data) > 0


def criar_usuario(email, senha):
    conectar().table("usuarios").insert({
        "email": email,
        "senha": senha
    }).execute()


# =====================================================
# SESSION
# =====================================================
if "logado" not in st.session_state:
    st.session_state.logado = False


# =====================================================
# LOGIN / CADASTRO
# =====================================================
if not st.session_state.logado:

    tab_login, tab_cadastro = st.tabs(["🔐 Entrar", "🆕 Criar conta"])


    # =================================================
    # LOGIN
    # =================================================
    with tab_login:

        email = st.text_input("Email", key="login_email")
        senha = st.text_input("Senha", type="password", key="login_senha")

        if st.button("Entrar", use_container_width=True):

            if validar_usuario(email, senha):
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Email ou senha inválidos")


    # =================================================
    # CADASTRO INLINE (SEM PÁGINAS)
    # =================================================
    with tab_cadastro:

        st.subheader("📜 Termos e Privacidade")

        # =========================
        # TERMOS
        # =========================
        with st.expander("📄 Ler Termos de Uso", expanded=False):

            st.markdown("""
COLE AQUI O TEXTO COMPLETO DOS TERMOS DE USO.
Pode ser gigante. Scroll automático.
""")

            aceite_termos = st.checkbox("Li e aceito os Termos de Uso", key="aceite_termos")


        # =========================
        # PRIVACIDADE
        # =========================
        with st.expander("🔒 Ler Política de Privacidade", expanded=False):

            st.markdown("""
COLE AQUI O TEXTO COMPLETO DA POLÍTICA DE PRIVACIDADE.
""")

            aceite_privacidade = st.checkbox("Li e aceito a Política de Privacidade", key="aceite_priv")


        pode_cadastrar = aceite_termos and aceite_privacidade

        st.markdown("---")

        email_novo = st.text_input("Email", key="cad_email", disabled=not pode_cadastrar)
        senha_nova = st.text_input("Senha", type="password", key="cad_senha", disabled=not pode_cadastrar)

        if st.button(
            "Criar conta",
            use_container_width=True,
            disabled=not pode_cadastrar
        ):
            criar_usuario(email_novo, senha_nova)
            st.success("Conta criada com sucesso. Faça login.")


    st.stop()


# =====================================================
# APP PRINCIPAL
# =====================================================
render_etapa_ideias()
render_etapa_headline()
render_etapa_conceito()
render_etapa_imagens()
render_etapa_postagem()
render_etapa_historico()
