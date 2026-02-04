# =====================================================
#             Etapa 04 - Conceito (VERSÃO FINAL ESTÁVEL)
# =====================================================

import streamlit as st
from modules.state_manager import (
    limpar_conceito,
    limpar_imagens,
    limpar_texto,
    limpar_postagem
)


# =====================================================
# 🤖 PROMPT FOTOGRÁFICO CINEMATOGRÁFICO COMPLETO
# =====================================================
PROMPT_BASE_FOTOGRAFICO = """
Gere uma fotografia profissional, não ilustração, não arte digital.

Tema principal: {assunto}.

A imagem deve parecer capturada por um fotógrafo experiente em uma situação real, com naturalidade e credibilidade.

Intenção narrativa:
– transmitir {emocao}
– momento espontâneo, não posado
– sensação de história acontecendo

Composição fotográfica:
– regra dos terços ou enquadramento intencional
– uso de linhas guia naturais
– equilíbrio de peso visual
– negative space bem distribuído
– camadas de profundidade (foreground, midground, background)
– corte limpo, sem elementos distraindo

Lente e câmera:
– lente {lente}
– abertura f/1.8–f/2.8
– profundidade de campo realista
– compressão de perspectiva natural
– leve bokeh orgânico

Iluminação:
– luz natural realista
– contraste equilibrado
– textura real

Cor e tratamento:
– tons naturais
– color grading cinematográfico sutil
– sem aparência digital

Qualidade técnica:
– foco perfeito
– nitidez alta
– proporções reais
– ultra realista

Acabamento:
– leve grão de filme
– estética editorial/documental

Resultado final:
uma fotografia autêntica, sofisticada e profissional.
"""


# -------------------------------------------------
# GERAR CONCEITO
# -------------------------------------------------
def _gerar_conceito(ideias, headline):

    assunto = f"{headline} | {', '.join(ideias)}"

    return PROMPT_BASE_FOTOGRAFICO.format(
        assunto=assunto,
        emocao="conexão humana e autenticidade",
        lente="50mm"
    )


# =====================================================
# RENDER
# =====================================================
def render_etapa_conceito():

    if not st.session_state.get("headline_escolhida"):
        return


    # STATES
    if "conceito_visual" not in st.session_state:
        st.session_state.conceito_visual = None

    if "etapa_4_liberada" not in st.session_state:
        st.session_state.etapa_4_liberada = False


    st.markdown(
        "<h3 style='color:#FF9D28;'>04. Conceito visual</h3>",
        unsafe_allow_html=True
    )


    # =================================================
    # GERAR
    # =================================================
    if not st.session_state.conceito_visual:

        if st.button("✨ Gerar conceito", use_container_width=True):

            with st.spinner("IA pensando como fotógrafo profissional..."):
                st.session_state.conceito_visual = _gerar_conceito(
                    st.session_state.get("ideias", []),
                    st.session_state.get("headline_escolhida")
                )

            st.rerun()

        return


    # =================================================
    # MOSTRAR
    # =================================================
    st.text_area(
        "Prompt fotográfico gerado",
        st.session_state.conceito_visual,
        height=380
    )


    col1, col2, col3 = st.columns(3)


    # 🔁 Novo conceito
    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = None
            st.rerun()


    # 🎨 Criar imagem (🔥 BOTÃO REAL AGORA)
    with col2:
        st.link_button(
            "🎨 Criar imagem",
            "https://labs.google/fx/tools/image-fx",
            use_container_width=True
        )


    # ➡ Continuar
    with col3:
        if st.button("Continuar ➡", use_container_width=True):
            st.session_state.etapa_4_liberada = True
            st.session_state.etapa = 4
            st.rerun()


    # =================================================
    # VOLTAR
    # =========
