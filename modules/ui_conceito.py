import streamlit as st
import streamlit.components.v1 as components
from modules.ia_engine import gerar_texto


def _gerar_conceito(ideias: list[str]):

    texto = "\n".join(ideias)

    prompt = f"""
Crie um conceito visual cinematográfico e detalhado.

Ideias:
{texto}
"""

    return gerar_texto(prompt).strip()


def render_etapa_conceito():

    if not st.session_state.get("modo_filtrado"):
        return

    if "conceito_visual" not in st.session_state:
        st.session_state.conceito_visual = None

    if not st.session_state.conceito_visual:
        with st.spinner("Criando conceito..."):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.ideias
            )

    st.markdown(
        "<h3 style='color:#FF9D28;'>03. Conceito visual</h3>",
        unsafe_allow_html=True
    )

    st.caption("Texto já selecionado. Só apertar Ctrl+C.")

    # ✅ AUTO-SELEÇÃO (NOVO)
    components.html(f"""
    <textarea id="conceito"
        style="
            width:100%;
            height:140px;
            border-radius:8px;
            padding:10px;
            font-size:14px;
            border:1px solid #333;
            background:#111;
            color:#fff;
        ">{st.session_state.conceito_visual}</textarea>

    <script>
    const t = document.getElementById("conceito");
    t.focus();
    t.select();
    </script>
    """, height=170)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔁 Novo conceito", use_container_width=True):
            st.session_state.conceito_visual = _gerar_conceito(
                st.session_state.ideias
            )
            st.rerun()

    with col2:
        st.empty()

    with col3:
        components.html(
            """
            <button style="width:100%;height:38px;border-radius:8px;border:1px solid #444;background:#111;color:#FF9D28;font-weight:600;cursor:pointer;"
            onclick="window.open('https://labs.google/fx/tools/image-fx','_blank')">
            🎨 Gerar imagens
            </button>
            """,
            height=45
        )

        st.session_state["etapa_4_liberada"] = True
