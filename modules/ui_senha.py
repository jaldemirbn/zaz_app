import streamlit as st


def render_trocar_senha(atualizar_senha):

    email = st.text_input("Email", key="alt_email")
    senha = st.text_input("Nova senha", type="password", key="alt_senha")

    if st.button("Atualizar senha", use_container_width=True):
        atualizar_senha(email, senha)
        st.success("Senha atualizada com sucesso.")

