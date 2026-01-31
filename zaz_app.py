# =====================================================
# zAz — ARQUIVO PRINCIPAL (ORQUESTRADOR)
# =====================================================

import streamlit as st
from supabase import create_client

# -------------------------------------------------
# IMPORTS DOS MÓDULOS
# -------------------------------------------------
from modules.ui_ideias import render_etapa_ideias
from modules.ui_headline import render_etapa_headline


# -------------------------------------------------
# CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="zAz",
    layout="centered"
)


# -------------------------------------------------
# FLUXO SEQUENCIAL (NOVA ORDEM)
# -------------------------------------------------

render_etapa_ideias()      # 01
render_etapa_headline()   # 02
