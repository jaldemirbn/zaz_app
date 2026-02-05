# =====================================================
# zAz — MÓDULO 06
# ETAPA 06 — POST (ORQUESTRADOR)
# =====================================================

import streamlit as st
from modules.post.copywriter import gerar_copy
from modules.post.designer import gerar_direcao_arte


# =====================================================
# RENDER
# =====================================================

def render_etapa_post():

    # =================================================
    # TÍTULO
    # =================================================
    st.markdown(
        "<h3 style='color:#FF9D28;'>06. Criação do post</h3>",
        unsafe_allow_html=True
    )


    # =================================================
    # INPUTS
    # =================================================
    tipo = st.radio(
        "Tipo de post:",
        ["Simples", "Animado"],
        horizontal=True,
        key="tipo_post"
    )


    # =================================================
    # AÇÃO PRINCIPAL
    # =================================================
    if st.button("✨ Criar post", use_container_width=True):

        contexto = f"""
Tema: {st.session_state.get("tema")}
Ideias: {st.session_state.get("ideias_filtradas")}
Headline base: {st.session_state.get("headline_escolhida")}
Tipo: {tipo}
"""

        with st.spinner("Gerando copy e direção de arte..."):

            # 1️⃣ COPY
            copy = gerar_copy(contexto)
            st.session_state["copy_post"] = copy

            # 2️⃣ DESIGN (DIREÇÃO DE ARTE)
            direcao = gerar_direcao_arte(contexto, copy, tipo)
            st.session_state["descricao_post"] = direcao


    # =================================================
    # RESULTADO
    # =================================================
    if st.session_state.get("descricao_post"):

        st.markdown("### 🧠 Direção de arte do post")

        st.code(
            st.session_state["descricao_post"],
            language="text"
        )

        st.link_button(
            "🎨 Abrir no Canva IA",
            "https://www.canva.com/ai",
            use_container_width=True
        )


    # =================================================
    # NAVEGAÇÃO (SEMPRE POR ÚLTIMO)
    # =================================================
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa -= 1
            st.rerun()

    with col2:
        if st.button("Seguir ➜", use_container_width=True):
            st.session_state.etapa += 1
            st.rerun()
