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
        "<h3 style='color:#FF9D28;'>06. Post visual</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # BOTÃO
    # -------------------------------------------------
    st.button(
        "Criar descrição do post",
        use_container_width=True,
        key="btn_criar_descricao_post"
    )

