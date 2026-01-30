import streamlit as st


# =====================================
# CONFIG GLOBAL (SEMPRE PRIMEIRO)
# =====================================
st.set_page_config(
    page_title="zAz",
    layout="wide",
    page_icon="🚀"
)


# =====================================
# 🔥 ESTILO APENAS DO TEXTO DO BOTÃO
# (muda só a palavra dentro do botão)
# =====================================
st.markdown("""
<style>
div.stButton > button p {
    color: #ff9d28 !important;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)


# =====================================
# LOGO
# =====================================
st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("assets/logo.png", width=450)

st.markdown("<br><br>", unsafe_allow_html=True)


# =====================================
# LOGIN
# =====================================
col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    # título laranja
    st.markdown(
        "<h2 style='color:#ff9d28;'>Entrar</h2>",
        unsafe_allow_html=True
    )

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar", use_container_width=True):
        st.success("Login clicado (backend vem depois)")
