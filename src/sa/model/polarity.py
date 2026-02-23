from enum import Enum
from typing import Dict, List

KeywordsByPolarity = Dict["Polarity", List[str]]
"""
Alias de tipo customizado que representa o agrupamento léxico.

Mapeia uma `Polarity` associando a um acervo de suas referentes palavras
identificadoras (`List[str]`). Estrutura largamente acionada internamente para
construção orgânica das pesquisas por tópicos na interface Reddit.
"""


class Polarity(Enum):
    """
    Enumeração taxonômica representativa dos rótulos de sentimento identificados.

    Responsável por catalogar de forma finita a qual classe um determinado
    termo, frase ou post isolado será assinalado dentro de um lexo avaliativo
    do aspecto qualitativo no funil de modelagem NLP, separando-os e orientando
    os caminhos dentro dos gráficos analíticos finais.

    Attributes:
        POSITIVE: O post/conteúdo aborda caráter emocional benéfico.
        NEGATIVE: O post/conteúdo aborda caráter emocional destrutivo/prejudicial.
        NEUTRAL: Conteúdos secos/informativos carentes de avaliação emocional afetuante.

    Observações:
        - Atua rigidamente contra classificação humana divergente, impedindo erros por mistyping.
    """

    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
