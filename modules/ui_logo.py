# =========================================
#              LOGO
# =========================================
import streamlit as st


def render_logo():

    # espaço topo
    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.image(
            "assets/logo.png",
            width=450
        )

        st.markdown(
            """
            <hr style="margin-top:25px;margin-bottom:25px;opacity:0.2;">
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style='text-align:center'>
                <h2 style='margin-bottom:5px;'>Planejamento estratégico com IA</h1>
                <p style='opacity:0.6;'>Transforme ideias em execução</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # espaço inferior
    st.markdown("<br><br>", unsafe_allow_html=True)


