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


def atualizar_senha(email, senha):
    conectar().table("usuarios").update({
        "senha": senha
    }).eq("email", email).execute()


# =====================================================
# SESSION STATES
# =====================================================
if "logado" not in st.session_state:
    st.session_state.logado = False

if "aceite_termos" not in st.session_state:
    st.session_state.aceite_termos = False

if "aceite_privacidade" not in st.session_state:
    st.session_state.aceite_privacidade = False

if "abrir_termos" not in st.session_state:
    st.session_state.abrir_termos = False

if "abrir_privacidade" not in st.session_state:
    st.session_state.abrir_privacidade = False


# =====================================================
# DIALOGS
# =====================================================

@st.dialog("Termos de Uso", width="large")
def dialog_termos():

    st.markdown("""
    ## Termos de Uso

    👉 Cole aqui o texto completo dos termos.

    Texto longo, rolagem normal...
    """)

    st.divider()

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

    👉 Cole aqui o texto completo da política.

    Texto longo...
    """)

    st.divider()

    aceite = st.checkbox("Aceitar política")

    if st.button("Confirmar"):
        if aceite:
            st.session_state.aceite_privacidade = True
            st.session_state.abrir_privacidade = False
            st.rerun()


# =====================================================
# LOGIN / CADASTRO
# =====================================================
if not st.session_state.logado:

    tab_login, tab_cadastro, tab_senha = st.tabs(
        ["🔐 Entrar", "🆕 Criar conta", "♻️ Trocar senha"]
    )


    # =================================================
    # LOGIN
    # =================================================
    with tab_login:

        email = st.text_input("Email", key="login_email")
        senha = st.text_input("Senha", type="password", key="login_senha")

        if st.button("Entrar", use_container_width=True, key="btn_login"):
            if validar_usuario(email, senha):
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Email ou senha inválidos")


    # =================================================
    # CADASTRO — UX MODAL LIMPO
    # =================================================
    with tab_cadastro:

        email_novo = st.text_input("Email", key="cad_email")
        senha_nova = st.text_input("Senha", type="password", key="cad_senha")

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            if st.session_state.aceite_termos:
                st.success("✅ Termos aceitos")
            else:
                if st.button("Aceitar os Termos de Uso"):
                    st.session_state.abrir_termos = True

        with col2:
            if st.session_state.aceite_privacidade:
                st.success("✅ Política aceita")
            else:
                if st.button("Aceitar a Política de Privacidade"):
                    st.session_state.abrir_privacidade = True


        # =========================
        # ABERTURA DOS DIALOGS (FORMA CORRETA)
        # =========================
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

        if st.button(
            "Criar conta",
            use_container_width=True,
            disabled=not pode_criar,
            key="btn_cadastro"
        ):
            criar_usuario(email_novo, senha_nova)
            st.success("Conta criada com sucesso. Faça login.")


    # =================================================
    # TROCAR SENHA
    # =================================================
    with tab_senha:

        email_alt = st.text_input("Email", key="alt_email")
        senha_alt = st.text_input("Nova senha", type="password", key="alt_senha")

        if st.button("Atualizar senha", use_container_width=True, key="btn_senha"):
            atualizar_senha(email_alt, senha_alt)
            st.success("Senha atualizada com sucesso.")

    st.stop()


# =====================================================
# FLUXO PRINCIPAL
# =====================================================
render_etapa_ideias()
render_etapa_headline()
render_etapa_conceito()
render_etapa_imagens()
render_etapa_postagem()
render_etapa_historico()
