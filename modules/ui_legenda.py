import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA
# =====================================================

def _gerar_legenda(contexto, texto_usuario, tons):

    tons_txt = ", ".join(tons)

    prompt = f"""
Você é um copywriter profissional especialista em redes sociais brasileiras.

Crie uma legenda envolvente.

REGRAS:
- 3 a 7 linhas
- emojis estratégicos
- incorporar o texto do usuário naturalmente
- respeitar os tons solicitados
- incluir CTA clara no final
- finalizar com hashtags relevantes

CONTEXTO:
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

    if "imagem_bytes" not in st.session_state:
        return

    st.markdown(
        "<h3 style='color:#FF9D28;'>08. Legenda</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # TEXTO
    # -------------------------------------------------

    texto_usuario = st.text_area(
        "O que você gostaria de colocar na legenda?",
        height=100
    )


    # -------------------------------------------------
    # TONS EM GRID 3x5
    # -------------------------------------------------

    st.write("Escolha o tom da legenda:")

    tons = [
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
            if st.checkbox(tons[i], key=f"tom_{i}"):
                tons_escolhidos.append(tons[i])

        with col2:
            if st.checkbox(tons[i+5], key=f"tom_{i+5}"):
                tons_escolhidos.append(tons[i+5])

        with col3:
            if st.checkbox(tons[i+10], key=f"tom_{i+10}"):
                tons_escolhidos.append(tons[i+10])


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
