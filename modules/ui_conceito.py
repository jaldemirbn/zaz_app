import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR CONCEITO (DETALHADO + FOTO + 1:1)
# -------------------------------------------------
def _gerar_conceito(ideias: list[str]):

    texto = "\n".join(ideias)

    prompt = f"""
Crie a descrição de UMA IMAGEM FOTOGRÁFICA estática, extremamente detalhada e realista.

Ideias base:
{texto}

Diretrizes obrigatórias:
- foto profissional (não é filme, não é pôster, não é capa)
- aparência natural e realista
- alta nitidez
- iluminação bem definida
- texturas visíveis
- profundidade de campo realista
- descrição rica de ambiente, luz, sombras, cores, materiais e superfícies
- composição fotográfica equilibrada
- objeto principal centralizado

Formato obrigatório:
- proporção 1:1
- imagem quadrada
- otimizada para feed do Instagram

Proibido:
- texto
- letras
- tipografia
- logotipos
- marcas d’água
- narrativa cinematográfica

Saída:
Apenas a descrição visual detalhada da imagem em um único parágrafo.
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

    st.caption("Copie o texto (Ctrl+C) e gere a imagem no site.")

    col1, col2, col3 = st.columns(3)

    # -------------------------------------------------
    # 🔁 Novo conceito
    # -------------------------------------------------
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
    # 🎨 GERAR IMAGENS (PADRÃO STREAMLIT + TEXTO LARANJA)
    # -------------------------------------------------
    with col3:

        st.markdown("""
        <style>
        div.stButton > button {
            color:#FF9D28 !important;
            font-weight:600;
        }
        </style>
        """, unsafe_allow_html=True)

        if st.button("🎨 Gerar imagens", use_container_width=True):
            st.session_state["etapa_4_liberada"] = True

            st.markdown(
                '<meta http-equiv="refresh" content="0; url=https://labs.google/fx/tools/image-fx">',
                unsafe_allow_html=True
            )
