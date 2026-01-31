import streamlit as st
import streamlit.components.v1 as components
from modules.ia_engine import gerar_texto


# -------------------------------------------------
# IA — GERAR CONCEITO (PROMPT CORRIGIDO)
# -------------------------------------------------
def _gerar_conceito(ideias: list[str]):

    texto = "\n".join(ideias)

    prompt = f"""
Crie a descrição de UMA IMAGEM estática, fotográfica, de alta qualidade.

Ideias base:
{texto}

Regras obrigatórias:
- NÃO é filme
- NÃO é pôster
- NÃO é capa
- é apenas uma foto realista

- descrever somente elementos visuais
- ambiente, luz, cores, objetos, textura, profundidade
- linguagem objetiva
- estilo fotográfico profissional
- alta nitidez
- proporção 1:1 (Instagram)

Proibido:
- texto
- letras
- tipografia
- logotipos
- marcas d’água

Saída: apenas a descrição visual em um único parágrafo.
"""

    return gerar_texto(prompt).strip()


# -------------------------------------------------
# RENDER
# -------------------------------------------------
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

    # textarea com seleção automática
    components.html(f"""
    <textarea id="conceito"
        style="width:100%;height:140px;border-radius:8px;padding:10px;">
{st.session_state.conceito_visual}
    </textarea>

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
            <button style="width:100%;height:38px;color:#FF9D28;font-weight:600;"
            onclick="window.open('https://labs.google/fx/tools/image-fx','_blank')">
            🎨 Gerar imagens
            </button>
            """,
            height=45
        )

        st.session_state["etapa_4_liberada"] = True
