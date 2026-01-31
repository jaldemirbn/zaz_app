# =====================================================
# zAz — ARQUIVO PRINCIPAL (ORQUESTRADOR)
# =====================================================
# Responsável apenas por:
# - autenticação
# - chamar módulos na ordem
# - não conter lógica de negócio
# =====================================================

import streamlit as st
from supabase import create_client

# -------------------------------------------------
# IMPORTS DOS MÓDULOS
# -------------------------------------------------
from modules.ui_ideias import render_etapa_ideias
from modules.ui_headline import render_etapa_headline   # 👈 agora etapa 03
from modules.ui_conceito import render_etapa_conceito   # 👈 agora etapa 04
from modules.ui_imagens import render_etapa_imagens     # 👈 agora etapa 05
from modules.ui_post import render_etapa_post           # 👈 etapa 06


# -------------------------------------------------
# CONFIG BÁSICA
# -------------------------------------------------
st.set_page_config(
    page_title="zAz",
    layout="centered"
)


# -------------------------------------------------
# FLUXO SEQUENCIAL DO APP (NOVA ORDEM)
# -------------------------------------------------

render_etapa_ideias()
render_etapa_headline()
render_etapa_conceito()
render_etapa_imagens()
render_etapa_post()
