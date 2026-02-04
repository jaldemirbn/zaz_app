# =====================================================
# zAz — MÓDULO 04
# ETAPA 04 — CONCEITO
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from modules.state_manager import limpar_conceito


# =====================================================
# PROMPT FOTOGRÁFICO COMPLETO (CINEMATOGRÁFICO)
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
– abertura f/1.8–f/2.8 para fundo desfocado ou f/8–f/11 para paisagem nítida
– profundidade de campo realista
– compressão de perspectiva natural
– leve bokeh orgânico

Iluminação:
– luz natural ou prática realista
– direção de luz consistente
– sombras suaves ou dramáticas conforme a emoção
– contraste equilibrado

Cor e tratamento:
– paleta coerente
– tons naturais
– color grading cinematográfico sutil

Qualidade técnica:
– foco perfeito
– nitidez alta
– textura realista
– proporções reais
– ultra realista

Resultado final:
uma fotografia autêntica, profissional e cinematográfica.
"""


# =====================================================
# FUNÇÃO AUXILIAR
# =====================================================
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

    # =================================================
    # GATE → só entra se headline existir
    # =================================================
    if not st.session_state.get("headline_escolhida"):
        return


    # -----------------------------
    # STATE
    # -----------------------------
    if "conceito_visual" not in st.session_state:
        st.session_state.conceito_visual = None


    # -----------------------------
    # TÍTULO
    # -----------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>04. Conceito visual</h3>",
        unsafe_allow_html=True
    )


    headline = st.session_state.get("headline_escolhida")
    ideias = st.session_state.get("ideias_filtradas", [])


    # =================================================
    # GERAR CONCEITO
    # =================================================
    if not st.session_state.conceito_visual:

        if st.button("✨ Gerar conceito", use_container_width=True):

            with st.spinner("IA pensando como fotógrafo profissional..."):
                st.session_state.conceito_visual = _gerar_conceito(
                    ideias,
                    headline
                )

            st.rerun()

    else:
        st.code(st.session_state.conceito_visual, language="text")


    # =================================================
    # BOTÕES
    # =================================================
    st.divider()
    col1, col2, col3 = st.columns(3)


    # 🔁 NOVO CONCEITO
    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = None
            st.rerun()


    # 🎨 LINK IMAGEM
    with col2:
        st.link_button(
            "🎨 Criar imagem",
            "https://labs.google/fx/tools/image-fx",
            use_container_width=True
        )


    # ➡ SEGUIR → próxima etapa automática
    with col3:
        if st.button("Seguir ➡", use_container_width=True):
            st.session_state.etapa += 1
            st.rerun()


    # ⬅ VOLTAR → etapa anterior automática
    if st.button("⬅ Voltar", use_container_width=True):

        limpar_conceito()

        st.session_state.etapa -= 1
        st.rerun()
