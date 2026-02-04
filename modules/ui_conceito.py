# =====================================================
# 🤖 zAz — DNA VISUAL FOTOGRÁFICO GLOBAL
# TODAS as imagens do sistema devem seguir este padrão
# =====================================================

PROMPT_BASE_FOTOGRAFICO = """
Gere uma fotografia profissional, não ilustração, não arte digital.

Tema principal: {assunto}.

A imagem deve parecer capturada por um fotógrafo experiente em uma situação real, com naturalidade e credibilidade.

Intenção narrativa:
– transmitir {emocao}
– momento espontâneo, não posado
– sensação de história acontecendo

Composição fotográfica:
– regra dos terços ou enquadramento intencional
– linhas guia naturais
– equilíbrio visual
– negative space bem distribuído
– camadas de profundidade (foreground, midground, background)
– sem elementos distraindo

Lente e câmera:
– lente {lente}
– profundidade de campo realista
– compressão natural
– leve bokeh orgânico

Iluminação:
– luz natural realista
– sombras coerentes
– contraste equilibrado
– textura real de pele, tecido e ambiente

Cor e tratamento:
– tons naturais
– color grading cinematográfico sutil
– sem oversaturation
– sem aparência digital

Qualidade técnica:
– foco perfeito
– nitidez alta
– microtexturas visíveis
– proporções reais
– ultra realista

Acabamento:
– leve grão de filme
– estética editorial/documental
– aparência de foto profissional premiada

Resultado:
uma fotografia autêntica, sofisticada e profissional.
"""


# =====================================================
# FUNÇÃO OFICIAL DO SISTEMA
# =====================================================
def montar_prompt_fotografico(
    assunto: str,
    emocao: str = "autenticidade",
    lente: str = "50mm"
):
    """
    Monta o prompt fotográfico padrão do zAz.
    Sempre use essa função para gerar descrições de imagem.
    """

    return PROMPT_BASE_FOTOGRAFICO.format(
        assunto=assunto,
        emocao=emocao,
        lente=lente
    )
