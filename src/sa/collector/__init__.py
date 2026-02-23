"""
Módulo de coleta de publicações em redes sociais.

Fornece a abstração responsável por orquestrar a busca, filtragem e
pré-processamento de publicações a partir de palavras-chave categorizadas
por polaridade.
"""

from .reddit import RedditCollector

__all__ = [
    "RedditCollector",
]
