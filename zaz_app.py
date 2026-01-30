import streamlit as st

# 🔥 PRIMEIRA COISA DO APP (antes de QUALQUER st.*)
st.set_page_config(
    page_title="zAz",
    layout="wide",
    page_icon="🚀"
)

from modules.ui_logo import render_logo
from modules.ui_login import tela_login


render_logo()
tela_login()

