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
from modules.ui_conceito import render_etapa_conceito
from modules.ui_imagens import render_etapa_imagens
from modules.ui_headline import render_etapa_headline
from modules.ui_post import render_etapa_post   # ✅ ADICIONADO


# -------------------------------------------------
# CONFIG BÁSICA
# -------------------------------------------------
st.set_page_config(
    page_title="zAz",
    layout="centered"
)


# -------------------------------------------------
# FLUXO SEQUENCIAL DO APP
# -------------------------------------------------
# Ordem oficial:
# 01 ideias
# 02 conceito
# 03 gerar imagem (site externo)
# 04 colar imagem
# 05 headline
# 06 post
# -------------------------------------------------

render_etapa_ideias()
render_etapa_conceito()
render_etapa_imagens()
render_etapa_headline()
render_etapa_post()   # ✅ ADICIONADO
