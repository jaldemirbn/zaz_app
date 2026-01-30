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

Requisitos obrigatórios:
- descrição rica em detalhes visuais
- cenário completo (ambiente, luz, cores, clima, objetos, textura, profundidade)
- enquadramento fotográfico
- estilo cinematográfico
- qualidade ultra realista
- iluminação profissional
- lente de cinema (bokeh, profundidade de campo)
- composição forte
- pronto para render 4K
- proporção 1:1 (feed Instagram)

Escreva como descrição de cena.
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

    if "historico_conceitos" not in st.session_state:
        st.session_state.historico_conceitos = []

    # gerar automaticamente se não existir
    if not st.session_state.conceito_visual:
        with st.spinner("Criando conceito..."):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.ideias
            )

    st.markdown(
        """
        <h3 style='color:#FF9D28; text-align:left; margin-top:20px;'>
        03. Conceito visual
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.info(st.session_state.conceito_visual)

    # -------------------------------------------------
    # BOTÕES
    # -------------------------------------------------
    col1, col2, col3 = st.columns(3)

    # 🔁 Novo conceito
    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            with st.spinner("Gerando novo conceito..."):
                st.session_state.conceito_visual = _gerar_conceito(
                    st.session_state.ideias
                )
            st.rerun()

    # 📋 Copiar texto
   # 📋 Copiar texto (FUNCIONAL)
with col2:
    if st.button("📋 Copiar", use_container_width=True):
        st.markdown(
            f"""
            <script>
            navigator.clipboard.writeText(`{st.session_state.conceito_visual}`);
            </script>
            """,
            unsafe_allow_html=True
        )
        st.toast("Copiado para a área de transferência")


    # 🎨 Abrir ImageFX (externo)
   # 🎨 Abrir ImageFX (cor personalizada)
with col3:
    st.markdown("""
        <style>
        div[data-testid="stLinkButton"] a {
            color: #FF9D28 !important;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

    st.link_button(
        "🎨 Gerar imagens",
        "https://labs.google/fx/tools/image-fx",
        use_container_width=True
    )
