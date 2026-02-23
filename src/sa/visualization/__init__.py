"""
Módulo de visualização e geração de gráficos lexicais.

Fornece as funções para expor as descobertas das etapas de processamento
através de plotagens claras e auto-explicativas. Focado estritamente na
renderização sem assumir responsabilidade sobre cálculos intensos (Pipeline).
"""

from .frequency import generate_frequency_chart
from .wordcloud import generate_wordcloud

__all__ = [
    "generate_frequency_chart",
    "generate_wordcloud",
]
