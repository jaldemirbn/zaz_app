import streamlit as st
import streamlit.components.v1 as components
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

Objetivo:
Descrever somente a IMAGEM como se fosse uma fotografia profissional de alta qualidade.

Diretrizes visuais obrigatórias:
- foto realista (NÃO é filme, NÃO é pôster, NÃO é capa, NÃO é cena cinematográfica)
- estilo fotográfico profissional moderno
- iluminação natural ou de estúdio bem definida
- cores equilibradas e harmônicas
- nitidez alta (sharp focus)
- texturas visíveis
- profundidade de campo realista
- detalhes minuciosos do ambiente
- descrição rica de materiais, superfícies, sombras, reflexos, clima, atmosfera
- enquadramento fotográfico claro (plano, ângulo, composição)
- composição forte e limpa
- sensação premium / estética profissional

Formato obrigatório:
- proporção 1:1
- imagem quadrada
- pensada para feed do Instagram
- objeto principal centralizado

Proibido:
- texto
- letras
- tipografia
- logotipos
- marcas d’água
- elementos gráficos
- narrativa ou storytelling

Saída:
Apenas UM parágrafo descrevendo detalhadamente a imagem visual.
Somente descrição visual. Nada de explicações extras.
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

    # 🎨 Gerar imagens
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
