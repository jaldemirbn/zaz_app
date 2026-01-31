import streamlit as st
from PIL import Image


def render_etapa_imagens():

    imagens = st.session_state.get("imagens_geradas")

    # 🔒 gate
    if not imagens:
        return

    if not isinstance(imagens[0], Image.Image):
        return

    # -------------------------------------------------
    # AUTO-SELEÇÃO NA PRIMEIRA EXECUÇÃO (NOVO)
    # -------------------------------------------------
    if "imagem_escolhida" not in st.session_state or st.session_state.imagem_escolhida is None:
        st.session_state.imagem_escolhida = imagens[0]

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        """
        <h3 style='color:#FF9D28; text-align:left; margin-top:24px;'>
        04. Imagens
        </h3>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # GRID
    # -------------------------------------------------
    cols = st.columns(3)

    for i, img in enumerate(imagens):
        with cols[i]:
            st.image(img, use_column_width=True)

    # -------------------------------------------------
    # SELEÇÃO
    # -------------------------------------------------
    escolha = st.radio(
        "Escolha:",
        list(range(len(imagens))),
        horizontal=True,
        index=0,  # ← primeira já marcada
        format_func=lambda x: f"Imagem {x+1}"
    )

    st.session_state.imagem_escolhida = imagens[escolha]
