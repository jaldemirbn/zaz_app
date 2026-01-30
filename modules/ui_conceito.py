import streamlit as st
from modules.ia_engine import gerar_texto


def _gerar_conceito(ideias: list[str]):

    texto = "\n".join(ideias)

    prompt = f"""
Crie UM conceito visual extremamente detalhado para geração de imagem por IA.

Ideias base:
{texto}

- cena rica em detalhes
- iluminação cinematográfica
- composição profissional
- ultra realista
- 4K
- proporção 1:1 (Instagram)

Parágrafo único.
"""

    return gerar_texto(prompt).strip()


def render_etapa_conceito():

    if not st.session_state.get("modo_filtrado"):
        return

    if "conceito_visual" not in st.session_state:
        st.session_state.conceito_visual = None

    if not st.session_state.conceito_visual:
        with st.spinner("Criando conceito..."):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.ideias
            )

    st.markdown(
        "<h3 style='color:#FF9D28;'>03. Conceito visual</h3>",
        unsafe_allow_html=True
    )

    # mantém visual original
    st.info(st.session_state.conceito_visual)

    # -------------------------------------------------
    # MESMO LAYOUT (3 COLUNAS)
    # -------------------------------------------------
    col1, col2, col3 = st.columns(3)

    # 🔁 Novo conceito
    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.ideias
            )
            st.rerun()

    # 📋 Copiar (AGORA FUNCIONAL)
    with col2:
        if st.button("📋 Copiar", use_container_width=True):
            st.text_area(
                "Copie o texto abaixo:",
                value=st.session_state.conceito_visual,
                height=120
            )

    # 🎨 Link externo (igual antes)
    with col3:
        st.markdown("""
            <style>
            div[data-testid="stLinkButton"] a {
                color:#FF9D28 !important;
                font-weight:600;
            }
            </style>
        """, unsafe_allow_html=True)

        st.link_button(
            "🎨 Gerar imagens",
            "https://labs.google/fx/tools/image-fx",
            use_container_width=True
        )
