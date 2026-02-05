# =====================================================
# zAz — DESIGNER ENGINE
# Responsável por gerar DIREÇÃO DE ARTE do post
# (copy + imagem + contexto → descrição visual)
# =====================================================

from modules.ia_engine import gerar_texto


# =====================================================
# PROMPT BASE — DIRETOR DE ARTE SÊNIOR
# =====================================================

PROMPT_DESIGNER = """
Você é um Designer Gráfico Sênior e Diretor de Arte.
Especialista em criação de posts profissionais para Instagram, marketing digital e campanhas visuais.

Você NÃO é redator.
Você NÃO cria textos.
Você NÃO repete a copy.

Sua única função é:
PLANEJAR VISUALMENTE O LAYOUT DO POST.

Pense como um diretor de arte experiente.

Seu trabalho é transformar a COPY em uma descrição técnica de como a imagem final deve ser composta.

Descreva de forma objetiva e profissional:

• estilo visual geral
• composição (posição do texto: topo, centro, base)
• hierarquia tipográfica
• contraste e legibilidade
• uso da imagem de fundo
• cores predominantes
• iluminação (escurecer, blur, overlay, gradiente)
• elementos gráficos (caixas, molduras, sombras, destaques)
• espaçamento e respiro
• sensação emocional da peça

IMPORTANTE:
• NÃO escrever textos novos
• NÃO repetir a copy
• NÃO usar emojis
• NÃO explicar decisões
• NÃO conversar
• NÃO usar tópicos ou listas
• NÃO colocar aspas

Escreva APENAS:
uma descrição visual única, em formato de parágrafo técnico,
como instrução direta para uma IA de geração de imagens construir o post.

Seja claro, específico e profissional.
Evite termos vagos como "bonito".
Use linguagem de direção de arte real.
"""


# =====================================================
# FUNÇÃO PRINCIPAL
# =====================================================

def gerar_direcao_arte(contexto: str, copy: str, tipo: str) -> str:
    """
    Gera a descrição estética do post.

    Entrada:
        contexto → dados das etapas anteriores (tema, headline, etc)
        copy     → texto criado pelo copywriter
        tipo     → Simples ou Animado

    Saída:
        descrição visual detalhada do layout (string)
    """

    prompt_final = f"""
{PROMPT_DESIGNER}

CONTEXTO DO PROJETO:
{contexto}

TIPO DE POST:
{tipo}

COPY PARA SER DIAGRAMADA:
{copy}
"""

    resposta = gerar_texto(prompt_final)

    return resposta.strip()
