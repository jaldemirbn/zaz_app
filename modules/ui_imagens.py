# =====================================================
# zAz — MÓDULO 03
# ETAPA IMAGENS (APENAS EXIBIÇÃO)
# =====================================================
# Regra:
# - NÃO gera imagens aqui
# - Apenas exibe imagens criadas no módulo 02
# - Só aparece após clicar "Gerar imagens"
# =====================================================

import streamlit as st
from PIL import Image


# =====================================================
# RENDER
# =====================================================

def render_etapa_imagens():

    imagens = st.session_state.get("imagens_geradas")

    # 🔒 GATE PRINCIPAL
    # se não existem imagens → não renderiza nada
    if not imagens:
        return


    # segurança extra
    if not isinstance(imagens[0], Image.Image):
        return


    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        """
        <h3 style='color:#FF9D28; text-align:left; margin-top:24px;'>
        04. Imagens
        </h3>
        """,
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # GRID 3 COLUNAS
    # -------------------------------------------------
    cols = st.columns(3)

    for i, img in enumerate(imagens):
        with cols[i]:
            st.image(img, use_column_width=True)


    # -------------------------------------------------
    # SELEÇÃO (SEM PRÉ-SELEÇÃO)
    # -------------------------------------------------
    escolha = st.radio(
        "Escolha:",
        list(range(len(imagens))),
        horizontal=True,
        index=None,
        format_func=lambda x: f"Imagem {x+1}"
    )

    if escolha is not None:
        st.session_state.imagem_escolhida = imagens[escolha]
