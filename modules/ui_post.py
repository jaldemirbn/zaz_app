# =====================================================
# zAz — MÓDULO 06
# ETAPA 06 - Post
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto

from modules.post.post_simples import gerar_prompt_post_simples
from modules.post.post_animado import gerar_prompt_post_animado


# =====================================================
# IA
# =====================================================

def _gerar_descricao_post(tipo, contexto):

    if tipo == "Animado":
        base_prompt = gerar_prompt_post_animado()
    else:
        base_prompt = gerar_prompt_post_simples()

    prompt = contexto + "\n\n" + base_prompt

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
    # TIPO
    # -------------------------------------------------
    tipo = st.radio(
        "Tipo de post:",
        ["Simples", "Animado"],
        horizontal=True,
        key="tipo_post"
    )


    # -------------------------------------------------
    # GERAR
    # -------------------------------------------------
    if st.button("Criar descrição do post", use_container_width=True):

        contexto = f"""
Ideia:
{st.session_state.get("ideia_escolhida")}

Conceito visual:
{st.session_state.get("conceito_visual")}

Headline:
{st.session_state.get("headline_escolhida")}

Texto base:
{st.session_state.get("texto_escolhido")}
"""

        with st.spinner("Criando descrição..."):
            st.session_state["descricao_post"] = _gerar_descricao_post(
                tipo,
                contexto
            )


    # -------------------------------------------------
    # RESULTADO
    # -------------------------------------------------
    if st.session_state.get("descricao_post"):

        # botão copiar automático
        st.code(
            st.session_state["descricao_post"],
            language="text"
        )

        # garantia 100%
        st.download_button(
            "📥 Baixar texto completo (.txt)",
            st.session_state["descricao_post"],
            file_name="descricao_post.txt",
            mime="text/plain",
            use_container_width=True
        )


        st.link_button(
            "🎨 Criar post no Canva IA",
            "https://www.canva.com/ai",
            use_container_width=True
        )


        # -------------------------------------------------
        # NAVEGAÇÃO
        # -------------------------------------------------
        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            if st.button("⬅ Voltar", use_container_width=True):
                st.session_state.pop("descricao_post", None)
                st.session_state.pop("tipo_post", None)
                st.session_state.etapa = 4
                st.rerun()

        with col2:
            if st.button("Próximo ➡", use_container_width=True):
                st.session_state.etapa = 6
                st.rerun()
