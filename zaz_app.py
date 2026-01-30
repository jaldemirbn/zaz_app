import streamlit as st


# =====================================
# CONFIG GLOBAL
# =====================================
st.set_page_config(
    page_title="zAz",
    layout="wide",
    page_icon="🚀"
)


# =====================================
# 🔥 ESTILO DO BOTÃO (COLE AQUI)
# =====================================
st.markdown("""
<style>
div.stButton > button {
    background-color: #ff9d28;
    color: black;
    font-weight: 700;
    border-radius: 10px;
    height: 45px;
}
</style>
""", unsafe_allow_html=True)

# =====================================
# LOGIN SIMPLES
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
        st.success("Login clicado (backend vem depois)")
