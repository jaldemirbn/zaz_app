# =====================================================
# zAz — MÓDULO 05
# ETAPA POST VISUAL
# =====================================================

import streamlit as st
from openai import OpenAI

# 🔒 SEMPRE usar key explícita
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# =====================================================
# IA
# =====================================================

def _gerar_headline(ideias, conceito):

    prompt = f"""
Crie uma headline curta, forte e chamativa.

Ideias:
{ideias}

Conceito visual:
{conceito}

Retorne somente a headline.
"""

    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return r.choices[0].message.content.strip()


# =====================================================
# RENDER
# =====================================================

def render_etapa_post():

    st.markdown("### 04 • Post visual")

    ideias = st.session_state.get("ideias")
    conceito = st.session_state.get("conceito")

    if not ideias or not conceito:
        return


    # -------------------------------------------------
    # BOTÃO GERAR HEADLINE
    # 🔥 CORREÇÃO APLICADA AQUI (spinner anti-spam)
    # -------------------------------------------------

    if st.button("✨ Gerar headline", use_container_width=True):

        with st.spinner("Gerando headline..."):
            st.session_state["headline_post"] = _gerar_headline(ideias, conceito)


    # -------------------------------------------------
    # EXIBIR RESULTADO
    # -------------------------------------------------

    if "headline_post" in st.session_state:

        st.text_area(
            "Headline",
            st.session_state["headline_post"],
            height=100
        )

