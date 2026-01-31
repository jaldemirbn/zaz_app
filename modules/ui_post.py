# =====================================================
# zAz — MÓDULO 06
# ETAPA POST VISUAL
# =====================================================

import streamlit as st


# =====================================================
# RENDER
# =====================================================

def render_etapa_post():

    # 🔒 GATE — só aparece após clicar "Criar descrição do post"
    if not st.session_state.get("criar_descricao_post"):
        return


    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>06 • Post visual</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # DADOS NECESSÁRIOS
    # -------------------------------------------------
    headline = st.session_state.get("headline_escolhida")

    if not headline:
        st.warning("Escolha uma headline primeiro.")
        return


    # -------------------------------------------------
    # PREVIEW SIMPLES (placeholder por enquanto)
    # -------------------------------------------------
    st.text_area(
        "Headline do post",
        headline,
        height=120
    )


    # -------------------------------------------------
    # BOTÃO VOLTAR (opcional reset)
    # -------------------------------------------------
    if st.button("🔁 Voltar", use_container_width=True):
        st.session_state["criar_descricao_post"] = False
        st.rerun()
