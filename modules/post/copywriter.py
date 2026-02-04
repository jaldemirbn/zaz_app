# =====================================================
# zAz — COPYWRITER
# Gera somente TEXTO (sem layout / sem visual)
# =====================================================

from modules.ia_engine import gerar_texto


# =====================================================
# PROMPT BASE — COPY PUBLICITÁRIA
# =====================================================
_PROMPT_COPY = """
Aja como copywriter publicitário sênior.

Crie apenas o TEXTO do post.

Não descreva imagem.
Não fale de layout.
Não sugira posição, fonte, cor ou animação.

Entregue somente a mensagem textual.

Formato obrigatório:

HEADLINE: frase curta e forte
SUBTITULO: complemento opcional
LEGENDA: texto persuasivo natural com CTA sutil

Tom humano, claro e direto.
Sem emojis.
Máx. 800 caracteres.
"""


# =====================================================
# FUNÇÃO PRINCIPAL
# =====================================================
def gerar_copy(contexto: str) -> str:

    prompt = contexto + "\n\n" + _PROMPT_COPY

    texto = gerar_texto(prompt).strip()

    texto = " ".join(texto.split())
    texto = texto[:1200]

    return texto
