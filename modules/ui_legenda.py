# =====================================================
# zAz — MÓDULO 08
# ETAPA 08 — LEGENDA
# Copywriter com tons + formatação profissional
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA
# =====================================================

def _gerar_legenda(contexto, texto_usuario, tons):

    tons_txt = ", ".join(tons)

    prompt = f"""
Você é um copywriter profissional especialista em Instagram.

OBJETIVO:
Criar uma legenda humana, envolvente e persuasiva.

REGRAS DE CONTEÚDO:
- 3 a 7 frases curtas
- usar emojis estrategicamente
- incorporar o texto do usuário naturalmente
- respeitar os tons solicitados
- linguagem brasileira autêntica
- incluir uma CTA clara e persuasiva

REGRAS DE FORMATAÇÃO (OBRIGATÓRIO):
- cada frase deve ficar em uma linha
- colocar uma linha em branco entre cada frase
- deixar a CTA isolada com uma linha antes e depois
- após a CTA escrever exatamente: Criado com @zAz_app
- deixar uma linha em branco
- finalizar com hashtags relevantes
- a última hashtag deve ser sempre #zaz_app

CONTEXTO:
Headline: {contexto.get("headline")}
Conceito visual: {contexto.get("conceito")}

Texto do usuário:
{texto_usuario}

Tons desejados:
{tons_txt}

Retorne apenas a legenda final formatada.
"""

    return gerar_texto(prompt).strip()


# =====================================================
# RENDER
# =====================================================

def render_etapa_legenda():

    # só aparece depois do canvas/post
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
        height=110
    )


    # -------------------------------------------------
    # TONS (GRID 3x5 CHECKBOX)
    # -------------------------------------------------

    st.caption("Escolha o tom da legenda")

    tons_lista = [
        "Humorístico/Zueira",
        "Informal/Coloquial",
        "Irônico/Sarcástico",
        "Resiliente/Perrengue",
        "Acolhedor/Comunitário",

        "Sarcasmo",
        "Educativo/Didático",
        "Inspiracional/Motivacional",
        "Vulnerável/Autêntico",
        "Visual/Emoji-heavy",

        "Comercial/Promocional",
        "Opinião/Polêmico",
        "Profissional/Formal",
        "Nostálgico",
        "Regional/Cultural"
    ]

    tons_escolhidos = []

    for i in range(5):
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.checkbox(tons_lista[i], key=f"tom_{i}"):
                tons_escolhidos.append(tons_lista[i])

        with col2:
            if st.checkbox(tons_lista[i+5], key=f"tom_{i+5}"):
                tons_escolhidos.append(tons_lista[i+5])

        with col3:
            if st.checkbox(tons_lista[i+10], key=f"tom_{i+10}"):
                tons_escolhidos.append(tons_lista[i+10])


    # -------------------------------------------------
    # BOTÃO GERAR
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
            height=320
        )
