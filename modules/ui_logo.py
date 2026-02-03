import streamlit as st


# =====================================================
# CONFIG
# =====================================================
LOGO_PATH = "assets/logo.png"
LOGO_WIDTH = 450

TITULO = "Planejamento estratégico com IA."
SUBTITULO = "Transformando ideias em postagens!"


# =====================================================
# RENDER
# =====================================================
def render_logo():

    st.markdown("<br>", unsafe_allow_html=True)

    # --- logo central ---
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(LOGO_PATH, width=LOGO_WIDTH)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- título ---
    st.markdown(
        f"<h2 style='text-align:center; margin-bottom:4px;'>{TITULO}</h2>",
        unsafe_allow_html=True
    )

    # --- subtítulo ---
    st.markdown(
        f"<p style='text-align:center; opacity:0.6; margin-top:0;'>{SUBTITULO}</p>",
        unsafe_allow_html=True
    )

    st.markdown("<br><br>", unsafe_allow_html=True)
