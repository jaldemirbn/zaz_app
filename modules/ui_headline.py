# =====================================================
# zAz — MÓDULO 06
# ETAPA POST VISUAL
# =====================================================

import streamlit as st


# =====================================================
# RENDER
# =====================================================

def render_etapa_post():

    # 🔒 GATE — só libera após clicar no botão "Criar descrição do post"
    if not st.session_state.get("criar_descricao_post", False):
        return


    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>06 • Post visual</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # CONTEÚDO (inalterado)
    # -------------------------------------------------
    headline = st.session_state.get("headline_escolhida")

    if not headline:
        return

    st.text_area(
        "Headline do post",
        headline,
        height=120
    )
