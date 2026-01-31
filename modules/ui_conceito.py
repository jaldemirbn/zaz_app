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
- iluminação profissional
- composição publicitária premium
- forte impacto emocional

FORMATO OBRIGATÓRIO:
- proporção 1:1 (quadrado perfeito)
- resolução exata 1080x1080 pixels
- composição centralizada
- elementos equilibrados dentro do quadro
- otimizado especificamente para feed do Instagram
- nada panorâmico
- nada vertical

TEXTO NA IMAGEM:
- obrigatoriamente em português

Tarefa:
Descrever detalhadamente a cena visual do post final,
já prevendo espaço harmônico para aplicação da headline.

Retorne apenas a descrição visual em português.
"""

    return gerar_texto(prompt).strip()


# -------------------------------------------------
# RENDER
# -------------------------------------------------
def render_etapa_conceito():

    # 🔒 só aparece após escolher headline
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

    st.info(st.session_state_
