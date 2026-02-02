import streamlit as st
from PIL import Image
import io


def render_etapa_postagem():

    st.markdown(
        "<h3 style='color:#FF9D28;'>09. Postagem</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # IMAGEM
    # -------------------------------------------------

    if "imagem_final_bytes" in st.session_state:

        img = Image.open(
            io.BytesIO(st.session_state["imagem_final_bytes"])
        )

        st.image(img, use_container_width=True)

    else:
        st.info("⚠️ Gere o Canvas para visualizar a imagem final.")


    # -------------------------------------------------
    # LEGENDA
    # -------------------------------------------------

    if "legenda_gerada" in st.session_state:

        st.text_area(
            "Legenda final",
            st.session_state["legenda_gerada"],
            height=550
        )

    else:
        st.info("⚠️ Gere a legenda para visualizar aqui.")


    # -------------------------------------------------
    # AÇÕES
    # -------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        if "imagem_final_bytes" in st.session_state:
            st.download_button(
                "⬇️ Baixar imagem",
                st.session_state["imagem_final_bytes"],
                "post_final.png",
                "image/png",
                use_container_width=True
            )

    with col2:
        if "legenda_gerada" in st.session_state:
            st.download_button(
                "⬇️ Baixar legenda",
                st.session_state["legenda_gerada"],
                "legenda.txt",
                "text/plain",
                use_container_width=True
            )
