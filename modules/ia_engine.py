# =====================================================
# zAz — IA ENGINE (Versão Corrigida)
# =====================================================

import streamlit as st
from openai import OpenAI

# =====================================================
# FUNÇÃO DE SEGURANÇA (Garante que o contador exista)
# =====================================================
def inicializar_contador():
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
    # Garante que a fundação do contador está de pé
    inicializar_contador()
    
    client = _client()

    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é o assistente criativo do app zAz, focado em posts profissionais e simétricos."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
    )

    # =================================================
    # MEDIÇÃO DE TOKENS (COM TRAVA DE SEGURANÇA)
    # =================================================
    usados = r.usage.total_tokens
    st.session_state.tokens_total += usados

    print(f"Tokens usados: {usados} | Total: {st.session_state.tokens_total}")

    return r.choices[0].message.content.strip()

# =====================================================
# IDEIAS
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
