import streamlit as st
from openai import OpenAI


def _client():
    return OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def gerar_texto(prompt: str) -> str:

    client = _client()

    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )

    return r.choices[0].message.content.strip()


def gerar_ideias(tema: str) -> str:

    prompt = f"Crie 10 ideias sobre {tema}"
    return gerar_texto(prompt)
