"""
Módulo principal de Processamento de Linguagem Natural (NLP).

Providencia as bibliotecas, funções analíticas e utilitários que tratam do
text mining (limpeza, lematização, filtragem e análise de sentimentos lexical).
"""

from .language import matches_language, normalize_text, preprocess_text
from .stopwords import build_stopwords, load_base_stopwords, load_extra_stopwords

__all__ = [
    "build_stopwords",
    "preprocess_text",
    "load_base_stopwords",
    "load_extra_stopwords",
    "matches_language",
    "normalize_text",
]
