# =====================================================
# zAz — MÓDULO 09
# ETAPA 09 — POSTAGEM
# Preview final do post (imagem do canvas + legenda)
# =====================================================

import streamlit as st
from PIL import Image
import io


def render_etapa_postagem():

    # -------------------------------------------------
    # SÓ APARECE SE TIVER RESULTADO FINAL
    # -------------------------------------------------

    if "imagem_final_bytes" not in st.session_state:
        return

    if "legenda_gerada" not in st.session_state:
        return


    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------

    st.markdown(
        "<h3 style='color:#FF9D28;'>09. Postagem</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # PREVIEW DA IMAGEM FINAL (VEM DO CANVAS)
    # -------------------------------------------------

    img = Image.open(
        io.BytesIO(st.session_state["imagem_final_bytes"])
    )

    st.image(
        img,
        caption="Preview do post final",
        use_container_width=True
    )


    # -------------------------------------------------
    # LEGENDA FINAL
    # -------------------------------------------------

    st.text_area(
        "Legenda final",
        st.session_state["legenda_gerada"],
        height=550
    )


    # -------------------------------------------------
    # AÇÕES RÁPIDAS
    # -------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "⬇️ Baixar imagem final",
            st.session_state["imagem_final_bytes"],
            file_name="post_final.png",
            mime="image/png",
            use_container_width=True
        )

    with col2:
        st.download_button(
            "⬇️ Baixar legenda (.txt)",
            st.session_state["legenda_gerada"],
            file_name="legenda.txt",
            mime="text/plain",
            use_container_width=True
        )
