# =====================================================
# zAz — APP PRINCIPAL
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

st.markdown(
    '<link rel="manifest" href="/manifest.json">',
    unsafe_allow_html=True
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


def criar_usuario(email, senha):
    conectar().table("usuarios").insert({
        "email": email,
        "senha": senha
    }).execute()


def atualizar_senha(email, senha):
    conectar().table("usuarios").update({
        "senha": senha
    }).eq("email", email).execute()


# =====================================================
# SESSION
# =====================================================
if "logado" not in st.session_state:
    st.session_state.logado = False

if "leu_termos" not in st.session_state:
    st.session_state.leu_termos = False

if "leu_privacidade" not in st.session_state:
    st.session_state.leu_privacidade = False


# =====================================================
# LOGIN PROFISSIONAL
# =====================================================
if not st.session_state.logado:

    tab_login, tab_cadastro, tab_senha = st.tabs(
        ["🔐 Entrar", "🆕 Criar conta", "♻️ Trocar senha"]
    )


    # =================================================
    # LOGIN
    # =================================================
    with tab_login:

        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar", use_container_width=True):
            if validar_usuario(email, senha):
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Email ou senha inválidos")


    # =================================================
    # CADASTRO COM LEITURA OBRIGATÓRIA
    # =================================================
    with tab_cadastro:

        email_novo = st.text_input("Email", key="cad_email")
        senha_nova = st.text_input("Senha", type="password", key="cad_senha")

        st.markdown("---")
        st.subheader("📜 Leitura obrigatória")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("📄 Ler Termos de Uso", use_container_width=True):
                st.session_state.leu_termos = True
                st.switch_page("pages/termos.py")

        with col2:
            if st.button("🔒 Ler Política de Privacidade", use_container_width=True):
                st.session_state.leu_privacidade = True
                st.switch_page("pages/privacidade.py")


        st.markdown("---")

        aceite_termos = False
        aceite_privacidade = False

        if st.session_state.leu_termos:
            aceite_termos = st.checkbox("Aceito os Termos de Uso")

        if st.session_state.leu_privacidade:
            aceite_privacidade = st.checkbox("Aceito a Política de Privacidade")


        pode_criar = (
            st.session_state.leu_termos
            and st.session_state.leu_privacidade
            and aceite_termos
            and aceite_privacidade
        )

        st.markdown("---")

        if st.button(
            "Criar conta",
            use_container_width=True,
            disabled=not pode_criar
        ):
            criar_usuario(email_novo, senha_nova)
            st.success("Conta criada com sucesso. Faça login.")


    # =================================================
    # TROCAR SENHA
    # =================================================
    with tab_senha:

        email_alt = st.text_input("Email")
        senha_alt = st.text_input("Nova senha", type="password")

        if st.button("Atualizar senha", use_container_width=True):
            atualizar_senha(email_alt, senha_alt)
            st.success("Senha atualizada com sucesso.")


    st.stop()


# =====================================================
# FLUXO DO APP
# =====================================================
render_etapa_ideias()
render_etapa_headline()
render_etapa_conceito()
render_etapa_imagens()
render_etapa_postagem()
render_etapa_historico()
