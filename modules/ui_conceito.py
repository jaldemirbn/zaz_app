# =====================================================
# ETAPA 04 — CONCEITO
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from modules.state_manager import (
    limpar_conceito,
    limpar_imagens,
    limpar_texto,
    limpar_postagem
)


# =====================================================
# CSS / ESTILO GLOBAL
# =====================================================
st.markdown("""
<style>

div.stButton > button,
div.stDownloadButton > button,
div[data-testid="stLinkButton"] button {

    background-color: transparent !important;
    color: #FF9D28 !important;
    border: 1px solid #FF9D28 !important;
    font-weight: 700 !important;
}

div.stButton > button:hover,
div.stDownloadButton > button:hover,
div[data-testid="stLinkButton"] button:hover {

    background-color: rgba(255,157,40,0.08) !important;
}

</style>
""", unsafe_allow_html=True)


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
– nada artificial ou plástico
– textura real da pele, tecido e ambiente

Cor e tratamento:
– paleta coerente
– tons de pele naturais
– color grading cinematográfico sutil
– sem oversaturation
– sem HDR exagerado
– sem aparência digital

Qualidade técnica:
– foco perfeito no sujeito
– nitidez alta
– microtexturas visíveis
– exposição correta
– sem ruído excessivo
– proporções reais
– 8k, ultra realista

Acabamento:
– leve grão de filme fotográfico
– contraste orgânico
– aparência de foto premiada de revista ou editorial
– estética documental ou cinematográfica

Resultado final:
uma fotografia autêntica, sofisticada, profissional, como se tivesse sido capturada no mundo real por um fotógrafo veterano.
"""


# =====================================================
# FUNÇÕES AUXILIARES
# =====================================================
def _gerar_conceito(ideias, headline):

    assunto = f"{headline} | {', '.join(ideias)}"

    return PROMPT_BASE_FOTOGRAFICO.format(
        assunto=assunto,
        emocao="conexão humana e autenticidade",
        lente="50mm"
    )


# =====================================================
# RENDER PRINCIPAL
# =====================================================
def render_etapa_conceito():

    if not st.session_state.get("headline_escolhida"):
        return


    # -------------------------------------------------
    # STATES
    # -------------------------------------------------
    if "conceito_visual" not in st.session_state:
        st.session_state.conceito_visual = None

    if "etapa_4_liberada" not in st.session_state:
        st.session_state.etapa_4_liberada = False


    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>04. Conceito visual</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # GERAR CONCEITO
    # -------------------------------------------------
    if not st.session_state.conceito_visual:

        if st.button("✨ Gerar conceito", use_container_width=True):

            with st.spinner("IA pensando como fotógrafo profissional..."):
                st.session_state.conceito_visual = _gerar_conceito(
                    st.session_state.get("ideias", []),
                    st.session_state.get("headline_escolhida")
                )

            st.rerun()

    else:

        # -------------------------------------------------
        # MOSTRAR PROMPT
        # -------------------------------------------------
        st.text_area(
            "Prompt fotográfico gerado",
            st.session_state.conceito_visual,
            height=380
        )

    # =================================================
    # BOTÕES
    # =================================================
    st.divider()
    col1, col2, col3 = st.columns(3)


    # BOTÃO — NOVO CONCEITO
    with col1:
        st.button(
            "🔁 Novo conceito",
            key="btn_novo_conceito",
            use_container_width=True
        )


    # BOTÃO — CRIAR IMAGEM
    with col2:
        st.link_button(
            "🎨 Criar imagem",
            "https://labs.google/fx/tools/image-fx",
            use_container_width=True
        )


    # BOTÃO — CONTINUAR
    with col3:
        st.button(
            "Continuar ➡",
            key="btn_continuar",
            use_container_width=True
        )


    # BOTÃO — VOLTAR
    if st.button(
        "⬅ Voltar",
        key="btn_voltar",
        use_container_width=True
    ):

        limpar_conceito()
        limpar_imagens()
        limpar_texto()
        limpar_postagem()

        st.session_state.etapa_4_liberada = False
        st.session_state.etapa = 2
        st.rerun()

