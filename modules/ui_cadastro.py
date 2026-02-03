import streamlit as st


def render_cadastro(supabase):

    st.subheader("Criar conta")

    email = st.text_input("Email", key="cad_email")
    senha = st.text_input("Senha", type="password", key="cad_senha")

    st.divider()

    # =====================================================
    # TERMOS E PRIVACIDADE (NOVO)
    # =====================================================
    aceite_termos = st.checkbox(
        "Li e aceito os Termos de Uso",
        key="aceite_termos"
    )

    aceite_privacidade = st.checkbox(
        "Li e aceito a Política de Privacidade",
        key="aceite_privacidade"
    )

    st.caption(
        "Leia os documentos: "
        "[Termos de Uso](/Termos_de_Uso) • "
        "[Política de Privacidade](/Politica_de_Privacidade)"
    )

    st.divider()

    # =====================================================
    # BOTÃO CRIAR CONTA
    # =====================================================
    if st.button("Criar conta", use_container_width=True):

        # 🔥 BLOQUEIO OBRIGATÓRIO
        if not (aceite
