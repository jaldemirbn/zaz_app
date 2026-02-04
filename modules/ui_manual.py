# =====================================================
# zAz — MÓDULO AUXILIAR
# MANUAL DO USUÁRIO
# =====================================================

import streamlit as st


# =====================================================
# RENDER
# =====================================================

def render_manual_sidebar():

    with st.sidebar:
        st.divider()
        st.markdown("## 📘 Manual do Usuário")

        if st.button("Abrir manual", use_container_width=True):
            st.session_state["abrir_manual"] = True


def render_manual_conteudo():

    if not st.session_state.get("abrir_manual", False):
        return

    st.title("📘 Manual de Uso — zAz")

    st.markdown("""
## 👋 O que é o zAz?

O zAz é um app que te ajuda a criar posts completos.

Você traz a ideia.  
O zAz monta o resto.

Imagem + texto + legenda + hashtags.  
Tudo pronto.

---

# 🧭 Como funciona?

Você segue um caminho simples:

Ideia → Conceito → Imagem → Texto → Visual → Legenda → Finalizar → Histórico

Você só avança quando termina a etapa atual.

---

# 🟢 ETAPA 1 — Ideia
Digite o assunto do post.  
Clique **Gerar ideias**.  
Escolha as melhores.

Ex: promoção, treino, dica, frase.

Objetivo: decidir **sobre o que falar**.

---

# 🟢 ETAPA 2 — Conceito
Escolha o sentimento do post.

Pergunte:
"O que quero que a pessoa sinta?"

Inspirar? Vender? Ensinar?

Objetivo: decidir **como falar**.

---

# 🟢 ETAPA 3 — Imagem
Envie uma foto base.

Ainda não edite.  
Só escolha.

Objetivo: ter o fundo do post.

---

# 🟢 ETAPA 4 — Texto (Copy)
Clique para gerar textos.  
Escolha o melhor.

Dica: escolha o mais claro.

Objetivo: ter a mensagem principal.

---

# 🟢 ETAPA 5 — Canvas (Visual)
Aqui você monta o design.

Pode:
- mover imagem
- ajustar tamanho
- posicionar texto
- baixar imagem

Sem IA. É manual.

Objetivo: montar a aparência final.

---

# 🟢 ETAPA 6 — Legenda
Gerar legendas.  
Escolher uma.

Já vem com:
- CTA
- hashtags
- emojis

Objetivo: texto do Instagram.

---

# 🟢 ETAPA 7 — Finalizar Post
Você pode:
- ver imagem
- ver legenda
- baixar arquivos
- salvar no histórico

Post pronto.

Só publicar.

---

# 🟢 ETAPA 8 — Histórico
Guarda seus posts.

Regras:
- máximo 10
- sempre os mais recentes
- antigos são apagados

Use como biblioteca.

---

# ✅ Dicas rápidas
• faça simples  
• escolha rápido  
• não encha de texto  
• baixe seus arquivos  

---

## Pronto.
Agora é só repetir o processo sempre que quiser criar outro post.
""")

    if st.button("Fechar manual"):
        st.session_state["abrir_manual"] = False
