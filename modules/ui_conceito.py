import streamlit as st
import streamlit.components.v1 as components
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR CONCEITO
# -------------------------------------------------
def _gerar_conceito(ideias: list[str]):

    texto = "\n".join(ideias)

    prompt = f"""
Crie um conceito visual cinematográfico e detalhado.

Ideias:
{texto}
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

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>03. Conceito visual</h3>",
        unsafe_allow_html=True
    )

    st.info(st.session_state.conceito_visual)

    st.caption("Copie o texto e clique em Gerar imagens para criar no site.")

    # -------------------------------------------------
    # COLUNAS
    # -------------------------------------------------
    col1, col2, col3 = st.columns(3)

    # 🔁 Novo conceito
    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.ideias
            )
            st.rerun()

    # vazio (sem botão copiar)
    with col2:
        st.empty()

    # 🎨 Gerar imagens (ABRE SITE + LIBERA ETAPA 4)
    with col3:

        components.html(
            """
            <button
                style="
                    width:100%;
                    height:38px;
                    border-radius:8px;
                    border:1px solid #444;
                    background:#111;
                    color:#FF9D28;
                    font-weight:600;
                    cursor:pointer;
                "
                onclick="window.open('https://labs.google/fx/tools/image-fx','_blank')">
                🎨 Gerar imagens
            </button>
            """,
            height=45
        )

        # libera etapa 4 no backend
        st.session_state["etapa_4_liberada"] = True
