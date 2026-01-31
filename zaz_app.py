# =====================================================
# zAz — APP PRINCIPAL (UX PROFISSIONAL FINAL)
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

if "aceite_termos" not in st.session_state:
    st.session_state.aceite_termos = False

if "aceite_privacidade" not in st.session_state:
    st.session_state.aceite_privacidade = False


# =====================================================
# MODAIS — LEITURA OBRIGATÓRIA
# =====================================================

@st.dialog("📄 Termos de Uso")
def modal_termos():

    st.markdown("""
COLE AQUI O TEXTO COMPLETO DOS TERMOS DE USO.

Pode ser longo.
O usuário rola até o final para aceitar.
""")

    st.markdown("---")

    if st.checkbox("Li todo o conteúdo e aceito os Termos de Uso"):
        if st.button("Confirmar aceite", use_container_width=True):
            st.session_state.aceite_termos = True
            st.rerun()


@st.dialog("🔒 Política de Privacidade")
def modal_privacidade():

    st.markdown("""
COLE AQUI O TEXTO COMPLETO DA POLÍTICA DE PRIVACIDADE.
""")

    st.markdown("---")

    if st.checkbox("Li todo o conteúdo e aceito a Política de Privacidade"):
        if st.button("Confirmar aceite", use_container_width=True):
            st.session_state.aceite_privacidade = True
            st.rerun()


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
    # CADASTRO PROFISSIONAL
    # =================================================
    with tab_cadastro:

        st.subheader("📜 Leitura obrigatória")


        col1, col2 = st.columns(2)

        # Termos
        with col1:
            if st.button(
                "Aceitar os Termos de Uso"
                if not st.session_state.aceite_termos
                else "✅ Termos aceitos",
                use_container_width=True,
                disabled=st.session_state.aceite_termos
            ):
                modal_termos()

        # Privacidade
        with col2:
            if st.button(
                "Aceitar a Política de Privacidade"
                if not st.session_state.aceite_privacidade
                else "✅ Política aceita",
                use_container_width=True,
                disabled=st.session_state.aceite_privacidade
            ):
                modal_privacidade()


        pode_criar = (
            st.session_state.aceite_termos
            and st.session_state.aceite_privacidade
        )

        st.markdown("---")

        email_novo = st.text_input("Email", disabled=not pode_criar)
        senha_nova = st.text_input("Senha", type="password", disabled=not pode_criar)

        if st.button(
            "Criar conta",
            use_container_width=True,
            disabled=not pode_criar
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
