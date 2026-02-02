#===================================================
#             Etapa 03 - Concceito
#==================================================
import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR CONCEITO (PADRÃO PROFISSIONAL ESTRUTURADO)
# -------------------------------------------------
def _gerar_conceito(ideias: list[str], headline: str):

    texto = "\n".join(ideias)

    prompt = f"""
Crie um prompt profissional de geração de imagem para IA seguindo EXATAMENTE a estrutura:

[Sujeito] + [Ação] + [Ambiente] + [Estilo Artístico] + [Técnicas] +
[Configurações de Câmera] + [Paleta de Cores] + [Atmosfera] + [Qualidade]

Objetivo:
Criar a descrição visual de um post publicitário de Instagram.

Informações base:
Ideias estratégicas:
{texto}

Headline:
{headline}

Diretrizes obrigatórias:

SUJEITO:
- elemento principal claro e impactante relacionado à headline

AÇÃO:
- pose ou interação dinâmica que comunique a mensagem

AMBIENTE:
- cenário coerente com marketing profissional

ESTILO:
- photorealistic
- cinematic
- publicidade premium

TÉCNICAS:
- depth of field
- sharp focus
- volumetric lighting
- cinematic lighting
- rim light

CÂMERA:
- DSLR
- lente 50mm ou 85mm
- f/1.8 ou f/2.8
- bokeh natural

CORES:
- paleta harmoniosa
- contraste profissional
- tons estratégicos para conversão

ATMOSFERA:
- persuasiva
- moderna
- emocional
- impacto visual forte

QUALIDADE:
- ultra-detailed
- hyper-realistic
- 8K
- HDR

FORMATO OBRIGATÓRIO:
- proporção 1:1
- resolução 1080x1080
- composição centralizada
- layout pensado para feed do Instagram

TEXTO:
- qualquer texto visível deve estar obrigatoriamente em português
- prever espaço limpo para encaixar a headline

Saída:
Retorne APENAS a descrição estruturada da imagem, em um único parágrafo técnico, sem explicações.
"""

    return gerar_texto(prompt).strip()


# -------------------------------------------------
# RENDER
# -------------------------------------------------
def render_etapa_conceito():

    if not st.session_state.get("headline_escolhida"):
        return

    if "conceito_visual" not in st.session_state:
        st.session_state.conceito_visual = None

    if not st.session_state.conceito_visual:
        with st.spinner("Criando conceito..."):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.get("ideias", []),
                st.session_state.get("headline_escolhida")
            )

    st.markdown(
        "<h3 style='color:#FF9D28;'>04. Conceito visual</h3>",
        unsafe_allow_html=True
    )

    st.info(st.session_state.conceito_visual)

    st.caption("Copie o texto (Ctrl+C) e gere a imagem no site.")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.get("ideias", []),
                st.session_state.get("headline_escolhida")
            )
            st.rerun()

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

    with col3:
        if st.button("Colar imagem", use_container_width=True, key="btn_liberar_img"):
            st.session_state["etapa_4_liberada"] = True
            st.rerun()


