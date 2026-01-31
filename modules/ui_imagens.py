# =====================================================
# zAz — MÓDULO 03
# ETAPA 04 — COLAR IMAGEM (CTRL+V)
# =====================================================
# Regra nova:
# - só aparece após clicar "Gerar imagens"
# - controlado por session_state["etapa_4_liberada"]
# =====================================================

import streamlit as st
import streamlit.components.v1 as components


def render_etapa_imagens():

    # -------------------------------------------------
    # 🔒 GATE (CORREÇÃO PRINCIPAL)
    # -------------------------------------------------
    if not st.session_state.get("etapa_4_liberada"):
        return

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28; margin-top:24px;'>04. Colar imagem</h3>",
        unsafe_allow_html=True
    )

    st.caption("Copie a imagem no site e cole aqui (Ctrl+V).")

    # -------------------------------------------------
    # ÁREA DE COLAGEM
    # -------------------------------------------------
   components.html(
    """
    <div id="paste-area"
         tabindex="0"
         style="
            border:2px dashed #444;
            padding:50px;
            text-align:center;
            border-radius:10px;
            color:#aaa;
            font-size:14px;
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

                    area.innerHTML = "";

                    const img = document.createElement("img");
                    img.src = event.target.result;

                    img.style.maxWidth = "100%";
                    img.style.height = "auto";
                    img.style.objectFit = "contain";
                    img.style.borderRadius = "8px";

                    area.appendChild(img);
                };

                reader.readAsDataURL(blob);
            }
        }
    });
    </script>
    """,
    height=600
)
