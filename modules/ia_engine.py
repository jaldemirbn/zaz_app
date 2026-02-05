# =====================================================
# zAz — IA ENGINE
# Motor único de geração de texto com OpenAI
# REGRA: sempre retornar STRING
# =====================================================

import streamlit as st
from openai import OpenAI


# =====================================================
# CONTADOR DE TOKENS (MEDIÇÃO DE CUSTO)
# =====================================================
if "tokens_total" not in st.session_state:
    st.session_state.tokens_total = 0


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

    # =================================================
    # MEDIÇÃO DE TOKENS
    # =================================================
    usados = r.usage.total_tokens
    st.session_state.tokens_total += usados

   st.info(f"🧮 Tokens acumulados: {st.session_state.tokens_total}")

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

