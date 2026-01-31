import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR CONCEITO (PROMPT DETALHADO + 1:1)
# -------------------------------------------------
def _gerar_conceito(ideias: list[str]):

    texto = "\n".join(ideias)

    prompt = f"""
Crie a descrição de UMA IMAGEM FOTOGRÁFICA estática, extremamente detalhada e realista.

Ideias base:
{texto}

Diretrizes:
- foto realista profissional
- alta nitidez
- texturas e detalhes ricos
- luz, sombras, profundidade, cores naturais
- composição fotográfica forte
- NÃO é filme, NÃO é pôster, NÃO é capa

Formato obrigatório:
- proporção 1:1
- imagem quadrada
- feed Instagram

Proibido:
- texto
- letras
- logos
- marcas d’água
- narrativa

Saída: apenas a descrição visual detalhada em um único parágrafo.
"""

    return gerar_texto(prompt).strip()


# -------------------------------------------------
# RENDER
# -------------------------------------------------
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

    st.info(st.session_state.conceito_visual)

    st.caption("Copie o texto manualmente (Ctrl+C) e gere a imagem no site.")

    col1, col2, col3 = st.columns(3)

    # 🔁 Novo conceito
    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.ideias
            )
            st.rerun()

    # vazio
    with col2:
        st.empty()

    # -------------------------------------------------
    # 🎨 GERAR IMAGENS (PADRÃO STREAMLIT + COR)
    # -------------------------------------------------
    with col3:

        st.markdown("""
        <style>
        div[data-testid="stLinkButton"] a {
            background-color:#ff9d28 !important;
            color:black !important;
            font-weight:600 !important;
            text-align:center !important;
        }
        </style>
        """, unsafe_allow_html=True)

        if st.link_button(
            "🎨 Gerar imagens",
            "https://labs.google/fx/tools/image-fx",
            use_container_width=True
        ):
            st.session_state["etapa_4_liberada"] = True
