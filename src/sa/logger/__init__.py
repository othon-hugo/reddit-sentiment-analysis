"""
Módulo de registro de eventos (logging).

Fornece infraestrutura centralizada e configurável para registro de eventos
(logs) do sistema. Contém loggers genéricos e especializados para diferentes
componentes do pipeline de NLP, padronizando os formatos de saída e os níveis
de severidade.
"""

from .reddit import RedditLogger, create_reddit_logger
from .utils import Logger, create_logger

__all__ = [
    "create_logger",
    "create_reddit_logger",
    "Logger",
    "RedditLogger",
]
