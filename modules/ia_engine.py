# =====================================================
# zAz — IA ENGINE
# Motor único de geração de texto com OpenAI
# REGRA: sempre retornar STRING
# =====================================================

import streamlit as st
from openai import OpenAI


# -----------------------------------------------------
# Cliente OpenAI
# -----------------------------------------------------
def _client():
    api_key = st.secrets.get("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)


# -----------------------------------------------------
# Função base (genérica)
# -----------------------------------------------------
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


# -----------------------------------------------------
# IDEIAS
# Retorna STRING (quebra depois no UI)
# -----------------------------------------------------
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
