# =====================================================
# zAz — MÓDULO IMAGEM
# ETAPA 04 — COLAR IMAGEM (CTRL+V)
# =====================================================

import streamlit as st
import streamlit.components.v1 as components
import base64


def render_etapa_imagens():

    # 🔒 Gate
    if not st.session_state.get("etapa_4_liberada"):
        return

    st.markdown(
        "<h3 style='color:#FF9D28; margin-top:0;'>04. Colar imagem</h3>",
        unsafe_allow_html=True
    )

    st.caption("Copie a imagem no site e cole aqui (Ctrl+V).")

    # -------------------------------------------------
    # HTML que envia imagem para o Python
    # -------------------------------------------------
    html_code = """
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

    <script>
    const area = document.getElementById("paste-area");

    area.focus();

    area.addEventListener("paste", (e) => {

        const items = (e.clipboardData || e.originalEvent.clipboardData).items;

        for (const item of items) {

            if (item.type.indexOf("image") !== -1) {

                const blob = item.getAsFile();
                const reader = new FileReader();

                reader.onload = function(event) {

                    const base64 = event.target.result;

                    area.innerHTML = "";

                    const img = document.createElement("img");
                    img.src = base64;
                    img.style.maxWidth = "100%";
                    img.style.borderRadius = "12px";

                    area.appendChild(img);

                    // 🔥 envia para Streamlit
                    Streamlit.setComponentValue(base64);
                };

                reader.readAsDataURL(blob);
            }
        }
    });
    </script>
    """

    img_base64 = components.html(html_code, height=1000)

    # -------------------------------------------------
    # PYTHON RECEBE E LIBERA DOWNLOAD
    # -------------------------------------------------
    if img_base64:

        header, encoded = img_base64.split(",", 1)
        img_bytes = base64.b64decode(encoded)

        st.download_button(
            label="⬇️ Baixar imagem",
            data=img_bytes,
            file_name="post.png",
            mime="image/png",
            use_container_width=True
        )
