# =====================================================
#             Etapa 04 - Conceito
# =====================================================
import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR CONCEITO
# -------------------------------------------------
def _gerar_conceito(ideias: list[str], headline: str):

    texto = "\n".join(ideias)

    prompt = f"""
Crie um prompt profissional de geração de imagem para IA seguindo EXATAMENTE a estrutura:

[Sujeito] + [Ação] + [Ambiente] + [Estilo Artístico] + [Técnicas] +
[Configurações de Câmera] + [Paleta de Cores] + [Atmosfera] + [Qualidade]

Ideias:
{texto}

Headline:
{headline}

Retorne apenas a descrição técnica em um único parágrafo.
"""

    return gerar_texto(prompt).strip()


# -------------------------------------------------
# RENDER
# -------------------------------------------------
def render_etapa_conceito():

    if not st.session_state.get("headline_escolhida"):
        return


    # -------------------------------------------------
    # STATES
    # -------------------------------------------------
    if "conceito_visual" not in st.session_state:
        st.session_state.conceito_visual = None

    if "etapa_4_liberada" not in st.session_state:
        st.session_state.etapa_4_liberada = False


    # -------------------------------------------------
    # GERA AUTOMÁTICO
    # -------------------------------------------------
    if not st.session_state.conceito_visual:
        with st.spinner("Criando conceito..."):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.get("ideias", []),
                st.session_state.get("headline_escolhida")
            )


    # -------------------------------------------------
    # UI
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>04. Conceito visual</h3>",
        unsafe_allow_html=True
    )

    st.info(st.session_state.conceito_visual)

    st.caption("Copie o texto e gere a imagem no site.")


    col1, col2, col3 = st.columns(3)


    # -------------------------------------------------
    # NOVO CONCEITO
    # -------------------------------------------------
    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.get("ideias", []),
                st.session_state.get("headline_escolhida")
            )
            st.rerun()


    # -------------------------------------------------
    # LINK
    # -------------------------------------------------
    with col2:
        st.markdown(
            """
            <a href="https://labs.google/fx/tools/image-fx" target="_blank"
               style="display:block;text-align:center;padding:10px 0;
               border:1px solid #333;border-radius:8px;
               text-decoration:none;font-weight:600;color:#FF9D28;">
               🎨 Criar imagem
            </a>
            """,
            unsafe_allow_html=True
        )


    # -------------------------------------------------
    # LIBERAR IMAGEM (🔥 AGORA NÃO AVANÇA)
    # -------------------------------------------------
    with col3:
        if st.button("Colar imagem", use_container_width=True):
            st.session_state.etapa_4_liberada = True
            st.success("Upload liberado. Clique em Próximo ➡")


    # =================================================
    # 🔥 NAVEGAÇÃO WIZARD (NOVO)
    # =================================================
    st.divider()

    colA, colB = st.columns(2)

    # ⬅ VOLTAR
    with colA:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 2
            st.rerun()

    # ➡ PRÓXIMO
    with colB:
        if st.button("Próximo ➡", use_container_width=True):

            if not st.session_state.get("etapa_4_liberada"):
                st.warning("Clique em 'Colar imagem' primeiro.")
            else:
                st.session_state.etapa = 4
                st.rerun()
