# =====================================================
# zAz — MÓDULO 06
# ETAPA 06 - Post
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto

# 👇 só terceiriza o prompt
from modules.post.post_simples import gerar_prompt_post_simples


# =====================================================
# IA
# =====================================================

def _gerar_descricao_post(conceito, headline):

    prompt = gerar_prompt_post_simples()

    return gerar_texto(prompt).strip()


# =====================================================
# RENDER
# =====================================================

def render_etapa_post():

    st.markdown(
        "<h3 style='color:#FF9D28;'>06. Criação do post</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # GERAR DESCRIÇÃO (EXATAMENTE COMO ERA)
    # -------------------------------------------------
    if st.button("Criar descrição do post", use_container_width=True):

        conceito = st.session_state.get("conceito_visual")
        headline = st.session_state.get("headline_escolhida")

        if conceito and headline:
            with st.spinner("Criando descrição..."):
                st.session_state["descricao_post"] = _gerar_descricao_post(
                    conceito,
                    headline
                )


    # -------------------------------------------------
    # MOSTRA DESCRIÇÃO
    # -------------------------------------------------
    if st.session_state.get("descricao_post"):

        st.text_area(
            "Descrição do post",
            st.session_state["descricao_post"],
            height=300
        )


        # 🔥 Canva (igual)
        st.link_button(
            "🎨 Criar post no Canva IA",
            "https://www.canva.com/ai",
            use_container_width=True
        )


        # =================================================
        # 🔥 BOTÕES VOLTAR / PRÓXIMO (IGUAIS AO ORIGINAL)
        # =================================================
        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            if st.button("⬅ Voltar", use_container_width=True):
                st.session_state.etapa = 4
                st.rerun()

        with col2:
            if st.button("Próximo ➡", use_container_width=True):
                st.session_state.etapa = 6
                st.rerun()
