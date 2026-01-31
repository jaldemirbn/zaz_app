# =====================================================
# zAz — MÓDULO IMAGEM
# ETAPA 04 — COLAR IMAGEM (CTRL+V)
# =====================================================

import streamlit as st
import streamlit.components.v1 as components


def render_etapa_imagens():

    if not st.session_state.get("etapa_4_liberada"):
        return

    st.markdown(
        "<h3 style='color:#FF9D28; margin-top:0;'>04. Colar imagem</h3>",
        unsafe_allow_html=True
    )

    st.caption("Copie a imagem no site e cole aqui (Ctrl+V).")

    html_code = """
    <div style="display:flex; flex-direction:column; gap:14px;">

        <div id="paste-area"
            tabindex="0"
            style="
                border:2px dashed #444;
                padding:60px;
                text-align:center;
                border-radius:12px;
                color:#aaa;
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
        </button>

    </div>

    <script>
    const area = document.getElementById("paste-area");
    const downloadBtn = document.getElementById("download-btn");

    let currentBlob = null;

    area.focus();

    area.addEventListener("paste", (e) => {

        const items = (e.clipboardData || e.originalEvent.clipboardData).items;

        for (const item of items) {

            if (item.type.indexOf("image") !== -1) {

                const blob = item.getAsFile();
                currentBlob = blob;

                const reader = new FileReader();

                reader.onload = function(event) {

                    area.innerHTML = "";

                    const img = document.createElement("img");
                    img.src = event.target.result;
                    img.style.maxWidth = "100%";
                    img.style.borderRadius = "12px";

                    area.appendChild(img);
                };

                reader.readAsDataURL(blob);
            }
        }
    });

    // 🔥 DOWNLOAD CONFIÁVEL (Blob → URL)
    downloadBtn.onclick = function() {

        if (!currentBlob) return;

        const url = URL.createObjectURL(currentBlob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "post.png";
        document.body.appendChild(a);
        a.click();

        URL.revokeObjectURL(url);
        a.remove();
    };
    </script>
    """

    components.html(html_code, height=1000)
