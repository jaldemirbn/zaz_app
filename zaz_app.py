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
from modules.ui_conceito import render_etapa_conceito
from modules.ui_imagens import render_etapa_imagens
from modules.ui_post import render_etapa_post


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
render_etapa_conceito()   # 03
render_etapa_imagens()    # 04
render_etapa_post()       # 05 (se existir)
