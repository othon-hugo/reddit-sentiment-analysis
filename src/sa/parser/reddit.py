"""Parser de argumentos CLI para coleta de posts do Reddit."""

from __future__ import annotations

import argparse
from pathlib import Path

from sa.analysis import Language
from sa.storage import StorageFormat

DEFAULT_SUBREDDIT = "conversas"
DEFAULT_LANGUAGE = Language.PT
DEFAULT_OUTPUT_FORMAT = StorageFormat.XLSX
DEFAULT_TOTAL_PER_CATEGORY = 50000


class RedditParser(argparse.ArgumentParser):
    """Parser de argumentos para coleta de posts do Reddit."""


class RedditParserNamespace(argparse.Namespace):
    """Tipagem explícita dos atributos retornados pelo parser."""

    subreddits: list[str]
    language: Language
    total: int
    output: Path
    format: StorageFormat


def create_reddit_parser() -> RedditParser:
    """Cria e configura o parser de argumentos para coleta no Reddit."""

    parser = RedditParser(
        prog="sa-reddit",
        description="Coleta posts do Reddit filtrados por palavras-chave e exporta para arquivo.",
    )

    parser.add_argument(
        "-s",
        "--subreddits",
        type=str,
        nargs="+",
        default=[DEFAULT_SUBREDDIT],
        help=f"Subreddit(s) alvo, separados por espaço (default: {DEFAULT_SUBREDDIT})",
    )

    parser.add_argument(
        "-l",
        "--language",
        type=Language,
        choices=[lang.value for lang in Language],
        default=DEFAULT_LANGUAGE.value,
        help=f"Idioma dos posts a serem coletados (default: {DEFAULT_LANGUAGE.value})",
    )

    parser.add_argument(
        "-t",
        "--total",
        type=int,
        default=DEFAULT_TOTAL_PER_CATEGORY,
        help=f"Total de posts por categoria (default: {DEFAULT_TOTAL_PER_CATEGORY})",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        required=True,
        help=f"Caminho de saída do arquivo",
    )

    parser.add_argument(
        "-f",
        "--format",
        type=StorageFormat,
        choices=[fmt.value for fmt in StorageFormat],
        default=DEFAULT_OUTPUT_FORMAT.value,
        help=f"Formato do arquivo de saída (default: {DEFAULT_OUTPUT_FORMAT.value})",
    )

    return parser


def parse_reddit_args(argv: list[str] | None = None) -> RedditParserNamespace:
    """Parseia os argumentos da linha de comando e retorna um namespace tipado."""

    parser = create_reddit_parser()

    return parser.parse_args(argv, namespace=RedditParserNamespace())
