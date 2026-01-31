import streamlit as st
import streamlit.components.v1 as components
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR CONCEITO (PROMPT AJUSTADO)
# -------------------------------------------------
def _gerar_conceito(ideias: list[str]):

    texto = "\n".join(ideias)

   prompt = f"""
Crie a descrição de UMA IMAGEM FOTOGRÁFICA estática e realista.

Ideias:
{texto}

Regras:
- é uma FOTO (não é filme, não é pôster, não é capa)
- aparência profissional
- alta nitidez e qualidade
- descreva somente elementos visuais (ambiente, luz, cores, objetos, texturas, enquadramento)
- composição limpa e equilibrada
- enquadramento central

FORMATO OBRIGATÓRIO:
- proporção 1:1
- imagem quadrada
- pensada para feed do Instagram

Proibido:
- texto
- letras
- tipografia
- logotipos
- marcas d’água
- narrativa cinematográfica

Saída: apenas a descrição visual da imagem em um único parágrafo.
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

    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.ideias
            )
            st.rerun()

    with col2:
        st.empty()

    with col3:
        components.html(
            """
            <button style="width:100%;height:38px;color:#FF9D28;font-weight:600;"
            onclick="window.open('https://labs.google/fx/tools/image-fx','_blank')">
            🎨 Gerar imagens
            </button>
            """,
            height=45
        )

        st.session_state["etapa_4_liberada"] = True

