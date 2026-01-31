# =====================================================
# zAz — MÓDULO IMAGEM
# ETAPA 04 — COLAR IMAGEM (CTRL+V)
# =====================================================

import streamlit as st
import streamlit.components.v1 as components


def render_etapa_imagens():

    # 🔒 Gate
    if not st.session_state.get("etapa_4_liberada"):
        return

    # -------------------------------------------------
    # Título
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28; margin-top:0;'>04. Colar imagem</h3>",
        unsafe_allow_html=True
    )

    st.caption("Copie a imagem no site e cole aqui (Ctrl+V).")

    # -------------------------------------------------
    # HTML + JS
    # -------------------------------------------------
    html_code = """
    <div style="display:flex; flex-direction:column; gap:12px;">

        <div id="paste-area"
            tabindex="0"
            style="
                border:2px dashed #444;
                padding:60px;
                text-align:center;
                border-radius:12px;
                color:#aaa;
                font-size:14px;
                min-height:850px;
            ">
            Clique aqui e pressione CTRL+V para colar a imagem
        </div>

        <button id="download-btn"
            style="
                padding:10px;
                border-radius:8px;
                border:1px solid #333;
                background:#111;
                color:#FF9D28;
                font-weight:600;
                cursor:pointer;
            ">
            ⬇️ Baixar imagem
