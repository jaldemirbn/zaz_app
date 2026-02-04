# =====================================================
#             Etapa 04 - Conceito (FINAL CORRIGIDO)
# =====================================================

import streamlit as st
from modules.state_manager import (
    limpar_conceito,
    limpar_imagens,
    limpar_texto,
    limpar_postagem
)


# =====================================================
# 🎨 CSS GLOBAL (inclui link_button)
# =====================================================
st.markdown("""
<style>

div.stButton > button,
div.stDownloadButton > button,
div[data-testid="stLinkButton"] > button {
    background-color: transparent !important;
    color: #FF9D28 !important;
    font-weight: 700 !important;
    border: 1px solid #FF9D28 !important;
    border-radius: 8px !important;
}

div.stButton > button:hover,
div.stDownloadButton > button:hover,
div[data-testid="stLinkButton"] > button:hover {
    background-color: rgba(255,157,40,0.08) !important;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# PROMPT BASE
# =====================================================
PROMPT_BASE_FOTOGRAFICO = """
Gere uma fotografia profissional, não ilustração, não arte digital.

Tema principal: {assunto}.
Transmitir {emocao}.
Lente {lente}.
Ultra realista, cinematográfico, profissional.
"""


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

            with st.spinner("Gerando conceito..."):
                st.session_state.conceito_visual = _gerar_conceito(
                    st.session_state.get("ideias", []),
                    st.session_state.get("headline_escolhida")
                )

            st.rerun()

    else:

        # =================================================
        # MOSTRAR
        # =================================================
        st.text_area(
            "Prompt fotográfico gerado",
            st.session_state.conceito_visual,
            height=350
        )


    # =================================================
    # BOTÕES (🔥 SEMPRE VISÍVEIS AGORA)
    # =================================================
    st.divider()

    col1, col2, col3 = st.columns(3)


    # 🔁 novo
    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = None
            st.rerun()


    # 🎨 criar imagem
    with col2:
        st.link_button(
            "🎨 Criar imagem",
            "https://labs.google/fx/tools/image-fx",
            use_container_width=True
        )


    # ➡ continuar
    with col3:
        if st.button("Continuar ➡", use_container_width=True):
            st.session_state.etapa_4_liberada = True
            st.session_state.etapa = 4
            st.rerun()


    # =================================================
    # VOLTAR
    # =================================================
    st.divider()

    if st.button("⬅ Voltar", use_container_width=True):

        limpar_conceito()
        limpar_imagens()
        limpar_texto()
        limpar_postagem()

        st.session_state.etapa_4_liberada = False
        st.session_state.etapa = 2
        st.rerun()
