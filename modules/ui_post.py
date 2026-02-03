# =====================================================
# zAz — MÓDULO 06
# ETAPA 06 - Post
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA
# =====================================================

def _gerar_descricao_post(conceito, headline):

    prompt = f"""
Você é um designer gráfico profissional.

Planeje a montagem do post usando a imagem base.

Imagem:
{conceito}

Headline:
{headline}

Descreva tecnicamente:
posição, fonte, tamanho, cor, contraste e estilo.
"""

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
    # GERAR DESCRIÇÃO
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


        # =================================================
        # 🔥 ABRIR CANVA AI (NOVA ABA)
        # =================================================
        st.markdown(
            """
            <a href="https://www.canva.com/ai" target="_blank"
               style="
               display:block;
               text-align:center;
               padding:12px 0;
               border-radius:10px;
               font-weight:600;
               text-decoration:none;
               background:#FF9D28;
               color:black;">
               🎨 Criar post no Canva IA
            </a>
            """,
            unsafe_allow_html=True
        )


        # =================================================
        # 🔥 NAVEGAÇÃO WIZARD
        # =================================================
        st.divider()

        col1, col2 = st.columns(2)

        # ⬅ VOLTAR (imagens)
        with col1:
            if st.button("⬅ Voltar", use_container_width=True):
                st.session_state.etapa = 4
                st.rerun()

        # ➡ PRÓXIMO (canvas interno / próxima etapa)
        with col2:
            if st.button("Próximo ➡", use_container_width=True):
                st.session_state.etapa = 6
                st.rerun()
