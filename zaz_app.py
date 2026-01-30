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

    # 🔥 TEXTO LARANJA
    st.markdown(
        "<h2 style=
