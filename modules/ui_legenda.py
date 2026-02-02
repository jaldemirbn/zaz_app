# =====================================================
# zAz — MÓDULO 08
# ETAPA 08 — LEGENDA (Copywriter com personalidade)
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA
# =====================================================

def _gerar_legenda(contexto, texto_usuario, tons):

    tons_txt = ", ".join(tons)

    prompt = f"""
Você é um copywriter profissional especialista em redes sociais brasileiras.

Crie uma legenda altamente humana, natural e envolvente.

REGRAS:
- 3 a 7 linhas
- usar emojis estrategicamente
- incorporar o texto do usuário naturalmente
- respeitar os tons solicitados
- linguagem brasileira autêntica
- incluir CTA clara no final
- finalizar com hashtags relacionadas

CONTEXTO DO POST:
Headline: {contexto.get("headline")}
Conceito visual: {contexto.get("conceito")}

Texto do usuário:
{texto_usuario}

Tons desejados:
{tons_txt}

Retorne apenas a legenda final.
"""

    return gerar_texto(prompt).strip()


# =====================================================
# RENDER
# =====================================================

def render_etapa_legenda():

    # só aparece depois do post/canvas
    if "imagem_bytes" not in st.session_state:
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>08. Legenda</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # TEXTO LIVRE
    # -------------------------------------------------

    texto_usuario = st.text_area(
        "O que você gostaria de colocar na legenda?",
        height=100
    )


    # -------------------------------------------------
    # TONS (3 COLUNAS × 5)
    # -------------------------------------------------

    grupo1 = [
        "Humorístico/Zueira",
        "Informal/Coloquial",
        "Irônico/Sarcástico",
        "Resiliente/Perrengue",
        "Acolhedor/Comunitário"
    ]

    grupo2 = [
        "Sarcasmo",
        "Educativo/Didático",
        "Inspiracional/Motivacional",
        "Vulnerável/Autêntico",
        "Visual/Emoji-heavy"
    ]

    grupo3 = [
        "Comercial/Promocional",
        "Opinião/Polêmico",
        "Profissional/Formal",
        "Nostálgico",
        "Regional/Cultural"
    ]

    col1, col2, col3 = st.columns(3)

    with col1:
        t1 = st.multiselect("Grupo 1", grupo1)

    with col2:
        t2 = st.multiselect("Grupo 2", grupo2)

    with col3:
        t3 = st.multiselect("Grupo 3", grupo3)

    tons_escolhidos = t1 + t2 + t3


    # -------------------------------------------------
    # BOTÃO
    # -------------------------------------------------

    if st.button("Criar legenda", use_container_width=True):

        contexto = {
            "headline": st.session_state.get("headline_escolhida", ""),
            "conceito": st.session_state.get("conceito_visual", "")
        }

        with st.spinner("Escrevendo legenda..."):
            st.session_state["legenda_gerada"] = _gerar_legenda(
                contexto,
                texto_usuario,
                tons_escolhidos
            )


    # -------------------------------------------------
    # RESULTADO
    # -------------------------------------------------

    if st.session_state.get("legenda_gerada"):

        st.text_area(
            "Legenda pronta",
            st.session_state["legenda_gerada"],
            height=240
        )
