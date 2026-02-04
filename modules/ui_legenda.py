# =====================================================
# zAz — MÓDULO 08
# ETAPA 08 — LEGENDA
# =====================================================

# =====================================================
# IMPORTS
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

Escreva uma legenda humana, natural, envolvente e persuasiva.

Regras:
- 3 a 7 frases curtas
- incluir CTA clara
- linguagem brasileira natural
- usar emojis de forma estratégica e moderada
- no máximo 1 emoji por frase
- emojis devem reforçar emoção ou CTA
- evitar emojis decorativos ou repetitivos
- priorizar emoji na frase de CTA quando fizer sentido
- hashtags devem ser reais, existentes e usadas de verdade no Instagram
- NÃO criar hashtags inventadas, genéricas ou sem sentido
- usar apenas hashtags diretamente relacionadas ao conteúdo e ao nicho
- preferir poucas hashtags relevantes em vez de muitas irrelevantes

Contexto:
Headline: {contexto.get("headline")}
Conceito: {contexto.get("conceito")}
Texto do usuário: {texto_usuario}
Tons: {tons_txt}

Formato: texto corrido normal.
"""

    bruto = gerar_texto(prompt).strip()

    import re

    hashtags = re.findall(r"#\w+", bruto)
    texto = re.sub(r"#\w+", "", bruto).strip()

    frases = re.split(r'(?<=[.!?])\s+', texto)
    frases = [f.strip() for f in frases if f.strip()]

    cta = ""
    frases_limpa = []

    gatilhos_cta = [
        "comenta", "clique", "salve", "compartilhe",
        "envie", "manda", "chama", "fale", "confira"
    ]

    for f in frases:
        if not cta and any(g in f.lower() for g in gatilhos_cta):
            cta = f
        else:
            frases_limpa.append(f)

    if not cta and frases_limpa:
        cta = frases_limpa.pop(-1)

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

    # =================================================
    # HASHTAGS EM LISTA
    # =================================================
    if hashtags:
        partes.append("Hashtags:")
        for h in hashtags:
            partes.append(f"- {h}")
        partes.append("- #zaz_app")
    else:
        partes.append("Hashtags:")
        partes.append("- #zaz_app")

    texto_final = "\n".join(partes).strip()
    texto_final = texto_final[:2200]

    return texto_final


# =====================================================
# RENDER
# =====================================================
def render_etapa_legenda():

    st.markdown(
        "<h3 style='color:#FF9D28;'>08. Legenda</h3>",
        unsafe_allow_html=True
    )

    texto_usuario = st.text_area(
        "O que você gostaria de colocar na legenda?",
        height=110
    )

    st.markdown("Escolha o tom da legenda")

    # =================================================
    # TONS (CONFORME SOLICITADO)
    # =================================================
    tons_lista = [
        "Casual",
        "Autêntico",
        "Memético",
        "Minimalista",
        "Argumentativo",
        "Sarcástico",
        "Educacional",
        "Provocativo",
        "Narrativo",
        "Dramático",
        "Motivacional",
        "Comercial",
        "Poético",
        "Persuasivo",
        "Regional"
    ]

    tons_escolhidos = []

    for i in range(5):
        col1, col2, col3 = st.columns(3)

        with col1:
            idx = i
            if idx < len(tons_lista):
                if st.checkbox(tons_lista[idx], key=f"tom_{idx}"):
                    tons_escolhidos.append(tons_lista[idx])

        with col2:
            idx = i + 5
            if idx < len(tons_lista):
                if st.checkbox(tons_lista[idx], key=f"tom_{idx}"):
                    tons_escolhidos.append(tons_lista[idx])

        with col3:
            idx = i + 10
            if idx < len(tons_lista):
                if st.checkbox(tons_lista[idx], key=f"tom_{idx}"):
                    tons_escolhidos.append(tons_lista[idx])

    # =================================================
    # GERAR
    # =================================================
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

    # =================================================
    # RESULTADO
    # =================================================
    if st.session_state.get("legenda_gerada"):
        st.code(
            st.session_state["legenda_gerada"],
            language="text"
        )

    # =================================================
    # NAVEGAÇÃO
    # =================================================
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.pop("legenda_gerada", None)
            st.session_state.etapa = 7
            st.rerun()

    with col2:
        if st.button("Seguir ➡", use_container_width=True):
            if not st.session_state.get("legenda_gerada"):
                st.warning("Crie a legenda antes de continuar.")
            else:
                st.session_state.etapa = 9
                st.rerun()
