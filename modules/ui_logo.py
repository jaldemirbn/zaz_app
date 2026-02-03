import streamlit as st


# =====================================================
# CONFIGURAÇÕES VISUAIS
# (ajuste rápido aqui sem mexer no resto)
# =====================================================
LOGO_PATH = "assets/logo.png"
LOGO_WIDTH = 450

TITULO = "Planejamento estratégico com IA"
SUBTITULO = "Transformando ideias em execução"

COR_SUBTITULO = 0.6
FONTE_TITULO = 28
FONTE_SUBTITULO = 16


# =====================================================
# COMPONENTES INTERNOS
# =====================================================

def _espaco_topo():
    st.markdown("<br><br>", unsafe_allow_html=True)


def _logo():
    st.image(LOGO_PATH, width=LOGO_WIDTH)


def _divisor():
    st.markdown(
        "<hr style='margin-top:25px;margin-bottom:25px;opacity:0.2;'>",
        unsafe_allow_html=True
    )


def _textos():
    st.markdown(
        f"""
        <div style='text-align:center'>
            <h2 style='margin-bottom:4px; font-size:{FONTE_TITULO}px;'>
                {TITULO}
            </h2>

            <p style='opacity:{COR_SUBTITULO}; margin-top:0px; font-size:{FONTE_SUBTITULO}px;'>
                {SUBTITULO}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def _espaco_base():
    st.markdown("<br><br>", unsafe_allow_html=True)


# =====================================================
# RENDER PRINCIPAL
# =====================================================

def render_logo():

    _espaco_topo()

    col1, col2, col3 = st.columns([0.5, 3, 0.5])

    with col2:
        _logo()
        _divisor()
        _textos()

    _espaco_base()
