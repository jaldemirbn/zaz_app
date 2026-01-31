# =====================================================
# zAz — MÓDULO 08
# Postagem (somente montagem final)
# =====================================================

import streamlit as st
from io import BytesIO


def _to_bytes(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def render_etapa_postagem():

    imagem = st.session_state.get("post_final_img")
    legenda = st.session_state.get("legenda")

    # só aparece quando já existir legenda (etapa 07 concluída)
    if not legenda:
        return


    # estados visuais
    if "mostrar_post" not in st.session_state:
        st.session_state["mostrar_post"] = False

    if "mostrar_legenda" not in st.session_state:
        st.session_state["mostrar_legenda"] = False


    # ---------------------------------
    # TÍTULO
    # ---------------------------------

    st.markdown(
        "<h3 style='color:#ff9d28;'>08. Postagem</h3>",
        unsafe_allow_html=True
    )


    # ---------------------------------
    # BOTÃO COLAR POST
    # ---------------------------------

    if st.button("📌 Colar post"):
        st.session_state["mostrar_post"] = True


    # ---------------------------------
    # MOSTRAR POST
    # ---------------------------------

    if st.session_state["mostrar_post"] and imagem:

        st.image(imagem)

        st.download_button(
            "⬇️ Baixar imagem",
            data=_to_bytes(imagem),
            file_name="post_zaz.png",
            mime="image/png"
        )


        # ---------------------------------
        # BOTÃO COLAR LEGENDA
        # ---------------------------------

        if st.button("📝 Colar legenda"):
            st.session_state["mostrar_legenda"] = True


    # ---------------------------------
    # MOSTRAR LEGENDA
    # ---------------------------------

    if st.session_state["mostrar_legenda"]:

        st.text_area(
            "Legenda pronta",
            legenda,
            height=280
        )
