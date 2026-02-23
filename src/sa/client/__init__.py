"""
Módulo de interface com a API de redes sociais.

Fornece a abstração de cliente HTTP autenticado para comunicação com a
API pública de uma plataforma de rede social, encapsulando a biblioteca
cliente utilizada para integração com essa API.
"""

from .reddit import RedditClient, create_reddit_client

__all__ = [
    "create_reddit_client",
    "RedditClient",
]
