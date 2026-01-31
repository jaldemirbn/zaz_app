# =====================================================
# zAz — MÓDULO 06
# ETAPA POST VISUAL
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA — GERAR DESCRIÇÃO DO POST
# =====================================================

def _gerar_descricao_post(conceito, headline):

    prompt = f"""
Você é um designer gráfico sênior especialista em posts para redes sociais.

Sua tarefa é descrever o MESMO POST utilizando:
- a imagem já definida
- a headline escolhida

IMPORTANTE:
- NÃO criar nova cena
- NÃO alterar a imagem
- NÃO inventar elementos
- usar EXATAMENTE a mesma imagem descrita
- apenas detalhar como o post será composto visualmente

Descrição da imagem (base fixa):
{conceito}

Headline:
{headline}

Crie uma descrição estratégica, profissional e clara,
explicando composição, posicionamento do texto, hierarquia visual,
equilíbrio, contraste, tipografia e intenção do design.

Retorne somente o texto da descrição.
"""

    return gerar_texto(prompt).strip()


# =====================================================
# RENDER
# =====================================================

def render_etapa_post():

    if not st.session_state.get("criar_descricao_post"):
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>06 • Post visual</h3>",
        unsafe_allow_html=True
    )

    if st.button(
        "Criar descrição do post",
        use_container_width=True,
        key="btn_criar_descricao_post"
    ):

        conceito = st.session_state.get("conceito_visual")
        headline = st.session_state.get("headline_escolhida")

        if conceito and headline:
            with st.spinner("Criando descrição..."):
                st.session_state["descricao_post"] = _gerar_descricao_post(
                    conceito,
                    headline
                )

    if st.session_state.get("descricao_post"):

        st.text_area(
            "Descrição do post",
            st.session_state["descricao_post"],
            height=400  # 👈 aumentado
        )
