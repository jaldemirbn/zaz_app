# =====================================================
# zAz — MÓDULO 03
# ETAPA 03 — HEADLINE
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# IA — GERAÇÃO
# =====================================================
def _gerar_headlines(tema, ideias):

    prompt = f"""
Você é um copywriter sênior.

Tema:
{tema}

Ideias:
{ideias}

Crie 5 headlines curtas e fortes em português.
Retorne uma por linha.
"""

    resposta = gerar_texto(prompt)
    return [h.strip() for h in resposta.split("\n") if h.strip()]


# =====================================================
# RENDER PRINCIPAL
# =====================================================
def render_etapa_headline():

    # =================================================
    # GATE → só entra se houver ideias selecionadas
    # =================================================
    if not st.session_state.get("ideias_filtradas"):
        return


    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>03. Headline</h3>",
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # STATES
    # -------------------------------------------------
    tema = st.session_state.get("tema")
    ideias = st.session_state.get("ideias_filtradas")


    # =================================================
    # BOTÃO — GERAR
    # =================================================
    if st.button("✨ Gerar headline", use_container_width=True):

        with st.spinner("Gerando headlines..."):
            st.session_state["headlines"] = _gerar_headlines(tema, ideias)
            st.session_state["headline_escolhida"] = None

        st.rerun()


    # =================================================
    # LISTA
    # =================================================
    if "headlines" not in st.session_state:
        return

    headlines = st.session_state["headlines"]
    escolhida = st.session_state.get("headline_escolhida")

    opcoes = [escolhida] if escolhida else headlines

    escolha = st.radio(
        "Escolha a headline:",
        opcoes,
        index=0 if escolhida else None,
        key="radio_headline"
    )

    if escolha and not escolhida:
        st.session_state["headline_escolhida"] = escolha
        st.rerun()


    # =================================================
    # NAVEGAÇÃO
    # =================================================
    st.divider()

    col1, col2, col3 = st.columns(3)


    # 🔁 TROCAR
    with col1:
        if escolhida:
            if st.button("🔁 Trocar", use_container_width=True):
                st.session_state["headline_escolhida"] = None
                st.rerun()


    # ⬅ VOLTAR → etapa 2
    with col2:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.etapa = 2
            st.rerun()


    # ➡ SEGUIR → etapa 4
    with col3:
        if st.button(
            "Seguir ➡",
            use_container_width=True,
            disabled=not escolhida
        ):
            st.session_state.etapa = 4
            st.rerun()
