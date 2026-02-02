import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA
# =====================================================

def _gerar_legenda(contexto, texto_usuario, tons):

    tons_txt = ", ".join(tons)

    prompt = f"""
Você é um copywriter.

Gere:
1) 3 a 7 frases curtas
2) 1 CTA
3) hashtags

Retorne EXATAMENTE nesse formato:

FRASES:
- frase 1
- frase 2
- frase 3

CTA:
cta aqui

HASHTAGS:
#tag1 #tag2 #tag3

CONTEXTO:
Headline: {contexto.get("headline")}
Conceito: {contexto.get("conceito")}
Texto usuário: {texto_usuario}
Tons: {tons_txt}
"""

    bruto = gerar_texto(prompt).strip()

    # =================================================
    # 🔥 FORMATAÇÃO CONTROLADA NO PYTHON (GARANTIA)
    # =================================================

    frases = []
    cta = ""
    hashtags = ""

    modo = None

    for linha in bruto.splitlines():

        linha = linha.strip()

        if not linha:
            continue

        if "FRASES" in linha.upper():
            modo = "frases"
            continue

        if "CTA" in linha.upper():
            modo = "cta"
            continue

        if "HASHTAGS" in linha.upper():
            modo = "hashtags"
            continue

        if modo == "frases":
            linha = linha.lstrip("- ").strip()
            frases.append(linha)

        elif modo == "cta":
            cta = linha

        elif modo == "hashtags":
            hashtags = linha

    # monta layout final (100% fixo)
    partes = []

    for f in frases:
        partes.append(f)
        partes.append("")

    partes.append("")
    partes.append(cta)
    partes.append("")
    partes.append("")
    partes.append("Criado com @zAz_app")
    partes.append("")
    partes.append("")
    partes.append(f"{hashtags} #zaz_app")

    return "\n".join(partes).strip()


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

    texto_usuario = st.text_area(
        "O que você gostaria de colocar na legenda?",
        height=110
    )

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

    if st.session_state.get("legenda_gerada"):

        st.text_area(
            "Legenda pronta",
            st.session_state["legenda_gerada"],
            height=340
        )
