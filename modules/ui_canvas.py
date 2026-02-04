# =====================================================
# zAz — MÓDULO 06
# ETAPA 06 — CRIAÇÃO DO POST
# =====================================================


# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from modules.ia_engine import gerar_texto


# =====================================================
# PROMPT — POST SIMPLES (COMPLETO, SEM RESUMO)
# =====================================================
def _gerar_post_simples(conceito, headline):

    prompt = f"""
Aja como um diretor de arte e designer gráfico sênior.

Sua função é criar a descrição técnica completa de um post estático profissional para redes sociais.

Formato padrão: vertical 1:1 ou 4:5.
Foco em impacto visual imediato, clareza e conversão.

Tema:
{conceito}

Headline:
{headline}

Analise:
– tema
– objetivo do post
– público-alvo
– emoção desejada

Gere:

1. Conceito criativo
– ideia central forte
– metáfora visual simples
– mensagem direta

2. Direção de design
– paleta de cores coerente
– tipografia profissional
– hierarquia clara
– layout limpo
– estética moderna e premium

3. Composição visual
– posição do texto
– margens e respiro
– equilíbrio visual
– uso de contraste
– foco principal
– leitura rápida

4. Especificações técnicas
– proporção ideal
– tamanho recomendado
– nitidez
– contraste
– exportação otimizada para redes sociais

Regras:
– design limpo
– poucos elementos
– sem poluição visual
– aparência premium
– nada amador

Saída em formato de briefing técnico estruturado, pronto para execução no Canva ou Photoshop.
"""
    return gerar_texto(prompt).strip()


# =====================================================
# PROMPT — POST ANIMADO (SEU TEXTO INTACTO)
# =====================================================
def _gerar_post_animado(conceito, headline):

    prompt = f"""
Aja como um diretor de arte, designer gráfico e motion designer sênior.

Sua função é criar a descrição técnica completa de um post animado profissional para redes sociais.

Tema:
{conceito}

Headline:
{headline}

Duração obrigatória e fixa: 8 segundos.
Formato padrão: vertical 9:16 (Reels/Stories).
Não alterar o tempo.

Pense como um especialista em publicidade digital, focado em impacto rápido, clareza e conversão.

Analise:
– tema
– objetivo do post
– público-alvo
– emoção desejada

Gere:

1. Conceito criativo
– ideia central forte
– metáfora visual simples
– mensagem direta

2. Direção de design
– paleta de cores coerente
– tipografia profissional
– hierarquia clara
– layout limpo
– estética moderna e premium

3. Roteiro de animação (obrigatório com tempo cronometrado)

Estrutura fixa:

Cena 1 – 0s a 2s (HOOK)
– impacto visual imediato
– entrada rápida (zoom, slide ou fade dinâmico)

Cena 2 – 2s a 6s (MENSAGEM)
– texto principal ou benefício
– movimento suave e profissional
– leitura clara

Cena 3 – 6s a 8s (CTA)
– oferta ou chamada para ação forte
– destaque máximo
– animação de reforço (pulse, scale, brilho leve)

4. Especificações técnicas
– 1080x1920
– 30fps
– loop suave
– otimizado para redes sociais
– exportação leve e nítida

Regras:
– design limpo
– poucos elementos por cena
– sem poluição visual
– movimento elegante
– aparência profissional
– nada amador ou exagerado

Saída em formato de briefing estruturado, pronto para execução no After Effects, Canva ou CapCut.
"""
    return gerar_texto(prompt).strip()


# =====================================================
# LIMPEZA
# =====================================================
def _limpar_post():
    st.session_state.pop("descricao_post", None)


# =====================================================
# RENDER
# =====================================================
def render_etapa_post():

    # -------------------------------------------------
    # TÍTULO
    # -------------------------------------------------
    st.markdown(
        "<h3 style='color:#FF9D28;'>06. Criação do post</h3>",
        unsafe_allow_html=True
    )


    # =================================================
    # ESCOLHA DO TIPO
    # =================================================
    tipo = st.radio(
        "Tipo de post:",
        ["Simples", "Com animação"],
        horizontal=True
    )


    # =================================================
    # BOTÃO — GERAR
    # =================================================
    if st.button("✨ Criar descrição do post", use_container_width=True):

        conceito = st.session_state.get("conceito_visual")
        headline = st.session_state.get("headline_escolhida")

        if conceito and headline:

            with st.spinner("IA planejando o post..."):

                if tipo == "Simples":
                    texto = _gerar_post_simples(conceito, headline)
                else:
                    texto = _gerar_post_animado(conceito, headline)

                st.session_state["descricao_post"] = texto


    # =================================================
    # RESULTADO
    # =================================================
    if st.session_state.get("descricao_post"):

        st.code(st.session_state["descricao_post"], language="text")

        # BOTÃO — CRIAR NO CANVA
        st.link_button(
            "🎨 Criar no Canva",
            "https://www.canva.com/ai",
            use_container_width=True
        )


    # =================================================
    # BOTÕES
    # =================================================
    st.divider()
    col1, col2 = st.columns(2)


    # BOTÃO — VOLTAR
    with col1:
        if st.button("⬅ Voltar", use_container_width=True):
            _limpar_post()
            st.session_state.etapa = 4
            st.rerun()


    # BOTÃO — PRÓXIMO
    with col2:
        if st.button("Próximo ➡", use_container_width=True):
            st.session_state.etapa = 6
            st.rerun()
