# ========================================
# POST SIMPLES — LAYOUT PURO (SEM IMAGEM)
# ========================================

def gerar_prompt_post_simples():

    prompt = """
Aja como diretor de arte e diagramador sênior.

A imagem já está pronta e NÃO deve ser descrita, recriada ou modificada.

Sua única função é planejar a montagem do layout do post SOBRE a imagem existente.

Descreva apenas:
posicionamento de headline, subtítulo, CTA, blocos de cor, faixas, caixas, fundos com opacidade, tipografia (peso, tamanho, contraste), alinhamentos, margens, espaçamentos, hierarquia visual e fluxo de leitura.

Explique como organizar os elementos para gerar impacto, clareza e conversão, como se estivesse instruindo alguém a montar no Canva.

Não fale da imagem, não invente cena, não sugira nova arte.

Entregue somente instruções objetivas de layout.

Formato obrigatório: um único parágrafo contínuo, sem quebras de linha, máximo 1200 caracteres.
"""

    return prompt
