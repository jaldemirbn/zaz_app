# =====================================================
# zAz — MÓDULO 05
# ETAPA 05 — IMAGENS
# =====================================================

import streamlit as st
from PIL import Image, ImageDraw
import io


# =====================================================
# MOCK — gera imagens placeholder locais
# (até integrar IA real depois)
# =====================================================
def _gerar_mock_imagens(texto):

    imagens = []

    for i in range(4):

        img = Image.new("RGB", (1024, 1024), (20, 20, 20))
        draw = ImageDraw.Draw(img)

        frase = f"Imagem {i+1}\n\n{texto[:120]}"

        draw.text((60, 480), frase, fill=(255, 157, 40))

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")

        imagens.append(buffer.getvalue())

    return imagens


# =====================================================
# RENDER
# =====================================================
def render_etapa_imagens():

    # =================================================
    # GATE → só entra se houver conceito
    # =================================================
    if not st.session_state.get("conceito_visual"):
        return


    # -----------------------------
    # STATE
    # -----------------------------
    if "imagens_geradas" not in st.session_state:
        st.session_state.imagens_geradas = []

    if "imagem_escolhida" not in st.session_state:
        st.session_state.imagem_escolhida = None


    # -----------------------------
    # TÍTULO
    # -----------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>05. Escolha a imagem</h3>",
        unsafe_allow_html=True
    )


    conceito = st.session_state["conceito_visual"]


    # =================================================
    # GERAR IMAGENS
    # =================================================
    if not st.session_state.imagens_geradas:

        if st.button("✨ Gerar imagens", use_container_width=True):

            with st.spinner("Gerando variações visuais..."):
                st.session_state.imagens_geradas = _gerar_mock_imagens(conceito)
                st.session_state.imagem_escolhida = None

            st.rerun()


    # =================================================
    # GRID DE IMAGENS
    # =================================================
    if not st.session_state.imagens_geradas:
        return


    st.caption("Escolha uma opção:")

    cols = st.columns(2)

    for idx, img_bytes in enumerate(st.session_state.imagens_geradas):

        with cols[idx % 2]:

            st.image(img_bytes, use_container_width=True)

            if st.button(
                f"Selecionar {idx+1}",
                key=f"img_{idx}",
                use_container_width=True
            ):
                st.session_state.imagem_escolhida = img_bytes
                st.rerun()


    # =================================================
    # NAVEGAÇÃO
    # =================================================
    st.divider()

    col1, col2 = st.columns(2)


    # ⬅ VOLTAR → etapa -1
    with col1:
        if st.button("⬅ Voltar", use_container_width=True):

            st.session_state.pop("imagens_geradas", None)
            st.session_state.pop("imagem_escolhida", None)

            st.session_state.etapa -= 1
            st.rerun()


    # ➡ SEGUIR → etapa +1
    with col2:
        if st.button(
            "Seguir ➜",
            use_container_width=True,
            disabled=not st.session_state.imagem_escolhida
        ):
            st.session_state.etapa += 1
            st.rerun()
