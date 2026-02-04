# =====================================================
#             Etapa 04 - Conceito (VERSÃO SEGURA)
# =====================================================

import streamlit as st
from modules.state_manager import (
    limpar_conceito,
    limpar_imagens,
    limpar_texto,
    limpar_postagem
)


# =====================================================
# 🤖 PROMPT FOTOGRÁFICO EMBUTIDO (SEM IMPORT EXTERNO)
# =====================================================
PROMPT_BASE_FOTOGRAFICO = """
Gere uma fotografia profissional, não ilustração, não arte digital.

Tema principal: {assunto}.

A imagem deve parecer capturada por um fotógrafo experiente em uma situação real.

Intenção narrativa:
– transmitir {emocao}
– momento espontâneo
– sensação de história acontecendo

Composição:
– regra dos terços
– profundidade (foreground, midground, background)
– sem distrações

Lente:
– {lente}
– bokeh orgânico

Iluminação natural
Cores naturais
Ultra realista
Aparência profissional de revista.
"""


def _gerar_conceito(ideias, headline):

    assunto = f"{headline} | {', '.join(ideias)}"

    return PROMPT_BASE_FOTOGRAFICO.format(
        assunto=assunto,
        emocao="autenticidade",
        lente="50mm"
    )


# =====================================================
# RENDER
# =====================================================
def render_etapa_conceito():

    if not st.session_state.get("headline_escolhida"):
        return

    if "conceito_visual" not in st.session_state:
        st.session_state.conceito_visual = None


    st.markdown(
        "<h3 style='color:#FF9D28;'>04. Conceito visual</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # GERAR
    # -------------------------------------------------
    if not st.session_state.conceito_visual:

        if st.button("✨ Gerar conceito", use_container_width=True):

            with st.spinner("Gerando conceito..."):
                st.session_state.conceito_visual = _gerar_conceito(
                    st.session_state.get("ideias", []),
                    st.session_state.get("headline_escolhida")
                )

            st.rerun()

        return


    # -------------------------------------------------
    # MOSTRAR
    # -------------------------------------------------
    st.text_area(
        "Prompt fotográfico",
        st.session_state.conceito_visual,
        height=300
    )


    col1, col2, col3 = st.columns(3)


    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = None
            st.rerun()


    with col2:
        st.markdown(
            "[🎨 Criar imagem](https://labs.google/fx/tools/image-fx)"
        )


    with col3:
        if st.button("Continuar ➡", use_container_width=True):
            st.session_state.etapa = 4
            st.rerun()


    # -------------------------------------------------
    # VOLTAR
    # -------------------------------------------------
    st.divider()

    if st.button("⬅ Voltar", use_container_width=True):

        limpar_conceito()
        limpar_imagens()
        limpar_texto()
        limpar_postagem()

        st.session_state.etapa = 2
        st.rerun()
