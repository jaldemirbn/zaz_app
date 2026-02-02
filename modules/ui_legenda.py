# =====================================================
# zAz — MÓDULO 08
# ETAPA 08 — LEGENDA
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA
# =====================================================

def _gerar_legenda(contexto, texto_usuario, tons):

    tons_txt = ", ".join(tons)

    prompt = f"""
Você é um copywriter brasileiro especialista em Instagram.

Escreva uma legenda humana, natural e envolvente.
Use emojis estrategicamente.

Regras:
- 3 a 7 frases curtas
- incluir uma CTA clara
- incluir hashtags reais e relevantes
- linguagem brasileira natural

Contexto:
Headline: {contexto.get("headline")}
Conceito: {contexto.get("conceito")}
Texto do usuário: {texto_usuario}
Tons: {tons_txt}

Retorne o texto corrido, sem formatação especial.
"""

    bruto = gerar_texto(prompt).strip()

    # =================================================
    # 1️⃣ SEPARAR HASHTAGS
    # =================================================
    palavras = bruto.split()
    texto_sem_hashtags = []
    hashtags = []

    for p in palavras:
        if p.startswith("#"):
            hashtags.append(p)
        else:
            texto_sem_hashtags.append(p)

    texto = " ".join(texto_sem_hashtags)

    # =================================================
    # 2️⃣ SEPARAR FRASES (pontuação real)
    # =================================================
    import re
    frases = re.split(r'(?<=[.!?])\s+', texto)

    frases = [f.strip() for f in frases if len(f.strip()) > 0]

    # =================================================
    # 3️⃣ IDENTIFICAR CTA (heurística simples)
    # =================================================
    cta = ""
    frases_limpa = []

    gatilhos_cta = [
        "comenta", "clique", "clique", "salve", "compartilhe",
        "envie", "manda", "chama", "fale", "confira"
    ]

    for f in frases:
        if any(g in f.lower() for g in gatilhos_cta) and not cta:
            cta = f
        else:
            frases_limpa.append(f)

    if not cta and frases_limpa:
        cta = frases_limpa.pop(-1)

    # =================================================
    # 4️⃣ MONTAR LAYOUT FINAL (PADRÃO OURO)
    # =================================================
    partes = []

    for f in frases_limpa:
        partes.append(f)
        partes.append("")

    partes.append("")
    partes.append(cta)
    partes.append("")
    partes.append("")
    partes.append("Criado com @zAz_app")
    partes.append("")
    partes.append("")

    if hashtags:
        partes.append(" ".join(hashtags) + " #zaz_app")
    else:
        partes.append("#zaz_app")

    return "\n".join(partes).strip()


    # =================================================
    # FORMATAÇÃO CONTROLADA (SEM PERDER EMOJIS)
    # =================================================

    linhas = [l.strip() for l in bruto.split("\n") if l.strip()]

    frases = []
    hashtags = []

    for l in linhas:
        if l.startswith("#"):
            hashtags.append(l)
        else:
            frases.append(l)

    partes = []

    # frases com respiro
    for f in frases:
        partes.append(f)
        partes.append("")

    # assinatura fixa
    partes.append("")
    partes.append("Criado com @zAz_app")
    partes.append("https://www.instagram.com/j_aldemir/?hl=pt-br")
    partes.append("")
    partes.append("")

    if hashtags:
        partes.append(" ".join(hashtags) + " #zaz_app")
    else:
        partes.append("#zaz_app")

    return "\n".join(partes).strip()


# =====================================================
# RENDER
# =====================================================

def render_etapa_legenda():

    # só aparece depois do canvas/post
   if "imagem_final_bytes" not in st.session_state:
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
    # TONS
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
            if st.checkbox(tons_lista[i + 5], key=f"tom_{i + 5}"):
                tons_escolhidos.append(tons_lista[i + 5])

        with col3:
            if st.checkbox(tons_lista[i + 10], key=f"tom_{i + 10}"):
                tons_escolhidos.append(tons_lista[i + 10])

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
            height=550
        )
