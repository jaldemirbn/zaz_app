# =====================================================
# zAz — MÓDULO 06
# ETAPA POST VISUAL
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA — GERAR DESCRIÇÃO DO POST
# =====================================================

def _gerar_descricao_post(conceito, headline, imagem_base64=None):

    imagem_info = ""

    # 🔹 se existir imagem salva, manda também
    if imagem_base64:
        imagem_info = f"""

Imagem do post em base64 (referência visual real do mesmo post):
{imagem_base64}
"""

    prompt = f"""
Você é um designer gráfico sênior especialista em criação de posts.

REGRAS OBRIGATÓRIAS:
- escrever somente em português
- usar a MESMA imagem (não alterar, não recriar)
- não inventar elementos
- apenas descrever o layout do mesmo post

Descrição original da imagem:
{conceito}

Headline escolhida:
{headline}

{imagem_info}

Tarefa:
Criar a melhor descrição possível do post final,
explicando composição, hierarquia visual, tipografia e intenção do design.

Retorne somente o texto.
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
        imagem_base64 = st.session_state.get("imagem_base64")  # 🔹 NOVO

        if conceito and headline:
            with st.spinner("Criando descrição..."):
                st.session_state["descricao_post"] = _gerar_descricao_post(
                    conceito,
                    headline,
                    imagem_base64
                )

    if st.session_state.get("descricao_post"):

        st.text_area(
            "Descrição do post",
            st.session_state["descricao_post"],
            height=400
        )
