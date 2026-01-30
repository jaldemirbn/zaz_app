# =====================================================
# zAz — IA ENGINE
# Motor único de geração de texto com OpenAI
# REGRA: sempre retornar STRING
# =====================================================

import streamlit as st
from openai import OpenAI


# =====================================================
# CLIENTE OPENAI
# =====================================================
def _client():
    return OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# =====================================================
# FUNÇÃO BASE (GENÉRICA)
# =====================================================
def gerar_texto(prompt: str) -> str:

    client = _client()

    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
    )

    return r.choices[0].message.content.strip()


# =====================================================
# IDEIAS (usada pelo ui_ideias.py)
# =====================================================
def gerar_ideias(tema: str) -> str:

    prompt = f"""
Crie 10 ideias curtas de posts para redes sociais sobre:

{tema}

Regras:
- frases curtas
- uma por linha
- sem emojis
- sem numeração
- sem explicações
"""

    return gerar_texto(prompt)
