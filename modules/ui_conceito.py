import streamlit as st
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR CONCEITO
# -------------------------------------------------
def _gerar_conceito(ideias: list[str], headline: str):

    texto = "\n".join(ideias)

    prompt = f"""
Você é especialista em:
- copywriting
- design gráfico
- direção de arte
- persuasão visual

Crie o conceito visual de um POST profissional para Instagram.

Base criativa:
Ideias estratégicas:
{texto}

Headline principal:
{headline}

Diretrizes obrigatórias:
- imagem fotográfica hiper-realista
- qualidade cinematográfica
- composição publicitária premium
- iluminação profissional
- forte impacto emocional

FORMATO OBRIGATÓRIO:
- proporção 1:1 (quadrado perfeito)
- resolução 1080x1080 pixels
- composição centralizada
- otimizado para feed do Instagram
- elementos equilibrados dentro de um quadro quadrado
- layout pensado especificamente para feed do Instagram
- nada panorâmico
- nada vertical
- foco total no enquadramento quadrado

TEXTO NA IMAGEM:
- obrigatoriamente em português do Brasil

Tarefa:
Descrever detalhadamente a cena visual do post já adaptada ao formato 1080x1080 pixels,
prevendo espaço ideal para aplicação da headline dentro desse enquadramento.

Retorne apenas a descrição visual em português.
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
        "<h3 style='color:#FF9D28;'>03 • Conceito visual</h3>",
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
