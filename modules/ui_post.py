# =====================================================
# zAz — MÓDULO 06
# ETAPA POST VISUAL
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA — GERAR DESCRIÇÃO DO POST
# =====================================================

def _gerar_descricao_post(conceito, headline):

    prompt = f"""
Você é um designer gráfico sênior.

INSTRUÇÃO PRINCIPAL:
Copie EXATAMENTE a descrição visual abaixo.
NÃO altere.
NÃO recrie.
NÃO modifique a cena.

Descrição visual original (copiar como base):
{conceito}

Depois disso:
acrescente apenas a explicação de como a headline será aplicada no layout.

Headline:
{headline}

Explique:
- posicionamento do texto
- contraste
- hierarquia
- legibilidade
- composição do post

Escreva somente em português.

Retorne somente o texto final.
"""

    return gerar_texto(prompt).strip()


# =====================================================
# RENDER
# =====================================================

def render_etapa_post():

    if not st.session_state.get("criar_descricao_post"):
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>06 • Post visual</h3>",
        unsafe_allow_html=True
    )

    if st.button(
        "Criar descrição do post",
        use_container_width=True,
        key="btn_criar_descricao_post"
    ):

        conceito = st.session_state.get("conceito_visual")
        headline = st.session_state.get("headline_escolhida")

        if conceito and headline:
            with st.spinner("Criando descrição..."):
