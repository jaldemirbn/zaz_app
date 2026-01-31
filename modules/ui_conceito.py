import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR CONCEITO
# -------------------------------------------------
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


# -------------------------------------------------
# RENDER PRINCIPAL
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

    # -------------------------------------------------
    # COLUNAS (ESCOPO CORRETO)
    # -------------------------------------------------
    st.caption("Copie o texto e clique no botão Gerar imagens e cole no site.")
    
    col1, col2, col3 = st.columns(3)

    # 🔁 Novo conceito
    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.ideias
            )
            st.rerun()

    # 📋 Copiar
   

   # 🎨 Gerar imagens (LIBERA ETAPA 4 + ABRE SITE)
with col3:

    st.markdown("""
        <style>
        div.stButton > button {
            height:38px;
            color:#FF9D28;
            font-weight:600;
        }
        </style>
    """, unsafe_allow_html=True)

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






