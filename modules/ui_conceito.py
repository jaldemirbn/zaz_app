# =====================================================
# zAz — MÓDULO 02
# CONCEITO VISUAL + GERAÇÃO DE IMAGENS (IA AQUI)
# =====================================================

import streamlit as st
from modules.ia_engine import gerar_texto

from openai import OpenAI
import base64
from PIL import Image
import io

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# -------------------------------------------------
# IA — GERAR CONCEITO
# -------------------------------------------------
def _gerar_conceito(ideias: list[str]):

    texto = "\n".join(ideias)

    prompt = f"""
Com base nas ideias abaixo, crie UM conceito visual forte.

Ideias:
{texto}

Regras:
- descreva apenas a cena visual
- tom cinematográfico
- 2 a 4 frases curtas
- sem explicações
"""

    return gerar_texto(prompt).strip()


# -------------------------------------------------
# IA — GERAR IMAGENS (OPENAI REAL)
# -------------------------------------------------
def _gerar_imagens_ia(prompt: str):

    imagens = []

    # 🔥 CORREÇÃO: agora gera somente 1 imagem (antes eram 3)
    for _ in range(1):

        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        img_base64 = result.data[0].b64_json
        img_bytes = base64.b64decode(img_base64)
        img = Image.open(io.BytesIO(img_bytes))

        imagens.append(img)

    return imagens


# -------------------------------------------------
# RENDER PRINCIPAL
# -------------------------------------------------
def render_etapa_conceito():

    if not st.session_state.get("modo_filtrado"):
        return

    if "conceito_visual" not in st.session_state:
        st.session_state.conceito_visual = None

    if "historico_conceitos" not in st.session_state:
        st.session_state.historico_conceitos = []

    if "imagens_geradas" not in st.session_state:
        st.session_state.imagens_geradas = []

    if "imagem_escolhida" not in st.session_state:
        st.session_state.imagem_escolhida = None

    if "ideias_cache" not in st.session_state:
        st.session_state.ideias_cache = []

    if st.session_state.ideias_cache != st.session_state.ideias:
        st.session_state.conceito_visual = None
        st.session_state.historico_conceitos = []
        st.session_state.imagens_geradas = []
        st.session_state.imagem_escolhida = None
        st.session_state.ideias_cache = st.session_state.ideias.copy()

    st.markdown(
        """
        <h3 style='color:#FF9D28; text-align:left; margin-top:20px;'>
        03. Conceito visual
        </h3>
        """,
        unsafe_allow_html=True
    )

    if not st.session_state.conceito_visual:
        with st.spinner("Criando conceito..."):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.ideias
            )

    st.info(st.session_state.conceito_visual)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):

            st.session_state.historico_conceitos.insert(
                0, st.session_state.conceito_visual
            )

            st.session_state.historico_conceitos = \
                st.session_state.historico_conceitos[:5]

            with st.spinner("Gerando novo conceito..."):
                st.session_state.conceito_visual = _gerar_conceito(
                    st.session_state.ideias
                )

            st.session_state.imagens_geradas = []
            st.session_state.imagem_escolhida = None
            st.rerun()

    with col2:
        if st.button("🎨 Gerar imagens", use_container_width=True):

            with st.spinner("Criando imagens com IA..."):
                st.session_state.imagens_geradas = _gerar_imagens_ia(
                    st.session_state.conceito_visual
                )
