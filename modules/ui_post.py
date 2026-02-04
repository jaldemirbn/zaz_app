# =====================================================
# zAz — MÓDULO 06
# ETAPA 06 - Post (SIMPLES)
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto
from modules.post.post_simples import gerar_prompt_post_simples


# =====================================================
# IA
# =====================================================

def _gerar_descricao_post(contexto):

    base_prompt = gerar_prompt_post_simples()

    prompt = (
        contexto
        + "\n\n"
        + base_prompt
        + "\n\nFormato: texto único, sem quebras, máximo 1200 caracteres."
    )

    texto = gerar_texto(prompt).strip()

    # força 1 linha + limite
    texto = " ".join(texto.split())
    texto = texto[:1200]

    return texto


# =====================================================
# RENDER
# =====================================================

def render_etapa_post():

    st.markdown(
        "<h3 style='color:#FF9D28;'>06. Criação do post</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # GERAR
    # -------------------------------------------------
    if st.button("Criar descrição do post", use_container_width=True):

        contexto = f"""
Ideia: {st.session_state.get("ideia_escolhida")}
Conceito visual: {st.session_state.get("conceito_visual")}
Headline: {st.session_state.get("headline_escolhida")}
Texto base: {st.session_state.get("texto_escolhido")}
"""

        with st.spinner("Criando..."):
            st.session_state["descricao_post"] = _gerar_descricao_post(contexto)


    # -------------------------------------------------
    # RESULTADO
    # -------------------------------------------------
    if st.session_state.get("descricao_post"):

        # 🔥 botão copiar automático (canto do bloco)
        st.code(
            st.session_state["descricao_post"],
            language="text"
        )

        # 🔥 garantia total
        st.download_button(
            "⬇ Baixar texto (.txt)",
            st.session_state["descricao_post"],
            file_name="descricao_post.txt",
            mime="text/plain",
            use_container_width=True
        )


        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            if st.button("⬅ Voltar", use_container_width=True):
                st.session_state.pop("descricao_post", None)
                st.session_state.etapa = 4
                st.rerun()

        with col2:
            if st.button("Próximo ➡", use_container_width=True):
                st.session_state.etapa = 6
                st.rerun()
