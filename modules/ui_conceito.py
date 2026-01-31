import streamlit as st
from modules.ia_engine import gerar_texto


def _gerar_conceito(ideias: list[str]):

    texto = "\n".join(ideias)

    prompt = f"""
Crie um conceito visual cinematográfico e detalhado.

Ideias:
{texto}
"""

    return gerar_texto(prompt).strip()


def render_etapa_conceito():

    if not st.session_state.get("modo_filtrado"):
        return

    if "conceito_visual" not in st.session_state:
        st.session_state.conceito_visual = None

    if not st.session_state.conceito_visual:
        st.session_state.conceito_visual = _gerar_conceito(
            st.session_state.ideias
        )

    st.markdown(
        "<h3 style='color:#FF9D28;'>03. Conceito visual</h3>",
        unsafe_allow_html=True
    )

    st.info(st.session_state.conceito_visual)

    # -------------------------------------------------
    # COLUNAS (ESCOPO CORRETO)
    # -------------------------------------------------
    col1, col2, col3 = st.columns(3)

    # 🔁 Novo conceito
    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.ideias
            )
            st.rerun()

    # vazio (copiar removido)
    with col2:
        st.empty()

    # 🎨 Gerar imagens (libera etapa 4 + abre site)
    with col3:
        if st.button("🎨 Gerar imagens", use_container_width=True):
            st.session_state["etapa_4_liberada"] = True

            st.markdown(
                """
                <script>
                window.open("https://labs.google/fx/tools/image-fx", "_blank");
                </script>
                """,
                unsafe_allow_html=True
            )
