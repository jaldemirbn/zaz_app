# =====================================================
#             Etapa 04 - Conceito
# =====================================================

import streamlit as st
from modules.state_manager import (
    limpar_conceito,
    limpar_imagens,
    limpar_texto,
    limpar_postagem
)

# 🔥 ROBO FOTOGRÁFICO GLOBAL
from modules.prompts_fotografia import montar_prompt_fotografico


# -------------------------------------------------
# GERAR CONCEITO (USA O DNA GLOBAL DO SISTEMA)
# -------------------------------------------------
def _gerar_conceito(ideias: list[str], headline: str):

    assunto = f"{headline} | {', '.join(ideias)}"

    return montar_prompt_fotografico(
        assunto=assunto,
        emocao="conexão humana e autenticidade",
        lente="50mm"
    )


# -------------------------------------------------
# RENDER
# -------------------------------------------------
def render_etapa_conceito():

    # segurança
    if not st.session_state.get("headline_escolhida"):
        return


    # -------------------------------------------------
    # STATE
    # -------------------------------------------------
    if "conceito_visual" not in st.session_state:
        st.session_state.conceito_visual = None


    st.markdown(
        "<h3 style='color:#FF9D28;'>04. Conceito visual</h3>",
        unsafe_allow_html=True
    )


    # =================================================
    # 🤖 ROBO (GERAÇÃO EXPLÍCITA)
    # =================================================
    if not st.session_state.conceito_visual:

        c1, c2, c3 = st.columns([1, 2, 1])

        with c2:
            st.markdown("### 🤖 Diretor de Fotografia IA")
            st.caption("Vou montar um conceito fotográfico profissional pra sua imagem.")

            if st.button("✨ Gerar conceito", use_container_width=True):

                with st.spinner("Pensando como fotógrafo profissional..."):
                    st.session_state.conceito_visual = _gerar_conceito(
                        st.session_state.get("ideias", []),
                        st.session_state.get("headline_escolhida")
                    )

                st.rerun()

        return


    # =================================================
    # MOSTRAR CONCEITO
    # =================================================
    st.text_area(
        "Prompt fotográfico gerado",
        st.session_state.conceito_visual,
        height=360
    )


    # -------------------------------------------------
    # AÇÕES
    # -------------------------------------------------
    col1, col2, col3 = st.columns(3)


    # novo conceito
    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = None
            st.rerun()


    # link externo
    with col2:
        st.markdown(
            """
            <a href="https://labs.google/fx/tools/image-fx" target="_blank"
               style="display:block;text-align:center;padding:10px 0;
               border:1px solid #333;border-radius:8px;
               text-decoration:none;font-weight:600;color:#FF9D28;">
               🎨 Criar imagem
            </a>
            """,
            unsafe_allow_html=True
        )


    # continuar
    with col3:
        if st.button("Continuar ➡", use_container_width=True):
            st.session_state.etapa = 4
            st.rerun()


    # =================================================
    # VOLTAR (LIMPA FUTURO)
    # =================================================
    st.divider()

    if st.button("⬅ Voltar", use_container_width=True):

        limpar_conceito()
        limpar_imagens()
        limpar_texto()
        limpar_postagem()

        st.session_state.etapa = 2
        st.rerun()
